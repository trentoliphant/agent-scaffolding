# Software Project Example

This example is a promoted domain-extension pattern for coding-focused scaling.

This example shows how the baseline can scale for a software project without
turning software work into the definition of the standard.

It is a coding-focused domain implementation example.

## Example Context

Imagine a product repository where agents help with feature work,
documentation, verification, and release preparation across multiple sessions.

The team wants:

- clearer handoffs between planning, implementation, verification, and release
- visible quality gates
- lightweight traces for feature work and fixes
- durable rationale for structural decisions
- coding standards where software-specific quality matters

## Example Structure

Start from the same baseline shape as the minimal adoption path:

```text
AGENTS.md
SYSTEM_MODEL.md
PLAN.md
PROGRESS.md
history/
  decisions/
state/
  current.md
```

Then add software-specific implementation assets only when they help:

```text
CODING_STANDARDS.md
WORKFLOW_STANDARDS.md
tasks/
  task_X.Y_spec.md
  task_X.Y_verification.md
reviews/
  periodic_harness_review.md
```

The first group expresses the local harness.
The second group is a software-project extension of that harness.

## Example Roles

The local harness might define roles such as:

- product owner: decides goals, acceptance tradeoffs, and release priorities
- planner: turns goals into sequenced tasks
- implementer: performs code or documentation changes
- verifier: applies verification contracts before work is accepted
- release owner: decides whether verified work is ready to ship

These roles may be filled by humans, machine agents, or mixed loops.
The role definition should stay separate from the actor that fills it.

## Example Verification Contracts

A software project may use verification contracts such as:

- correctness: the change satisfies the stated behavior and handles relevant
  edge cases
- architecture alignment: the change respects component boundaries and system
  invariants
- documentation completeness: relevant user, contributor, or system
  documentation remains accurate
- regression awareness: existing supported behavior still works or known risk
  is explicitly accepted
- release readiness: remaining caveats are acceptable for the intended release

These are verification contracts, not just review labels.
Each contract should define the criteria, verifier role or function, verdicts,
and next action for each verdict.

## Example Task Cycle

A feature might move through the harness like this:

1. `PLAN.md` identifies the task and its intended sequence.
2. A task spec defines scope, role assignment, verification requirements, and
   trace expectations.
3. The implementer performs the change.
4. Required checks or evidence are collected.
5. The verifier applies the relevant verification contracts.
6. `PROGRESS.md` records status, actor, verification state, and trace state.
7. Durable structural tradeoffs are recorded in `history/decisions/`.
8. A periodic harness review looks for repeated friction or improvement
   opportunities.

## Example Trace

A lightweight task trace can stay readable:

```text
Task: Add CSV export to the reporting command.
Responsible role: implementer
Acting party: machine agent
Outcome: export command writes selected report rows as CSV
Evidence or observations: unit tests passed; manual sample output inspected
Verification result: accepted_with_notes
Next action: document delimiter behavior before release
```

## Why This Example Matters

This example shows that the scaffold can support software delivery without
becoming a software-only standard.

The scaling move is not to copy every possible file.
The scaling move is to add explicit task, verification, trace, workflow, and
coding standards only where the project benefits from them.

For the general extension rules behind those additions, use
[../../guide/domain-implementation-extensions.md](../../guide/domain-implementation-extensions.md)
for domain implementation structure and
[../../guide/execution-system-integration.md](../../guide/execution-system-integration.md)
for runtime-specific mapping.
