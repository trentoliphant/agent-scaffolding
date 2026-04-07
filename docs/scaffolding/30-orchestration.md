# Orchestration

Orchestration is the part of the scaffold that coordinates work across roles, tasks, and review.

It defines how the system behaves, not just what parts the system contains.

## What Orchestration Is Responsible For

Orchestration is responsible for:

- routing work to the right role
- sequencing tasks
- deciding when and how review is applied
- managing escalation and handoffs
- keeping session state aligned with active work

## What Orchestration Should Not Absorb

Orchestration should not replace the other components.

It should not be used as a vague catch-all for:

- the definition of roles
- the content of tasks
- the criteria of review types
- the full historical rationale of the system

## Minimal Orchestration

A minimal scaffold can use very lightweight orchestration.

For example:

- a builder defines a task
- an implementation role performs it
- a review type is applied before completion
- important outcomes are promoted into history or decisions

That is still orchestration, even if it is simple.

## Growing Orchestration

As a system becomes more complex, orchestration may need to define:

- routing rules
- escalation thresholds
- handoff criteria
- approval points
- rollback or revision loops

These additions should be introduced only when they make the system clearer or safer to operate.

## Orchestration Questions

If orchestration is underspecified, ask:

- Who decides which role acts next?
- What must happen before a task can begin?
- What review is required before work is accepted?
- When does uncertainty trigger escalation?
- What information must be preserved for later sessions?

Answers to those questions often reveal where the scaffold needs more explicit coordination logic.
