# OPERATING MODEL — AI TEAM

## Purpose

This document defines the operating model for AI-assisted, multi-agent
project planning and execution.

It governs how coding agents, reviewer agents, and humans collaborate,
how work is validated, how trust is established, and how decisions are
escalated.

This model enables parallel execution while preserving system integrity.

---

## Core principles

- Structure before execution
- Architecture before planning
- Planning before implementation
- One step = one unit of work
- Separate machine validation from human acceptance
- Fix forward, do not rewrite history
- Explicit dependencies and ownership
- Controlled promotion of shared truth

---

## Roles

### Coding agent
- Implements `step_X.Y_spec.md`
- Produces working code
- Writes tests

### Reviewer agent
- Validates implementation against:
  - `step_X.Y_spec.md`
  - `SYSTEM_MODEL.md`
  - `OPERATING_MODEL.md`
  - relevant standards documents
- Runs structured review checks
- Identifies scope violations, architectural drift, and test issues

### Human
- Validates intent and correctness
- Approves completion (`Done` state)
- Approves all changes to shared truth:
  - `SYSTEM_MODEL.md`
  - `PLAN.md`
  - `OPERATING_MODEL*.md`
  - templates
  - standards documents when appropriate

---

## Document roles

### `SYSTEM_MODEL.md`
Defines architecture, invariants, and boundaries.

### `PLAN.md`
Defines phases, sequencing, and step structure.

### `step_X.Y_spec.md`
Defines execution contract for one step.

### `PROGRESS.md`
Tracks step state, ownership, and status.

### `HISTORY.md`
Records meaningful discoveries and insights.

---

## Required execution context

Before generating or executing a step:

1. `OPERATING_MODEL_AI_TEAM.md`
2. `SYSTEM_MODEL.md`
3. `CODING_STANDARDS.md`
4. `WORKFLOW_STANDARDS.md`
5. `PLAN.md`
6. `PROGRESS.md`
7. Current `step_X.Y_spec.md`

---

## Step ownership

- Each step has exactly one owner (agent or human)
- Only the owner modifies implementation for that step
- Reviewer agents do not implement changes directly
- Ownership must be visible in `PROGRESS.md` or `step_X.Y_spec.md`

---

## Completion states

Each step progresses through the following states:

- Not Started
- In Progress
- Agent Review
- Machine Complete
- Human Review
- Done
- Blocked

---

## Completion definitions

### Machine Complete

A step is Machine Complete when:

- Implementation is finished
- Tests pass
- Reviewer agent validates:
  - scope adherence
  - acceptance criteria coverage
  - architectural constraints
  - no obvious regressions

Machine Complete indicates local correctness, not final acceptance.

---

### Done

A step is Done when:

- Human review is completed
- Implementation is accepted as correct
- The step is considered stable for future work

---

## Dependency levels

Each dependency must specify required completion level.

### Machine-level dependency

- Requires upstream step to be Machine Complete
- Allows parallel progress

Use when:
- dependent work can tolerate upstream changes

---

### Human-level dependency

- Requires upstream step to be Done
- Enforces stability

Use when:
- dependency affects shared structure or meaning
- changes would be costly or destabilizing

---

## Dependency rules

- Dependencies must be explicitly listed in `step_X.Y_spec.md`
- A step must not start unless dependencies meet the required level
- Do not assume behavior of incomplete steps

---

## Machine dependency safety rule

When depending on a Machine Complete step:

- Do not tightly couple to unstable details
- Be prepared to adapt if upstream changes
- Prefer loose interfaces or adapters

If this is not acceptable:
- require a Human-level dependency

---

## Concurrency rules

- Steps may run in parallel only if:
  - they do not modify the same components
  - they do not depend on each other

- If uncertain:
  - default to sequential execution

---

## Step boundary rules

Each step must:

- Have a single clear purpose
- Stay within defined scope
- Avoid implementing future work
- Avoid refactoring unrelated components
- Respect architectural boundaries

---

## Component awareness

Before implementing:

- Check for existing functionality
- Avoid duplication
- Extend existing components where appropriate

---

## Issue classification rules

When issues arise, classify using:

1. `step_X.Y_spec.md`
2. `PLAN.md`
3. `SYSTEM_MODEL.md`
4. Observed behavior

### Implementation issue
- Fix in current step
- Record in `HISTORY.md` if meaningful

### Step spec issue
- Clarify or update `step_X.Y_spec.md`
- Continue

### Plan issue
- Stop execution
- Update `PLAN.md`
- Continue

### Architectural issue
- Stop execution
- Update `SYSTEM_MODEL.md`
- Continue

---

## Architectural escalation triggers

Escalate when:

- A change affects multiple components
- A boundary is unclear or inconsistent
- A workaround bypasses an abstraction
- Two implementations conflict conceptually

---

## Fix-forward rule

Do not rewrite completed steps.

If issues are discovered:

- Fix forward when intent was correct
- Clarify step if ambiguous
- Update plan if sequence was wrong
- Update system model if architecture was wrong

Record meaningful insights in `HISTORY.md`.

---

## Review flow

### Agent review (required)

Reviewer agents must validate:

- scope adherence
- acceptance criteria
- architectural constraints
- test validity
- regression risk

---

### Human review (required for Done)

Human review is required before:

- Marking a step as Done
- Accepting significant behavioral changes

Human review focuses on:

- intent correctness
- real-world behavior
- test realism
- proper classification and escalation

---

## Human-required checkpoints

Human approval is required for:

1. Transition from Machine Complete → Done
2. Any change to:
   - `SYSTEM_MODEL.md`
   - `PLAN.md`
   - `OPERATING_MODEL*.md`
   - templates
   - standards documents when defaults change
3. Periodic reviews

---

## Progress rules

`PROGRESS.md` tracks:

- step
- owner
- status
- notes

It must not include:

- planning logic
- architectural decisions
- implementation details

---

## History rules

`HISTORY.md` is append-only.

Use it to record:

- non-obvious behavior
- important discoveries
- fix-forward changes
- execution insights

Keep entries concise and structured.

---

## Periodic review

At regular intervals:

- Review patterns in `HISTORY.md`
- Identify repeated issues
- Detect architectural tension
- Promote improvements to:
  - `SYSTEM_MODEL.md`
  - `PLAN.md`
  - `OPERATING_MODEL*.md`
  - standards documents
  - templates

---

## Experimental run mode

The system may operate in Experimental Run mode for the purpose of
improving process, templates, and agent behavior.

In this mode:

- Steps may proceed from Machine Complete without human review
- Full development cycles may be completed by agents only
- Reviewer agents remain active
- Human review is deferred until after the run

### Experimental constraints

- No experimental output is considered Done
- No experimental output may be used in production
- All outputs are treated as untrusted artifacts
- Results must be reviewed before promotion

### Post-run review

After an experimental run:

- Conduct structured review
- Analyze `HISTORY.md` and outputs
- Identify patterns and failures
- Promote improvements to:
  - operating models
  - system model
  - plan
  - standards documents
  - templates

Do not promote implementation artifacts directly.

---

## Anti-patterns

- Treating Machine Complete as final
- Skipping human review for critical steps
- Hidden architectural changes
- Ignoring dependencies
- Multiple agents modifying same step
- Duplicate implementations
- Over-coupling to unstable upstream steps
- Mixing roles of documents
