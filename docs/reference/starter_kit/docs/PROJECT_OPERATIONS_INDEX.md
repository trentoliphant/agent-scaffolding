[200~# PROJECT OPERATIONS INDEX

## Purpose

This document provides a quick orientation to the project’s scaffolding
documents and execution system.

It explains what each document is for, when it should be used, and how the
documents work together.

Use this as the entry point for humans or agents who need to understand how
the project is structured before doing work.

---

## System overview

This project uses a structured document system to support planning,
implementation, review, and learning.

The system separates:

- process governance
- system architecture
- coding conventions
- workflow conventions
- project planning
- step execution
- progress tracking
- historical learning

This separation is intentional. Each document has a distinct responsibility.

---

## Document map

### `process/OPERATING_MODEL.md`
Defines how work is governed.

Use for:
- execution rules
- issue classification
- escalation behavior
- review flow
- dependency behavior
- trust and promotion rules

Do not use for:
- project architecture
- coding style
- step-specific implementation

---

### `docs/SYSTEM_MODEL.md`
Defines what the system is.

Use for:
- architecture
- invariants
- boundaries
- core abstractions
- system responsibilities

Do not use for:
- coding style
- workflow conventions
- implementation details of a single step

---

### `docs/CODING_STANDARDS.md`
Defines how code should be written.

Use for:
- code organization
- naming conventions
- testing standards
- error handling style
- language-specific coding rules

Do not use for:
- architecture
- git workflow
- step sequencing

---

### `docs/WORKFLOW_STANDARDS.md`
Defines repository and workflow practices.

Use for:
- commit message format
- branch conventions
- document update rules
- step status handling
- repository hygiene

Do not use for:
- code style
- architecture
- step-specific implementation details

---

### `docs/PLAN.md`
Defines what gets built and in what order.

Use for:
- phases
- step list
- dependencies between steps
- planning decisions

Do not use for:
- architecture
- coding conventions
- detailed execution instructions

---

### `steps/step_X.Y_spec.md`
Defines the execution contract for one step.

Use for:
- objective
- scope
- dependencies
- outputs
- acceptance criteria
- testing requirements

Do not use for:
- architecture redesign
- broad planning changes
- workflow policy

---

### `docs/PROGRESS.md`
Tracks current state of execution.

Use for:
- step status
- owner
- brief current notes
- blocked state

Do not use for:
- planning logic
- architecture reasoning
- implementation detail

---

### `docs/HISTORY.md`
Records meaningful discoveries and execution insights.

Use for:
- non-obvious behavior
- fix-forward corrections
- implementation insights
- lessons worth preserving

Do not use for:
- replacing architecture docs
- planning future work
- storing step instructions

---

## Recommended reading order

### For a new contributor or agent

Read in this order:

1. `PROJECT_OPERATIONS_INDEX.md`
2. `process/OPERATING_MODEL.md`
3. `docs/SYSTEM_MODEL.md`
4. `docs/CODING_STANDARDS.md`
5. `docs/WORKFLOW_STANDARDS.md`
6. `docs/PLAN.md`
7. `docs/PROGRESS.md`
8. Current `steps/step_X.Y_spec.md`

---

## When to update each document

### Update `SYSTEM_MODEL.md` when:
- architecture changes
- responsibilities change
- an invariant changes
- a boundary needs clarification

### Update `CODING_STANDARDS.md` when:
- a repeated implementation pattern should become standard
- language-specific defaults need clarification

### Update `WORKFLOW_STANDARDS.md` when:
- repository or process defaults change
- review / commit / branch conventions evolve

### Update `PLAN.md` when:
- step sequence is wrong
- dependencies are wrong
- new steps or phases are needed

### Update `PROGRESS.md` when:
- a step changes status
- ownership changes
- a step becomes blocked or unblocked

### Update `HISTORY.md` when:
- meaningful discoveries occur
- a fix-forward change teaches something worth preserving
- execution reveals a non-obvious system truth

### Update `step_X.Y_spec.md` when:
- the current step needs clarification
- the step is underdefined
- local execution guidance needs refinement

---

## Decision guide

If something changes during execution, use this guide:

- **Implementation issue** → fix in current step
- **Step ambiguity** → update step spec
- **Plan sequencing issue** → update `PLAN.md`
- **Architecture issue** → update `SYSTEM_MODEL.md`
- **Repeated coding pattern** → update `CODING_STANDARDS.md`
- **Repeated workflow/process pattern** → update `WORKFLOW_STANDARDS.md` or `OPERATING_MODEL.md`
- **Meaningful discovery** → record in `HISTORY.md`

---

## Execution loop

The normal step workflow is:

1. Read project context
2. Select current step
3. Read or create step spec
4. Execute implementation
5. Run tests
6. Review
7. Update documents
8. Commit
9. Update progress
10. Repeat

---

## Periodic review

At regular intervals, review:

- `HISTORY.md` for repeated patterns
- `PROGRESS.md` for bottlenecks
- `PLAN.md` for sequencing issues
- standards documents for missing defaults

Promote repeated insights upward into the appropriate documents.

---

## Experimental mode

If operating in experimental mode:

- clearly label the run as experimental
- do not treat outputs as production-trusted
- use model evaluation and post-experiment review artifacts
- promote only reviewed process improvements

---

## File placement reference

Suggested structure:

project-root/
  process/
    OPERATING_MODEL.md

  docs/
    PROJECT_OPERATIONS_INDEX.md
    SYSTEM_MODEL.md
    CODING_STANDARDS.md
    WORKFLOW_STANDARDS.md
    PLAN.md
    PROGRESS.md
    HISTORY.md

  steps/
    step_1.1_spec.md
    step_1.2_spec.md

---

## What this document is not

This document does not define:

- Architecture
- Code style
- Workflow rules themselves
- Project plan contents
- Step-specific implementation

It is a navigation and orientation document.
