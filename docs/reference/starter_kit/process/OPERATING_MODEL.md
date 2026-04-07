# OPERATING MODEL

## Purpose

This document defines the operating model for AI-assisted project planning
and execution.

It governs how work is structured, how documents are used, how issues are
classified, how changes are escalated, and how execution proceeds.

It is process-level, not project-specific.

---

## Core principles

- Structure before execution
- Architecture before planning
- Planning before implementation
- One step at a time
- Explicit scope boundaries
- Explicit escalation when higher-level issues are discovered
- Progress and history are recorded as part of execution

---

## Document roles

### SYSTEM_MODEL.md
Defines the architecture, invariants, responsibilities, and constraints of
the system being built.

### PLAN.md
Defines phases, sequencing, and the ordered list of work.

### step_X.Y_spec.md
Defines the execution contract for one step only.

### PROGRESS.md
Tracks execution state only.

### HISTORY.md
Records meaningful discoveries, corrections, and execution insights.

---

## Required execution context

Before generating or executing a step, read:

1. OPERATING_MODEL.md
2. SYSTEM_MODEL.md
3. CODING_STANDARDS.md
4. WORKFLOW_STANDARDS.md
5. PLAN.md
6. PROGRESS.md
7. Current step spec

---

## Planning rules

- SYSTEM_MODEL.md must exist before implementation begins
- PLAN.md must be based on SYSTEM_MODEL.md
- Step specs must be based on SYSTEM_MODEL.md, PLAN.md, and current progress
- Only one step spec is active at a time

---

## Step boundary rules

Each step must:

- Have one clear purpose
- Stay within its defined scope
- Avoid implementing future work
- Avoid refactoring unrelated areas
- Respect architectural constraints

---

## Issue classification rules

When an issue is discovered during execution, classify it using these
sources in order:

1. Current step spec
2. PLAN.md
3. SYSTEM_MODEL.md
4. Existing code behavior

Classify the issue as one of:

### 1. Implementation bug or omission
The step intent is still correct, but the implementation is wrong or incomplete.

Action:
- Fix in the current step
- Record in HISTORY.md if meaningful

### 2. Step spec gap or ambiguity
The step is underdefined or unclear, but the broader plan and architecture
remain correct.

Action:
- Update the step spec if needed
- Continue execution

### 3. Plan issue
The sequence, dependency, or step breakdown is wrong or incomplete.

Action:
- Stop execution
- Update PLAN.md
- Re-read plan
- Continue

### 4. Architectural issue
An invariant, boundary, responsibility, or design decision is wrong, missing,
or no longer viable.

Action:
- Stop execution
- Update SYSTEM_MODEL.md
- Re-read system model
- Continue

When uncertain, prefer the lowest level that resolves the issue cleanly.

---

## Fix-forward rule

Completed steps are not rewritten as if they never happened.

If a later step reveals a problem in earlier work:

- fix forward if the intent was correct
- clarify the step if the step was ambiguous
- update the plan if sequencing was wrong
- update the system model if architecture was wrong

Record meaningful discoveries in HISTORY.md.

---

## Plan mutation rules

- PLAN.md is stable during execution
- Do not modify PLAN.md implicitly
- If PLAN.md changes, do so explicitly and with rationale

---

## System model mutation rules

- SYSTEM_MODEL.md changes only through architectural escalation
- Do not change architecture implicitly during step execution

---

## Progress rules

PROGRESS.md tracks state only.

It may include:
- step
- description
- status
- brief notes

It must not include:
- planning logic
- architectural decisions
- implementation details

---

## History rules

HISTORY.md is append-only.

Use it to capture:
- important discoveries
- meaningful corrections
- non-obvious behavior
- execution insights worth preserving

Do not use it as a substitute for:
- SYSTEM_MODEL.md
- PLAN.md
- step specs

Promote information upward only when required.

---

## Anti-patterns

- Mixing architecture into PLAN.md
- Mixing planning into PROGRESS.md
- Using HISTORY.md as a decision log for architecture
- Implementing future work during a current step
- Generating multiple active step specs at once
- Silently changing higher-level documents during execution
