#!/usr/bin/env python3
"""Harness kit CLI — ledger validation, state generation, session briefs.

Stdlib only. Usage:
    python3 harness.py validate [LEDGER]
    python3 harness.py state    [LEDGER] [-o STATE.md]
    python3 harness.py brief TASK --role ROLE [LEDGER]

LEDGER defaults to ledger.jsonl next to this script.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HARNESS_VERSION = "kit-0.1"
ISSUE_PREFIX = "ISSUE"  # customize per project (e.g. "MYAPP-ISSUE")
HERE = Path(__file__).resolve().parent
REPO = HERE.parent  # harness/ -> repo root

ACTORS = {"planner", "implementer", "reviewer", "approver", "facilitator",
          "maintainer", "auditor", "system"}
EVENTS = {"baseline", "phase", "task_created", "task_state", "verdict",
          "escalation", "issue", "issue_route", "decision", "human_accept",
          "audit"}
STATES = {"not_started", "in_progress", "agent_review", "machine_complete",
          "human_review", "done", "blocked"}
VERDICTS = {"accepted", "accepted_with_notes", "revise", "escalate", "blocked"}
RECOMMENDATIONS = {"optional", "advised", "strong", "required"}
MODES = {"separate", "same-session-ok"}
DEP_LEVELS = {"machine-level", "human-level"}
SEVERITIES = {"blocking", "major", "minor"}
ISSUE_STATUSES = {"open", "routed", "fixed", "closed", "deferred"}
DECISION_LEVELS = {"task-local", "cross-task", "architecture/contract",
                   "harness/process"}
PARTIES = {"human", "machine", "mixed"}          # optional acting-party sensor
CONFIDENCES = {"low", "medium", "high"}          # optional self-assessment sensor

LEGAL_TRANSITIONS = {
    None: {"not_started", "in_progress", "blocked"},
    "not_started": {"in_progress", "blocked"},
    "in_progress": {"agent_review", "blocked"},
    "agent_review": {"machine_complete", "in_progress", "blocked"},
    "machine_complete": {"human_review", "done", "in_progress"},
    "human_review": {"done", "in_progress"},
    "blocked": {"not_started", "in_progress", "agent_review"},
    "done": set(),  # terminal
}

ACCUMULATION_LEVELS = [(0, "low"), (2, "medium"), (4, "high"), (6, "extra-high")]

ROLE_RULES = {
    "implementer": """\
ROLE: Implementer
- Work only inside this task's scope; respect the out-of-scope list.
- Check the task against every listed system contract before and after coding.
- Do not change architecture invariants, contracts, schemas, or phase scope —
  append an `escalation` event and stop instead.
- When ready for review: commit the task branch, append
  `task_state: agent_review`, and stop. Never review, accept, or merge your
  own work. Never mark machine_complete or done.
- Record issues found along the way as `issue` events; do not fix unrouted
  issues.""",
    "reviewer": """\
ROLE: Reviewer
- You must be a different session/party from the implementer (validated from
  the ledger `session` field).
- Judge against the task spec, the listed contracts, and the changed
  artifacts. Tier-1 spec check always; Tier-2 re-derivation when spec author
  == implementer or the task is `separate` mode.
- Write a short prose review record (judgment and risk only — no state
  restating) and append one `verdict` event with a recommendation level and a
  fully-routed `deferred` list.
- If accepted: append `task_state: machine_complete` and merge the task branch
  into the integration branch. Never merge to stable; never mark done.""",
    "planner": """\
ROLE: Planner
- Derive bounded task specs from PLAN + architecture + contracts; declare
  scope, out-of-scope, dependency level, authoring mode, and the affected
  contracts in the `task_created` event.
- Commit the spec on the integration branch before the task branch exists.""",
    "approver": """\
ROLE: Approver (human)
- Only you move work to `done` (via `human_accept`), close phases, freeze
  contracts, approve architecture/contract or harness/process decisions, and
  promote integration branches to stable.""",
    "auditor": """\
ROLE: Auditor (process audit at the human gate)
- Fresh session: you must not be any implementer or reviewer session of the
  audited tasks (validated from the ledger).
- Your object is the PROCESS RECORD, not the product. Do not re-review code
  quality; that gate already ran.
- Mandate: findings, not reassurance. Hunt for: scope shaved relative to
  PLAN/spec; review judgment that is boilerplate rather than engagement with
  the specific contracts and diff; deferred items routed to targets that do
  not or will never exist (route laundering); recommendation levels too low
  for the surface touched; escalation signals that should have fired and
  did not.
- Output: a report per templates/audit_report.template.md — the few items
  worth the approver's minutes, what you verified, what you could NOT
  verify. You direct attention; you never approve. The human gate stays
  human.
- Finish by appending one `audit` event (tasks, findings count, report
  path). See harness/roles/AUDITOR.md for the full checklist.""",
}


# ---------------------------------------------------------------- loading

def load_ledger(path):
    """Return (events, findings). Parse errors are findings, not crashes."""
    events, findings = [], []
    try:
        text = Path(path).read_text()
    except OSError as e:
        return [], [f"line 0: cannot read ledger: {e}"]
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as e:
            findings.append(f"line {i}: invalid JSON ({e})")
            continue
        obj["_line"] = i
        events.append(obj)
    return events, findings


# ---------------------------------------------------------------- replay

class Replay:
    """Replays the ledger into current state, collecting rule findings."""

    def __init__(self, events):
        self.findings = []
        self.tasks = {}          # id -> dict(title, mode, spec, contracts, ...)
        self.task_state = {}     # id -> state
        self.task_sessions = {}  # id -> set of implementer sessions
        self.verdicts = {}       # id -> list of verdict events
        self.last_review_entry = {}  # id -> ledger line of latest agent_review
        self.accepted = set()    # tasks human-accepted
        self.issues = {}         # id -> dict(severity, summary, status, route, target)
        self.decisions = []      # decision events
        self.escalations = []    # escalation events
        self.audits = []         # audit events
        self.phases = []         # phase events
        self.stable_branch = None
        self.integration_branch = None
        self.hard_gate = None    # (task, reason) or None
        self.last_ts = None
        for ev in events:
            self.apply(ev)

    def fail(self, ev, msg):
        self.findings.append(f"line {ev.get('_line', '?')}: {msg}")

    # -- helpers

    def known_task(self, ev, field="task", required=True):
        tid = ev.get(field)
        if tid is None:
            if required:
                self.fail(ev, f"missing required field '{field}'")
            return None
        if tid not in self.tasks:
            self.fail(ev, f"references unregistered task '{tid}' "
                          f"(no task_created/baseline)")
            return None
        return tid

    def accumulation_n(self):
        return sum(1 for t, s in self.task_state.items()
                   if s == "machine_complete" and t not in self.accepted)

    def accumulation_level(self):
        n = self.accumulation_n()
        level = "low"
        for floor, name in ACCUMULATION_LEVELS:
            if n >= floor:
                level = name
        return n, level

    def recompute_gate(self):
        n = self.accumulation_n()
        pending_required = [
            t for t, vs in self.verdicts.items()
            if vs and vs[-1].get("recommendation") == "required"
            and t not in self.accepted
        ]
        if pending_required:
            self.hard_gate = (pending_required[-1],
                              "recommendation=required pending human review")
        elif n >= 6:
            self.hard_gate = (None, f"accumulation extra-high (N={n})")
        else:
            self.hard_gate = None

    # -- event application

    def apply(self, ev):
        etype = ev.get("event")
        if etype not in EVENTS:
            self.fail(ev, f"unknown event type '{etype}'")
            return
        for field in ("ts", "actor", "session"):
            if not ev.get(field):
                self.fail(ev, f"missing envelope field '{field}'")
        if ev.get("actor") and ev["actor"] not in ACTORS:
            self.fail(ev, f"unknown actor '{ev['actor']}'")
        if ev.get("party") and ev["party"] not in PARTIES:
            self.fail(ev, f"party must be one of {sorted(PARTIES)}, "
                          f"got '{ev['party']}'")
        if ev.get("ts"):
            if self.last_ts and ev["ts"] < self.last_ts:
                self.fail(ev, f"timestamp {ev['ts']} earlier than previous "
                              f"event ({self.last_ts}); ledger must be "
                              f"append-ordered")
            self.last_ts = ev["ts"]
        getattr(self, f"ev_{etype}")(ev)

    def ev_baseline(self, ev):
        for tid in ev.get("tasks_done", []):
            self.tasks[tid] = {"title": "(pre-ledger, accepted Done)",
                               "mode": None, "spec": None, "contracts": [],
                               "baseline": True}
            self.task_state[tid] = "done"
            self.accepted.add(tid)

    def ev_phase(self, ev):
        if ev.get("action") not in {"setup", "closeout"}:
            self.fail(ev, f"phase action must be setup|closeout, "
                          f"got '{ev.get('action')}'")
        self.phases.append(ev)
        if ev.get("stable_branch"):
            self.stable_branch = ev["stable_branch"]
        if ev.get("action") == "setup":
            self.integration_branch = ev.get("integration_branch")
        elif ev.get("action") == "closeout":
            self.integration_branch = None

    def ev_task_created(self, ev):
        tid = ev.get("task")
        if not tid:
            return self.fail(ev, "task_created missing 'task'")
        if tid in self.tasks:
            return self.fail(ev, f"task '{tid}' already registered")
        if ev.get("mode") not in MODES:
            self.fail(ev, f"task '{tid}': mode must be one of {sorted(MODES)}")
        if ev.get("dep_level") not in DEP_LEVELS:
            self.fail(ev, f"task '{tid}': dep_level must be one of "
                          f"{sorted(DEP_LEVELS)}")
        if ev.get("verification") is not None and \
                not isinstance(ev["verification"], list):
            self.fail(ev, f"task '{tid}': 'verification' must be a list of "
                          f"paths")
        self.tasks[tid] = {"title": ev.get("title", ""),
                           "mode": ev.get("mode"),
                           "spec": ev.get("spec"),
                           "spec_session": ev.get("session"),
                           "contracts": ev.get("contracts", []),
                           "verification": ev.get("verification", []),
                           "class": ev.get("class"),
                           "branch": ev.get("branch"),
                           "baseline": False}
        self.task_state.setdefault(tid, None)

    def _check_authoring(self, ev, tid):
        meta = self.tasks.get(tid) or {}
        if meta.get("mode") == "separate" and                 ev.get("session") == meta.get("spec_session") and                 not meta.get("_authoring_flagged"):
            meta["_authoring_flagged"] = True
            self.fail(ev, f"task '{tid}': separate-mode spec was authored "
                          f"by this implementer session "
                          f"('{ev.get('session')}') — authoring-mode "
                          f"violation (escalate)")

    def ev_task_state(self, ev):
        tid = self.known_task(ev)
        if not tid:
            return
        new = ev.get("state")
        if new not in STATES:
            return self.fail(ev, f"unknown state '{new}'")
        cur = self.task_state.get(tid)
        if new not in LEGAL_TRANSITIONS.get(cur, set()):
            self.fail(ev, f"task '{tid}': illegal transition "
                          f"{cur or 'unregistered'} -> {new}")
        if new == "in_progress":
            # hard gate: no *other* task may start while gate active
            if self.hard_gate and self.hard_gate[0] != tid:
                self.fail(ev, f"task '{tid}': started while hard gate active "
                              f"({self.hard_gate[1]}); requires human_accept "
                              f"first")
            self.task_sessions.setdefault(tid, set()).add(ev.get("session"))
            self._check_authoring(ev, tid)
        if new == "agent_review":
            self.task_sessions.setdefault(tid, set()).add(ev.get("session"))
            self._check_authoring(ev, tid)
            self.last_review_entry[tid] = ev.get("_line", 0)
            if ev.get("self_verdict") and ev["self_verdict"] not in VERDICTS:
                self.fail(ev, f"task '{tid}': self_verdict must be one of "
                              f"{sorted(VERDICTS)}")
            if ev.get("self_confidence") and \
                    ev["self_confidence"] not in CONFIDENCES:
                self.fail(ev, f"task '{tid}': self_confidence must be one "
                              f"of {sorted(CONFIDENCES)}")
        if new == "machine_complete":
            vs = self.verdicts.get(tid, [])
            last = vs[-1] if vs else None
            if not last or last.get("verdict") not in {"accepted",
                                                       "accepted_with_notes"}:
                self.fail(ev, f"task '{tid}': machine_complete without a "
                              f"latest accepted/accepted_with_notes verdict")
            elif last.get("_line", 0) < self.last_review_entry.get(tid, 0):
                self.fail(ev, f"task '{tid}': machine_complete relies on a "
                              f"verdict that predates the latest agent_review "
                              f"— re-review required after reopen")
            if ev.get("session") in self.task_sessions.get(tid, set()):
                self.fail(ev, f"task '{tid}': machine_complete recorded by an "
                              f"implementer session "
                              f"('{ev.get('session')}') — reviewer "
                              f"independence violated")
        if new == "done":
            if tid not in self.accepted:
                self.fail(ev, f"task '{tid}': done without a prior "
                              f"human_accept by approver")
        self.task_state[tid] = new
        self.recompute_gate()

    def ev_verdict(self, ev):
        tid = self.known_task(ev)
        if not tid:
            return
        if self.task_state.get(tid) != "agent_review":
            self.fail(ev, f"task '{tid}': verdict while state is "
                          f"'{self.task_state.get(tid)}' (must be "
                          f"agent_review)")
        if ev.get("verdict") not in VERDICTS:
            self.fail(ev, f"task '{tid}': unknown verdict "
                          f"'{ev.get('verdict')}'")
        if ev.get("recommendation") not in RECOMMENDATIONS:
            self.fail(ev, f"task '{tid}': missing/unknown recommendation "
                          f"'{ev.get('recommendation')}'")
        if ev.get("session") in self.task_sessions.get(tid, set()):
            self.fail(ev, f"task '{tid}': verdict by implementer session "
                          f"('{ev.get('session')}') — reviewer independence "
                          f"violated")
        if not ev.get("review"):
            self.fail(ev, f"task '{tid}': verdict missing 'review' (path to "
                          f"prose review record)")
        for i, item in enumerate(ev.get("deferred", [])):
            if not item.get("route") or not item.get("target"):
                self.fail(ev, f"task '{tid}': deferred item {i} "
                              f"('{item.get('item', '?')}') lacks route "
                              f"and/or target")
        self.verdicts.setdefault(tid, []).append(ev)
        self.recompute_gate()

    def ev_escalation(self, ev):
        if not ev.get("reason"):
            self.fail(ev, "escalation missing 'reason'")
        if ev.get("task"):
            self.known_task(ev)
        self.escalations.append(ev)

    def ev_issue(self, ev):
        iid = ev.get("issue")
        if not iid:
            return self.fail(ev, "issue missing 'issue' id")
        if ev.get("severity") not in SEVERITIES:
            self.fail(ev, f"issue '{iid}': severity must be one of "
                          f"{sorted(SEVERITIES)}")
        self.issues[iid] = {"severity": ev.get("severity"),
                            "summary": ev.get("summary", ""),
                            "status": "open", "route": None, "target": None}

    def ev_issue_route(self, ev):
        iid = ev.get("issue")
        if iid not in self.issues:
            return self.fail(ev, f"issue_route for unregistered issue '{iid}'")
        if ev.get("status") not in ISSUE_STATUSES:
            self.fail(ev, f"issue '{iid}': unknown status "
                          f"'{ev.get('status')}'")
        if ev.get("status") in {"routed", "deferred"} and not \
                (ev.get("route") and ev.get("target")):
            self.fail(ev, f"issue '{iid}': status '{ev.get('status')}' "
                          f"requires route and target")
        self.issues[iid].update({"status": ev.get("status"),
                                 "route": ev.get("route"),
                                 "target": ev.get("target")})

    def ev_decision(self, ev):
        if ev.get("level") not in DECISION_LEVELS:
            self.fail(ev, f"decision '{ev.get('decision')}': unknown level "
                          f"'{ev.get('level')}'")
        if ev.get("level") in {"architecture/contract", "harness/process"} \
                and ev.get("human_gate") is not True:
            self.fail(ev, f"decision '{ev.get('decision')}': level "
                          f"'{ev.get('level')}' requires human_gate: true")
        self.decisions.append(ev)

    def ev_audit(self, ev):
        if ev.get("actor") != "auditor":
            self.fail(ev, "audit actor must be 'auditor'")
        if not ev.get("report"):
            self.fail(ev, "audit missing 'report' (path to prose report)")
        if not isinstance(ev.get("findings"), int) or ev["findings"] < 0:
            self.fail(ev, "audit 'findings' must be a non-negative integer")
        for tid in ev.get("tasks", []):
            if tid not in self.tasks:
                self.fail(ev, f"audit for unregistered task '{tid}'")
                continue
            partial = self.task_sessions.get(tid, set()) | \
                {v.get("session") for v in self.verdicts.get(tid, [])}
            if ev.get("session") in partial:
                self.fail(ev, f"task '{tid}': audit by a session that "
                              f"implemented or reviewed it "
                              f"('{ev.get('session')}') — auditor "
                              f"independence violated")
        self.audits.append(ev)

    def ev_human_accept(self, ev):
        if ev.get("actor") != "approver":
            self.fail(ev, "human_accept actor must be 'approver'")
        for tid in ev.get("tasks", []):
            if tid not in self.tasks:
                self.fail(ev, f"human_accept for unregistered task '{tid}'")
                continue
            if self.task_state.get(tid) not in {"machine_complete",
                                                "human_review"}:
                self.fail(ev, f"task '{tid}': human_accept while state is "
                              f"'{self.task_state.get(tid)}' (must be "
                              f"machine_complete or human_review)")
            self.accepted.add(tid)
        self.recompute_gate()


# ---------------------------------------------------------------- commands

def cmd_validate(args):
    events, findings = load_ledger(args.ledger)
    replay = Replay(events)
    findings += replay.findings
    n, level = replay.accumulation_level()
    if findings:
        print(f"FAIL: {len(findings)} finding(s) in {args.ledger}")
        for f in findings:
            print(f"  - {f}")
        return 1
    print(f"OK: {len(events)} events, {len(replay.tasks)} tasks, "
          f"{len(replay.issues)} issues, N={n} ({level}), "
          f"hard gate={'YES: ' + replay.hard_gate[1] if replay.hard_gate else 'no'}")
    return 0


def task_sort_key(tid):
    parts = []
    for chunk in tid.replace("-", ".").split("."):
        parts.append((0, int(chunk)) if chunk.isdigit() else (1, chunk))
    return parts


def cmd_state(args):
    events, findings = load_ledger(args.ledger)
    replay = Replay(events)
    findings += replay.findings
    n, level = replay.accumulation_level()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    out = []
    out.append("# STATE")
    out.append("")
    out.append(f"Generated by `harness.py state` at {now} from "
               f"`{Path(args.ledger).name}` ({len(events)} events). "
               f"**Do not edit by hand.**")
    out.append("")
    if findings:
        out.append(f"**LEDGER INVALID — {len(findings)} finding(s). "
                   f"Run `harness.py validate`.**")
        out.append("")
    out.append(f"Harness version: {HARNESS_VERSION}")
    last_phase = replay.phases[-1] if replay.phases else None
    if last_phase:
        out.append(f"Phase: {last_phase.get('phase')} "
                   f"({last_phase.get('action')}"
                   f"{', decision ' + last_phase['decision'] if last_phase.get('decision') else ''})")
    out.append(f"Stable branch: {replay.stable_branch or '(unset)'} · "
               f"Integration branch: {replay.integration_branch or '(none — between phases)'}")
    out.append("")
    gate = (f"**YES — {replay.hard_gate[1]}**" if replay.hard_gate else "no")
    pending = [vs[-1].get("recommendation") for t, vs in replay.verdicts.items()
               if vs and t not in replay.accepted]
    rank = {"optional": 0, "advised": 1, "strong": 2, "required": 3}
    highest = max(pending, key=lambda r: rank.get(r, -1)) if pending else "—"
    out.append(f"## Human Review Queue")
    out.append("")
    out.append(f"N={n} ({level}) · highest pending recommendation: {highest} "
               f"· hard gate: {gate}")
    out.append("")

    active = {t: s for t, s in replay.task_state.items()
              if not replay.tasks[t].get("baseline")}
    if active:
        out.append("## Tasks")
        out.append("")
        out.append("| Task | Title | State | Mode | Last verdict | Recommendation |")
        out.append("|------|-------|-------|------|--------------|----------------|")
        for tid in sorted(active, key=task_sort_key):
            t = replay.tasks[tid]
            vs = replay.verdicts.get(tid, [])
            last = vs[-1] if vs else {}
            out.append(f"| {tid} | {t['title']} | {active[tid] or 'registered'} "
                       f"| {t['mode'] or ''} | {last.get('verdict', '—')} "
                       f"| {last.get('recommendation', '—')} |")
        out.append("")

    done_baseline = sorted((t for t, m in replay.tasks.items()
                            if m.get("baseline")), key=task_sort_key)
    if done_baseline:
        out.append(f"Pre-ledger tasks accepted `Done` (baseline): "
                   f"{', '.join(done_baseline)}")
        out.append("")

    open_issues = {i: d for i, d in replay.issues.items()
                   if d["status"] not in {"closed", "fixed"}}
    if open_issues:
        out.append("## Open Issues")
        out.append("")
        out.append("| Issue | Severity | Status | Route | Target |")
        out.append("|-------|----------|--------|-------|--------|")
        for iid in sorted(open_issues):
            d = open_issues[iid]
            out.append(f"| {iid} | {d['severity']} | {d['status']} "
                       f"| {d['route'] or '—'} | {d['target'] or '—'} |")
        out.append("")

    unresolved = [e for e in replay.escalations if not e.get("resolution")]
    resolved_reasons = {e.get("reason") for e in replay.escalations
                        if e.get("resolution")}
    unresolved = [e for e in unresolved
                  if e.get("reason") not in resolved_reasons]
    if unresolved:
        out.append("## Unresolved Escalations")
        out.append("")
        for e in unresolved:
            out.append(f"- {e.get('task', '(no task)')}: {e.get('reason')}")
        out.append("")

    gated = [d for d in replay.decisions if d.get("human_gate")]
    if gated:
        out.append("## Human-Gated Decisions Recorded")
        out.append("")
        for d in gated:
            out.append(f"- `{d.get('decision')}` {d.get('title', '')} "
                       f"({d.get('level')}) — {d.get('path', '')}")
        out.append("")

    text = "\n".join(out) + "\n"
    dest = Path(args.output) if args.output else HERE / "STATE.md"
    dest.write_text(text)
    print(f"Wrote {dest} ({len(text.splitlines())} lines)")
    return 0 if not findings else 1


def cmd_brief(args):
    events, findings = load_ledger(args.ledger)
    replay = Replay(events)
    findings += replay.findings
    tid = args.task
    role = args.role

    out = []
    out.append(f"# Session Brief — task {tid} — role: {role}")
    out.append("")
    out.append(f"Harness version: {HARNESS_VERSION}. Read "
               f"`harness/HARNESS.md` for invariants, gates, and "
               f"escalation signals. Mechanical rules are enforced by "
               f"`harness.py validate` — run it before and after your "
               f"handoff.")
    out.append("")
    if findings:
        out.append(f"**WARNING: ledger has {len(findings)} validation "
                   f"finding(s) — resolve before starting.**")
        out.append("")
    out.append(ROLE_RULES.get(role, f"(no canned rules for role '{role}')"))
    out.append("")

    last_phase = replay.phases[-1] if replay.phases else None
    out.append("## Where you are")
    out.append("")
    out.append(f"- Phase: {last_phase.get('phase') if last_phase else '?'} "
               f"({last_phase.get('action') if last_phase else '?'})")
    out.append(f"- Stable branch: {replay.stable_branch or '(unset)'} — "
               f"never commit here")
    out.append(f"- Integration branch: {replay.integration_branch or '(none)'}")
    if replay.hard_gate:
        out.append(f"- **HARD GATE ACTIVE: {replay.hard_gate[1]} — no new "
                   f"task may start until human_accept**")
    out.append("")

    if role == "auditor" and tid == "queue":
        pending = sorted((t for t, s in replay.task_state.items()
                          if s in {"machine_complete", "human_review"}
                          and t not in replay.accepted), key=task_sort_key)
        out.append(f"## Audit queue ({len(pending)} task(s) pending human "
                   f"acceptance)")
        out.append("")
        if not pending:
            out.append("Queue is empty — nothing awaiting the human gate.")
        for t in pending:
            meta = replay.tasks[t]
            vs = replay.verdicts.get(t, [])
            last = vs[-1] if vs else {}
            impl = sorted(replay.task_sessions.get(t, set()))
            rev = sorted({v.get("session") for v in vs})
            out.append(f"### {t}: {meta['title']}")
            out.append("")
            out.append(f"- Spec: {meta.get('spec')} · Mode: {meta['mode']} "
                       f"· Branch: {meta.get('branch') or 'task/' + t}")
            out.append(f"- Verdict: {last.get('verdict', '—')} "
                       f"({last.get('recommendation', '—')}) — review: "
                       f"{last.get('review', '—')}")
            out.append(f"- Contracts checked per reviewer: "
                       f"{', '.join(last.get('contracts_checked', [])) or '(none listed)'}")
            for d in last.get("deferred", []):
                out.append(f"- Deferred: {d.get('item')} -> "
                           f"{d.get('route')} / {d.get('target')}")
            out.append(f"- Sessions — implementer: {', '.join(impl) or '?'} "
                       f"· reviewer: {', '.join(rev) or '?'} (yours must "
                       f"differ from both)")
            out.append("")
        unresolved = [e for e in replay.escalations if not e.get("resolution")]
        if unresolved:
            out.append("## Unresolved escalations (in scope)")
            out.append("")
            for e in unresolved:
                out.append(f"- {e.get('task', '(no task)')}: {e.get('reason')}")
            out.append("")
        out.append("Full history: query the ledger directly, e.g. "
                   "`SELECT * FROM read_json_auto('ledger.jsonl')` in DuckDB. "
                   "Report template: harness/templates/"
                   "audit_report.template.md.")
        print("\n".join(out))
        return 0

    meta = replay.tasks.get(tid)
    if not meta:
        out.append(f"**Task `{tid}` is not registered in the ledger.** "
                   f"A planner must append `task_created` first.")
    else:
        out.append(f"## Task {tid}: {meta['title']}")
        out.append("")
        out.append(f"- State: {replay.task_state.get(tid) or 'registered'}")
        out.append(f"- Authoring mode: {meta['mode']} · Branch: "
                   f"{meta.get('branch') or 'task/' + tid}")
        vs = replay.verdicts.get(tid, [])
        if vs:
            out.append(f"- Last verdict: {vs[-1].get('verdict')} "
                       f"({vs[-1].get('recommendation')}) — "
                       f"{vs[-1].get('review')}")
        out.append("")
        if meta.get("contracts"):
            out.append("### Contracts to check")
            out.append("")
            for c in meta["contracts"]:
                out.append(f"- {c}")
            out.append("")
        if meta.get("verification"):
            out.append("### Verification contracts (named criteria)")
            out.append("")
            for v in meta["verification"]:
                out.append(f"- {v}")
            out.append("")
        routed = {i: d for i, d in replay.issues.items()
                  if d.get("target") == tid and d["status"] in
                  {"routed", "open", "deferred"}}
        if routed:
            out.append("### Issues routed to this task")
            out.append("")
            for iid, d in sorted(routed.items()):
                out.append(f"- {iid} ({d['severity']}, {d['status']}): "
                           f"{d['summary']}")
            out.append("")
        spec = meta.get("spec")
        if spec:
            spec_path = REPO / spec
            out.append(f"### Task spec ({spec})")
            out.append("")
            if spec_path.exists():
                out.append(spec_path.read_text().rstrip())
            else:
                out.append(f"(spec file not found at {spec_path})")
            out.append("")

    print("\n".join(out))
    return 0


def cmd_log(args):
    """Append one well-formed event, refusing anything the validator rejects."""
    ledger_path = Path(args.ledger)
    events, findings = load_ledger(ledger_path)
    replay = Replay(events)
    if findings or replay.findings:
        print(f"refusing to append: ledger already invalid "
              f"({len(findings) + len(replay.findings)} finding(s)) — run "
              f"`harness.py validate` first")
        return 1

    ev = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
          "event": {"issue": "issue", "route": "issue_route",
                    "state": "task_state"}[args.kind],
          "actor": args.actor, "session": args.session}
    if getattr(args, "party", None):
        ev["party"] = args.party

    if args.kind == "issue":
        if args.id:
            iid = args.id
        else:
            nums = [int(i.rsplit("-", 1)[-1]) for i in replay.issues
                    if i.rsplit("-", 1)[-1].isdigit()]
            iid = f"{ISSUE_PREFIX}-{max(nums, default=100) + 1:04d}"
        ev.update(issue=iid, severity=args.severity, summary=args.summary)
        if args.category:
            ev["category"] = args.category
    elif args.kind == "route":
        ev.update(issue=args.issue, status=args.status)
        for k in ("route", "target", "note"):
            if getattr(args, k, None):
                ev[k] = getattr(args, k)
    elif args.kind == "state":
        ev.update(task=args.task, state=args.state)
        for k in ("note", "commit", "self_verdict", "self_confidence"):
            if getattr(args, k, None):
                ev[k] = getattr(args, k)

    probe = dict(ev)
    probe["_line"] = len(events) + 1
    after = Replay(events + [probe])
    if after.findings:
        print("refusing to append — event would be invalid:")
        for f in after.findings:
            print(f"  - {f}")
        return 1

    with open(ledger_path, "a") as fh:
        fh.write(json.dumps(ev) + "\n")
    label = ev.get("issue") or f"{ev.get('task')} -> {ev.get('state')}"
    print(f"appended {ev['event']}: {label}")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    default_ledger = str(HERE / "ledger.jsonl")

    v = sub.add_parser("validate", help="schema + rule check the ledger")
    v.add_argument("ledger", nargs="?", default=default_ledger)

    s = sub.add_parser("state", help="generate STATE.md from the ledger")
    s.add_argument("ledger", nargs="?", default=default_ledger)
    s.add_argument("-o", "--output", help="output path (default harness/STATE.md)")

    b = sub.add_parser("brief", help="emit a session context pack for a task")
    b.add_argument("task", help="task id, or 'queue' with --role auditor")
    b.add_argument("--role", required=True,
                   choices=["implementer", "reviewer", "planner", "approver",
                            "auditor"])
    b.add_argument("-l", "--ledger", default=default_ledger)

    lg = sub.add_parser("log", help="append a well-formed event "
                                    "(issue | route | state)")
    lgs = lg.add_subparsers(dest="kind", required=True)
    today = datetime.now(timezone.utc).strftime("%m%d")

    def _common(sp, default_actor, default_session, default_party):
        sp.add_argument("--ledger", default=default_ledger)
        sp.add_argument("--actor", default=default_actor,
                        choices=sorted(ACTORS),
                        required=default_actor is None)
        sp.add_argument("--session", default=default_session,
                        required=default_session is None)
        sp.add_argument("--party", default=default_party,
                        choices=sorted(PARTIES))

    li = lgs.add_parser("issue", help="capture an observed issue")
    li.add_argument("summary")
    li.add_argument("--severity", required=True, choices=sorted(SEVERITIES))
    li.add_argument("--category")
    li.add_argument("--id", help="override auto-assigned ISSUE id")
    _common(li, "approver", f"cli-manual-{today}", "human")

    lr = lgs.add_parser("route", help="triage/route an issue")
    lr.add_argument("issue")
    lr.add_argument("status", choices=sorted(ISSUE_STATUSES))
    lr.add_argument("--route")
    lr.add_argument("--target")
    lr.add_argument("--note")
    _common(lr, "approver", f"cli-manual-{today}", "human")

    lt = lgs.add_parser("state", help="record a task state transition")
    lt.add_argument("task")
    lt.add_argument("state", choices=sorted(STATES))
    lt.add_argument("--note")
    lt.add_argument("--commit")
    lt.add_argument("--self-verdict", dest="self_verdict",
                    choices=sorted(VERDICTS))
    lt.add_argument("--self-confidence", dest="self_confidence",
                    choices=sorted(CONFIDENCES))
    _common(lt, None, None, None)

    args = p.parse_args()
    return {"validate": cmd_validate, "state": cmd_state,
            "brief": cmd_brief, "log": cmd_log}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
