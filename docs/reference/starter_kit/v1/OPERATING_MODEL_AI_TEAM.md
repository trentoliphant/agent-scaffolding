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
- Implements STEP_SPEC
- Produces working code
- Writes tests

### Reviewer agent
- Validates implementation against:
  - STEP_SPEC
  - SYSTEM_MODEL
  - OPERATING_MODEL
- Runs structured review checks
- Identifies scope violations, architectural drift, and test issues

### Human
- Validates intent and correctness
- Approves completion (Done state)
- Approves all changes to shared truth:
  - SYSTEM_MODEL
  - PLAN
  - OPERATING_MODEL
  - templates

---

## Document roles

### SYSTEM_MODEL.md
Defines architecture, invariants, and boundaries.

### PLAN.md
Defines phases, sequencing, and step structure.

### step_X.Y_spec.md
Defines execution contract for one step.

### PROGRESS.md
Tracks step state, ownership, and status.

### HISTORY.md
Records meaningful discoveries and insights.

---

## Required execution context

Before generating or executing a step:

1. OPERATING_MODEL_AI_TEAM.md
2. SYSTEM_MODEL.md
3. PLAN.md
4. PROGRESS.md
5. Current STEP_SPEC

---

## Step ownership

- Each step has exactly one owner (agent or human)
- Only the owner modifies implementation
- Reviewer agents do not implement changes directly
- Ownership must be visible in PROGRESS.md or STEP_SPEC

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
  - Scope adherence
  - Acceptance criteria coverage
  - Architectural constraints
  - No obvious regressions

Machine Complete indicates **local correctness**, not final acceptance.

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

Used when:
- dependent work can tolerate upstream changes

---

### Human-level dependency

- Requires upstream step to be Done
- Enforces stability

Used when:
- dependency affects shared structure or meaning
- changes would be costly or destabilizing

---

## Dependency rules

- Dependencies must be explicitly listed in STEP_SPEC
- A step must not start unless dependencies meet required level
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
  - They do not modify the same components
  - They do not depend on each other

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

1. STEP_SPEC
2. PLAN.md
3. SYSTEM_MODEL.md
4. Observed behavior

### Implementation issue
- Fix in current step
- Record in HISTORY.md if meaningful

### Step spec issue
- Clarify or update STEP_SPEC
- Continue

### Plan issue
- Stop execution
- Update PLAN.md
- Continue

### Architectural issue
- Stop execution
- Update SYSTEM_MODEL.md
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

Record meaningful insights in HISTORY.md.

---

## Review flow

### Agent review (required)

Reviewer agents must validate:

- Scope adherence
- Acceptance criteria
- Architectural constraints
- Test validity
- Regression risk

---

### Human review (required for Done)

Human review is required before:

- Marking a step as Done
- Accepting significant behavioral changes

Human review focuses on:

- Intent correctness
- Real-world behavior
- Test realism
- Proper classification and escalation

---

## Human-required checkpoints

Human approval is required for:

1. Transition from Machine Complete → Done
2. Any change to:
   - SYSTEM_MODEL.md
   - PLAN.md
   - OPERATING_MODEL
   - templates
3. Periodic reviews

---

## Progress rules

PROGRESS.md tracks:

- Step
- Owner
- Status
- Notes

It must not include:

- Planning logic
- Architectural decisions
- Implementation details

---

## History rules

HISTORY.md is append-only.

Use it to record:

- Non-obvious behavior
- Important discoveries
- Fix-forward changes
- Execution insights

Keep entries concise and structured.

---

## Periodic review

At regular intervals:

- Review patterns in HISTORY.md
- Identify repeated issues
- Detect architectural tension
- Promote improvements to:
  - SYSTEM_MODEL.md
  - PLAN.md
  - OPERATING_MODEL
  - templates

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
