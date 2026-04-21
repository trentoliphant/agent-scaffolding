# Minimal Adoption

This guide shows the smallest useful version of the standard for a real
project.

## Goal

The goal of a minimal adoption is not completeness.

The goal is to make a domain harness more legible, inspectable, and improvable
without adding unnecessary process.

Use
[baseline-implementation.md](baseline-implementation.md)
alongside this guide when you want to stay clear about which recommendations
are baseline defaults and which parts belong to the standard itself.

## What A Minimal Adoption Must Clarify

Even the smallest useful adoption should make these things explicit:

- what the harness is trying to achieve
- what roles exist
- which roles are filled by humans, machines, or mixed loops
- what a task cycle looks like
- what must be verified
- what trace is preserved from each task cycle
- where durable harness decisions are recorded

## Recommended Minimal Structure

In your own project, start with something like:

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

Optional when work spans multiple sessions:

```text
state/
  current.md
```

This gives you:

- a repo-specific operating contract
- a small but explicit local standard definition
- a baseline implementation shape that is easy to adapt
- a place to define trace and verification expectations
- a place for durable rationale
- an optional continuity layer for multi-session work

## What To Put In Those Files

Use `AGENTS.md` for:

- how agents should work in the project
- local editing and review expectations
- escalation expectations

Use `docs/scaffolding/00-overview.md` for:

- what the local harness is trying to achieve
- the core modules you are actually using
- the intended scope of the harness

Use `docs/scaffolding/20-components-and-boundaries.md` for:

- the local definitions of roles, tasks, verification, and orchestration
- the boundary between standard-core concepts and local extensions

Use `docs/scaffolding/50-traces-verification-and-evolution.md` for:

- the minimum trace expected from a task cycle
- the verification contract used locally
- the improvement loop used to learn from real usage

Use `history/decisions/` for:

- naming choices
- structural tradeoffs
- changes in interpretation
- durable lessons that should outlive the current task

Use `state/current.md` when needed for:

- the active objective
- open questions
- active tasks or blocking issues
- candidate harness changes not yet adopted

## Suggested First Workflow

A simple first workflow is:

1. Define a task.
2. Assign or imply the role responsible for doing it.
3. Execute the task.
4. Apply an explicit verification contract.
5. Record a lightweight trace of what happened.
6. Record any durable structural lesson as a decision.

That loop is often enough to prove whether the harness is helping.

## When To Add More

Add more structure only when the project needs it.

Common triggers include:

- more than one recurring role
- repeated confusion about who may decide what
- repeated confusion about what verification is required
- work spanning multiple sessions
- recurring failures that reveal missing trace fields
- domain-specific escalation or compliance needs
- different expertise tiers needing different autonomy levels

## What To Add Next

The next useful additions are often:

- a more explicit orchestration document
- autonomy or expertise profiles such as junior, regular, and senior
- domain-specific verification modules
- integration guidance for a specific execution system
- richer examples for common task patterns

If older starter-kit-derived patterns are relevant to your project, use
[starter-kit-adoption.md](starter-kit-adoption.md) as reference or migration
material rather than as the default baseline.
