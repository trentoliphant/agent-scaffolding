# Minimal Adoption

This guide shows the smallest useful version of the scaffold for a real project.

## Goal

The goal of a minimal adoption is not completeness. The goal is to make agent-assisted work more legible and repeatable without adding unnecessary process.

## Recommended Minimal Structure

In your own project, start with something like:

```text
AGENTS.md
docs/
  scaffolding/
    00-overview.md
    20-components-and-boundaries.md
history/
  decisions/
```

This gives you:

- a repo-specific operating contract
- a small but explicit system definition
- a place for durable rationale

## What To Put In Those Files

Use `AGENTS.md` for:

- how agents should work in the project
- local editing expectations
- review expectations

Use `docs/scaffolding/00-overview.md` for:

- what the local system is trying to achieve
- the core components you are using
- the intended scope of the scaffold

Use `docs/scaffolding/20-components-and-boundaries.md` for:

- the local definitions of roles, tasks, review, and orchestration
- any project-specific distinctions that need to remain explicit

Use `history/decisions/` for:

- naming choices
- structural tradeoffs
- changes in interpretation

## Suggested First Workflow

A simple first workflow is:

1. Define a task
2. Assign or imply the role responsible for doing it
3. Apply at least one review type before accepting the result
4. Record any durable structural lesson as a decision

That loop is often enough to prove whether the scaffold is helping.

## When To Add More

Add more structure only when the project needs it.

Common triggers include:

- more than one recurring role
- repeated confusion about what review is required
- work spanning multiple sessions
- handoffs between planning, execution, and review
- recurring design debates that need durable resolution
