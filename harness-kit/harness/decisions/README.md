# Decisions (harness v2)

Prose decision records, split by stream:

- `product/` — architecture, contracts, product behavior. The legible record
  of what the *system* is.
- `process/` — harness, authority, gates, workflow. The deliverable of the
  process-discovery half of this project.

Every record here is announced by a `decision` event in the ledger carrying
id, level, authority, human-gate flag, and this file's path. The prose holds
context, rationale, and escalation triggers — judgment, not state.

New decisions use `D-####` (product) and `P-####` (process).
