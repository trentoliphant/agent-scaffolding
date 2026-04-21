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
docs/
  scaffolding/
    00-overview.md
    20-components-and-boundaries.md
    50-traces-verification-and-evolution.md
history/
  decisions/
```

## Example Definitions

The local harness might define:

- a builder role that decides goals and accepts work
- an implementation role that performs changes
- a verification contract for correctness
- a verification contract for boundary compliance
- a lightweight trace requirement for each completed task cycle

The orchestration can stay simple:

1. A task is defined.
2. The implementation role performs it.
3. Verification is applied.
4. A lightweight trace is recorded.
5. Any durable lesson is recorded as a decision.

## Why This Example Matters

This example is useful because it proves that a harness can stay small and
still be real.

It does not require:

- many roles
- complex orchestration
- automation infrastructure
- a large document system

It only requires explicit structure where the work benefits from it most.
