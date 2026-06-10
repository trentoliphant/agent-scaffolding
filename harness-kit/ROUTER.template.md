# Agent Entry Point

<!-- Copy this file to your repo root TWICE: as CLAUDE.md and as AGENTS.md.
     Replace <PROJECT> and delete these comments. -->

This repo runs a versioned AI process harness. **Active version: kit-0.1**
(`harness/`, adopted by decision `P-0001`).

Before any harness-governed work:

1. Get your task id and role from the operator (implementer, reviewer,
   planner, auditor, or approver-facilitator). Do not pick your own task.
2. Run `python3 harness/harness.py brief <task> --role <role>` — the output
   is your working context: role rules, branch targets, gate status,
   contracts to check, routed issues, and the task spec.
3. Read `harness/HARNESS.md` for invariants, gates, and escalation
   signals. Stop and escalate on any red-line signal.
4. Record every process state change as one appended event in
   `harness/ledger.jsonl` (schema: `harness/SCHEMA.md`) — prefer
   `harness/harness.py log ...` which refuses invalid events. Pick a unique
   session id `<tool>-<role>-<date>-<letter>` and use it on every event you
   append — it enforces reviewer independence.
5. Run `python3 harness/harness.py validate` before starting and before
   your handoff; finish with `python3 harness/harness.py state`.

Product truth lives in <PROJECT>'s sources named in
`harness/HARNESS.md` §Source Authority — the harness governs process only.
