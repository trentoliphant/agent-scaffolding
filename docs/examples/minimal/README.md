# Minimal Example

This example shows a deliberately small domain harness for a single-project
workflow.

It is intentionally modest. The point is to demonstrate a usable starting
shape, not a complete system.

## Example Context

Imagine a builder using agents to evolve a small internal tool.

The builder wants:

- clearer task ownership
- explicit verification before acceptance
- a lightweight trace of what happened
- a durable record of important structural choices

## Example Structure

```text
AGENTS.md
SYSTEM_MODEL.md
PLAN.md
PROGRESS.md
history/
  decisions/
```

This structure expresses the standard locally without requiring the project to
copy the repository's full `docs/scaffolding/` definition.

## Example Definitions

The local harness might define:

- a builder role that decides goals and accepts work
- an implementation role that performs changes
- a verification contract for correctness
- a verification contract for boundary compliance
- a lightweight trace requirement for each completed task cycle

The files map to the standard this way:

- `AGENTS.md` defines local agent behavior, escalation expectations, and
  repository-specific working rules
- `SYSTEM_MODEL.md` defines the local harness purpose, role boundaries,
  verification expectations, and trace expectations
- `PLAN.md` defines the current task sequence or phases
- `PROGRESS.md` tracks task status, actor, verification state, and trace state
- `history/decisions/` preserves durable rationale when the harness changes

The orchestration can stay simple:

1. A task is defined.
2. The implementation role performs it.
3. Verification is applied.
4. A lightweight trace is recorded.
5. Any durable lesson is recorded as a decision.

An individual task trace can stay small:

```text
Task: Update the import path in the reporting command.
Responsible role: implementation
Acting party: machine agent
Outcome: command now imports the shared formatter
Evidence: targeted test passed
Verification result: accepted
Next action: mark task complete in progress
```

## Why This Example Matters

This example is useful because it proves that a harness can stay small and
still be real.

It does not require:

- many roles
- complex orchestration
- automation infrastructure
- a large document system

It only requires explicit structure where the work benefits from it most.

## What To Add Next

If this minimal shape is working but the project now needs runtime-specific
mapping, read
[../../guide/execution-system-integration.md](../../guide/execution-system-integration.md).

If the project needs domain-specific roles, verification modules, or overlays,
read
[../../guide/domain-implementation-extensions.md](../../guide/domain-implementation-extensions.md).
