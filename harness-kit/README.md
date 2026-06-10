# Harness Kit (kit-0.1)

Status: **Incubating** (per this repository's status taxonomy). A complete,
executable baseline implementation of the scaffolding standard, extracted
from the Intelligence Hub project after 28 governed tasks across three
phases. This is the standard's concepts running on an enforced substrate:

| Layer | Substrate | Trust mechanism |
|-------|-----------|-----------------|
| Meaning — invariants, authority, gates | `harness/HARNESS.md` (text) | human review |
| Facts — state, history | `harness/ledger.jsonl` (append-only JSONL) | git history + hook |
| Mechanical rules | `harness/harness.py validate` (script) | deterministic |

`STATE.md` is generated, never authored. Review records are judgment-only.
Session orientation costs one CLI call, not a reading list.

## What's in the box

```text
ROUTER.template.md      → copy to target repo root as CLAUDE.md + AGENTS.md
harness/
  HARNESS.md            meaning layer; FILL IN sections = your Phase 0
  SCHEMA.md             11 event types, mechanical rules, sensor fields
  harness.py            validate | state | brief | log  (stdlib only)
  hooks/pre-commit      blocks edits to ledger history + invalid ledgers
  roles/AUDITOR.md      process auditor for the human gate
  templates/            judgment-only review + audit report templates
  decisions/            product/ (D-####) and process/ (P-####) streams
  eval/queries.sql      optional DuckDB analysis over the ledger
  examples/             demo lifecycle + four invalid ledgers the
                        validator must catch (selftest fixtures)
```

## Adoption (≈30 minutes, most of it thinking)

1. **Copy** `harness/` into your repo root; copy `ROUTER.template.md` to
   the repo root twice, as `CLAUDE.md` and `AGENTS.md`; fill placeholders.
2. **Answer the questionnaire** — the FILL IN sections in
   `harness/HARNESS.md` (source authority, invariants, escalation red
   lines, PoC gates). This is human work; do not delegate it. The
   categories encode where AI-driven development erodes systems.
3. **Initialize the ledger** — one baseline line (adjust and append):

   ```json
   {"ts": "2026-01-01T00:00:00Z", "event": "baseline", "actor": "system", "session": "bootstrap", "harness_version": "kit-0.1", "note": "Ledger adopted at project start.", "tasks_done": []}
   ```

   Then `python3 harness/harness.py validate` must say OK.
4. **Install the hook:** `chmod +x harness/hooks/pre-commit && git config
   core.hooksPath harness/hooks` — then commit everything. The commit
   timestamps are what make the ledger trustworthy. (The chmod matters:
   copy methods that strip the executable bit make git *silently ignore*
   the hook.)
5. **Record adoption as `P-0001`** (a `decision` event with
   `human_gate: true` + a short prose record in `decisions/process/`), run
   a planning session, append the `phase` setup event, and start the first
   task with `harness.py brief <task> --role implementer`.

Verify the substrate anytime:

```bash
python3 harness/harness.py validate harness/examples/demo-ledger.jsonl  # OK
python3 harness/harness.py validate harness/examples/bad-ledger.jsonl   # 9 caught
python3 harness/harness.py validate harness/examples/bad-reopen.jsonl   # 1 caught
python3 harness/harness.py validate harness/examples/bad-authoring.jsonl # 1 caught
```

## What to customize (and what not to)

Customize: the FILL IN sections, `ISSUE_PREFIX` in `harness.py`,
accumulation thresholds (before data collection, never after), and the
demo examples (delete or keep as fixtures). Do **not** customize authority
or gates by editing prose alone — those are `harness/process` decisions and
belong in the ledger with `human_gate: true`.

## Practices that earned their place (from the origin project)

- **Fresh sessions per role.** Orientation is cheap now (`brief`); session
  reuse trades nothing for accumulated anchoring. Reviewer reuse in
  particular died with the reading tax that justified it.
- **Capture issues the moment you see them** (`harness.py log issue`).
  Capture and triage are decoupled by design.
- **Iterate freely inside `in_progress`** — no events during back-and-forth
  with an implementer. Record `party: mixed` when a human co-drives, so
  calibration data stays honest.
- **Planning chats stay freeform**; only the closing 30–60 line summary is
  committed (criteria, options, decisions, rejected alternatives,
  overridden warnings, 3–5 bets with falsifiers). Score the bets at the
  next phase break. For hard-to-reverse decisions, use two independent
  model families and treat their *divergence* as the uncertainty map —
  record overridden warnings with reasons.
- **The auditor directs attention; it never approves.** A gate a human
  cannot cheaply verify at is trust theater.

## Provenance

Extracted 2026-06-10 from `intelhub` `harness/v2` (decisions P-0001–P-0003
there). The origin project's process-validation experiment (C1–C6,
pre-registered thresholds) continues in that repo; findings that prove
portable will be folded back here. This kit is itself the C5 experiment:
if adopting it into a new project requires editing `harness.py` or the
schema, that edit is a finding — report it.
