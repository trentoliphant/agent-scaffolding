# Software Project Example

This example shows how the scaffold can be applied to a more involved software project.

## Example Context

Imagine a product repository where agents help with feature work, documentation, and review across multiple sessions.

The team wants:

- clearer handoffs between planning, implementation, and review
- visible quality gates
- durable rationale for structural decisions

## Example Structure

```text
AGENTS.md
docs/
  scaffolding/
    00-overview.md
    10-principles.md
    20-components-and-boundaries.md
    30-orchestration.md
  guide/
    delivery-workflow.md
history/
  decisions/
state/
  current.md
```

## Example Roles

The local system might define roles such as:

- planner
- implementer
- reviewer
- release owner

## Example Review Types

Review types might include:

- correctness
- architecture alignment
- documentation completeness
- usability

## Example Orchestration

A feature might move through the system like this:

1. Planning defines the task and expected constraints
2. Implementation performs the change
3. Review types are applied by the appropriate roles
4. Open issues trigger revision or escalation
5. Durable tradeoffs are recorded in decision history

## Why This Example Matters

This example shows how the same scaffold scales by making orchestration more explicit, not by abandoning the core distinctions.
