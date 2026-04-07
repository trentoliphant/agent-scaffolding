# Minimal Example

This example shows a small scaffold for a single-project workflow.

It is intentionally modest. The point is to demonstrate a usable starting shape, not a complete system.

## Example Context

Imagine a builder using agents to evolve a small internal tool.

The builder wants:

- clearer task ownership
- a repeatable review step
- durable record of important structural choices

## Example Structure

```text
AGENTS.md
docs/
  scaffolding/
    00-overview.md
    20-components-and-boundaries.md
history/
  decisions/
```

## Example Definitions

The local scaffold might define:

- a builder role that decides goals and accepts work
- an implementation role that performs changes
- a review type for correctness
- a review type for boundary compliance

The orchestration can stay simple:

1. A task is defined
2. The implementation role performs it
3. Correctness and boundary review are applied
4. Any durable lesson is recorded as a decision

## Why This Example Matters

This example is useful because it proves that a scaffold can be small and still be real.

It does not require:

- many roles
- complex orchestration
- automation infrastructure

It only requires explicit structure where the work benefits from it most.
