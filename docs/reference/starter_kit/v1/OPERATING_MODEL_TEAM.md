# OPERATING MODEL

## Purpose

This document defines the operating model for AI-assisted project
planning and execution.

It governs how work is structured, how documents are used, how issues
are classified, how decisions are escalated, and how execution proceeds.

It applies to all contributors and is process-level, not project-specific.

---

## Core principles

- Structure before execution
- Architecture before planning
- Planning before implementation
- One step = one unit of work
- Explicit scope boundaries
- Explicit escalation for higher-level issues
- Fix forward, do not rewrite history
- Shared clarity over individual interpretation

---

## Document roles

### SYSTEM_MODEL.md
Defines architecture, invariants, responsibilities, and boundaries.

### PLAN.md
Defines phases, sequencing, and step structure.

### step_X.Y_spec.md
Defines execution contract for a single step.

### PROGRESS.md
Tracks execution state only.

### HISTORY.md
Records meaningful discoveries and execution insights.

---

## Required execution context

Before generating or executing a step, read:

1. OPERATING_MODEL.md
2. SYSTEM_MODEL.md
3. PLAN.md
4. PROGRESS.md
5. Current step spec

---

## Planning rules

- SYSTEM_MODEL.md must exist before implementation begins
- PLAN.md must be derived from SYSTEM_MODEL.md
- Step specs must be derived from SYSTEM_MODEL.md, PLAN.md, and PROGRESS.md
- Only one active step spec per step
- Steps must define dependencies explicitly

---

## Step ownership

- Each step has exactly one owner
- Only the owner modifies code for that step
- Others may review or suggest, but not implement
- Ownership must be visible in STEP_SPEC and/or PROGRESS.md

---

## Concurrency rules

- Multiple steps may be executed in parallel only if:
  - They do not modify the same components
  - They do not depend on each other

- If steps share dependencies or components:
  - Execute sequentially

- When uncertain:
  - Default to sequential execution

---

## Dependency rules

- A step must not be executed until its dependencies are complete
- Do not assume behavior of incomplete steps
- Dependencies must be explicitly listed in STEP_SPEC

---

## Step boundary rules

Each step must:

- Have a single clear purpose
- Stay within defined scope
- Avoid implementing future-phase work
- Avoid refactoring unrelated components
- Respect architectural boundaries

---

## Component awareness

Before implementing new logic:

- Check if similar functionality already exists
- Prefer extending existing components over duplicating logic
- Avoid parallel implementations of the same concept

---

## Issue classification rules

When an issue is discovered during execution, classify using:

1. Step spec
2. PLAN.md
3. SYSTEM_MODEL.md
4. Existing behavior

### 1. Implementation bug or omission
- Intent is correct, implementation is wrong

Action:
- Fix in current step
- Record in HISTORY.md if meaningful

---

### 2. Step spec gap or ambiguity
- Step is underdefined or unclear

Action:
- Clarify or update step spec
- Continue execution

---

### 3. Plan issue
- Sequence or dependency is incorrect

Action:
- Stop execution
- Update PLAN.md
- Re-read plan
- Continue

---

### 4. Architectural issue
- Invariant, boundary, or abstraction is incorrect or missing

Action:
- Stop execution
- Update SYSTEM_MODEL.md
- Re-read system model
- Continue

---

## Architectural escalation triggers

Escalate to SYSTEM_MODEL.md review if:

- A change affects multiple components
- A boundary feels unclear or inconsistent
- A workaround bypasses an abstraction
- Two implementations conflict conceptually

---

## Fix-forward rule

Completed steps are not rewritten.

If a problem is discovered in earlier work:

- Fix forward if intent was correct
- Clarify step if ambiguous
- Update plan if sequence was wrong
- Update system model if architecture was wrong

Record meaningful insights in HISTORY.md.

---

## Plan mutation rules

- PLAN.md is stable during execution
- Do not modify it implicitly
- Changes must be explicit and justified

---

## System model mutation rules

- SYSTEM_MODEL.md changes only through architectural escalation
- Do not change architecture implicitly during step execution

---

## Progress rules

PROGRESS.md tracks state only.

It may include:
- Step
- Description
- Owner
- Status
- Brief notes

It must not include:
- Planning logic
- Architecture decisions
- Implementation details

---

## History rules

HISTORY.md is append-only.

Use it to record:
- Non-obvious behavior
- Important discoveries
- Corrections and insights

Keep entries:
- Concise
- Structured
- Relevant

---

## Review requirements

### Step review (required)

Before marking a step complete:

- Run STEP_REVIEW checklist
- Resolve any issues
- Ensure alignment with system and plan

---

### Periodic review (recommended)

At regular intervals:

- Identify patterns and friction
- Detect repeated issues
- Extract insights
- Promote improvements to:
  - SYSTEM_MODEL.md
  - PLAN.md
  - OPERATING_MODEL.md
  - templates

---

## Anti-patterns

- Implementing future work during a step
- Silent architectural changes
- Ignoring dependencies
- Multiple owners modifying the same step
- Duplicate implementations of the same concept
- Mixing roles of documents
- Skipping step specs
- Treating HISTORY as a planning or architecture document
