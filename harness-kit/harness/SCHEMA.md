# Ledger Event Schema (harness v2.0-prototype)

The ledger (`ledger.jsonl`) is the single source of truth for process **facts**.
One JSON object per line, append-only. Judgment stays in prose (review records,
decision records) and is linked from events by path. Never edit or delete a
line; correct a mistake by appending a corrective event with a `supersedes`
note.

Query it directly with DuckDB:

```sql
SELECT * FROM read_json_auto('harness/ledger.jsonl') WHERE event = 'verdict';
```

## Envelope (every event)

| Field     | Type   | Rule |
|-----------|--------|------|
| `ts`      | string | ISO 8601 UTC timestamp |
| `event`   | string | One of the 10 types below |
| `actor`   | string | `planner` \| `implementer` \| `reviewer` \| `approver` \| `facilitator` \| `maintainer` \| `auditor` \| `system` |
| `session` | string | Free-form session/party identifier (used to enforce reviewer independence) |

Type-specific fields are flat, top-level keys (easier to query than nesting).

Optional envelope field (sensor): `party`
(`human` | `machine` | `mixed`) — who actually acted, as distinct from the
responsible role in `actor`. Defaults to `machine` for agent sessions.

## Event Types

### 1. `baseline`
Adopts the ledger at a point in time; registers prior history without
fabricating per-event detail.
Fields: `harness_version`, `note`, `tasks_done` (array of task ids accepted as
`Done` before the ledger existed; they are registered and terminal).

### 2. `phase`
Fields: `phase` (e.g. `"2"`), `action` (`setup` | `closeout`), `decision`
(decision id, optional), `stable_branch`, `integration_branch` (setup only),
`note`.

### 3. `task_created`
Fields: `task`, `title`, `spec` (repo path), `mode` (`separate` |
`same-session-ok`), `dep_level` (`machine-level` | `human-level`), `contracts`
(array of repo paths), `branch` (task branch name, optional).
Sensor fields (optional): `class` (phase-consistent task class,
e.g. `contract-shaping` | `boundary` | `routine-fenced`), `verification`
(array of paths to named verification-contract files).

### 4. `task_state`
Fields: `task`, `state` (`not_started` | `in_progress` | `agent_review` |
`machine_complete` | `human_review` | `done` | `blocked`), `note` (optional),
`commit` (optional git sha).
Sensor fields (optional): on `agent_review`, the implementer may
add `self_verdict` (predicted reviewer verdict, same enum as verdicts) and
`self_confidence` (`low` | `medium` | `high`). On `in_progress`, load-bearing
assumptions go in `note` with the convention `assumes: ...`. Sensors never
gate: missing sensor fields are valid.

### 5. `verdict`
Recorded by the reviewer when a task is in `agent_review`.
Fields: `task`, `verdict` (`accepted` | `accepted_with_notes` | `revise` |
`escalate` | `blocked`), `review` (repo path to the prose review record),
`recommendation` (`optional` | `advised` | `strong` | `required` — Human
Review Signal), `contracts_checked` (array), `deferred` (array of
`{item, route, target}` — every entry needs both `route` and `target`).

### 6. `escalation`
Fields: `task` (optional), `reason`, `resolution` (optional; append a second
`escalation` event with the same `reason` and a `resolution` when resolved),
`decision` (optional decision id).

### 7. `issue`
Fields: `issue` (e.g. `ISSUE-0051`), `severity` (`blocking` | `major` |
`minor`), `category` (optional), `summary`.

### 8. `issue_route`
Fields: `issue`, `status` (`open` | `routed` | `fixed` | `closed` |
`deferred`), `route` (e.g. `task-spec`, `new-task`, `decision`, `deferral`),
`target` (task id, phase, or gate), `note` (optional).

### 9. `decision`
Fields: `decision` (id), `title`, `level` (`task-local` | `cross-task` |
`architecture/contract` | `harness/process`), `authority` (`spec-author` |
`implementer` | `reviewer` | `approver`), `human_gate` (bool), `path` (repo
path to the prose record). Product decisions live under `decisions/product/`,
process decisions under `decisions/process/`.

### 10. `human_accept`
Fields: `tasks` (array of task ids), `gate` (optional, e.g. `poc-3`,
`phase-2-closeout`), `note`. Actor must be `approver`. Resets the
accumulation counter for the accepted tasks.

### 11. `audit`
Process audit run at the human gate (role:
`roles/AUDITOR.md`). Fields: `tasks` (array audited), `findings`
(non-negative integer — count of attention items in the report), `report`
(repo path to the prose report), `note` (optional). Actor must be
`auditor`.

## Derived, never stored

These are computed by `harness.py` and must not be hand-written anywhere:

- Current state of any task (last `task_state`).
- Accumulation `N` = tasks at `machine_complete` not yet in a `human_accept`.
- Accumulation level: `low` 0–1, `medium` 2–3, `high` 4–5, `extra-high` 6+.
- Hard gate = latest pending `recommendation == required` OR `N >= 6`.
- `STATE.md`, the review queue, and any dashboard.

## Mechanical rules enforced by `harness.py validate`

1. Envelope completeness and enum validity on every event.
2. Events may only reference tasks registered by `task_created` or `baseline`.
3. Task state transitions follow the legal state machine.
4. `verdict` only while the task is in `agent_review`.
5. Reviewer independence: the `session` recording a `verdict` (and the
   `machine_complete` transition) must differ from the session that delivered
   the implementation (`in_progress`/`agent_review` events).
6. `machine_complete` requires the latest verdict to be `accepted` or
   `accepted_with_notes`, recorded **after** the most recent `agent_review`
   transition — a reopened task needs a fresh re-review verdict; the
   pre-reopen verdict is stale.
7. `done` requires a prior (or same-event-batch) `human_accept` by an
   `approver` listing the task.
8. Every `deferred` item on a verdict has a non-empty `route` and `target`.
9. Hard gate: while the gate is active, no *other* task may enter
   `in_progress` until a `human_accept` clears it.
10. `decision` events with `level` of `architecture/contract` or
    `harness/process` must have `human_gate: true`.
11. `audit` events: actor `auditor`, non-empty `report`, integer
    `findings`, registered tasks, and a session distinct from every
    implementer and reviewer session of each audited task.
12. Sensor enums (`party`, `self_verdict`, `self_confidence`,
    `verification` list-shape) are validated when present, never required.
13. A `separate`-mode task's spec-author session (the `task_created`
    session) must not implement that task — spec authorship is planner
    authority; `same-session-ok` is the only mode that permits one session
    to wear both hats.
