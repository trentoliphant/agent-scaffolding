# CLAUDE.md — AI Execution Instructions for [Project Name]

This file is read automatically by Claude Code at the start of every session.
It resolves conflicts and ambiguities across framework documents and defines
how AI agents should behave in this design project.

---

## Project type

Domain adapter: **design**
Scaffold version: [version]
Project: [Project Name]

---

## Required reading order

Before generating or executing any step, read these documents in order:

1. `OPERATING_MODEL.md`
2. `DESIGN_STANDARDS.md`
3. `WORKFLOW_STANDARDS.md`
4. `PROJECT_CHARTER.md`
5. `PLAN.md`
6. `PROGRESS.md`
7. The current active step spec (see file location rules below)

Do not begin work until all of the above have been read in the current
session. If any file is missing and the bootstrap exception in
`OPERATING_MODEL.md` does not apply, stop and ask the user before
proceeding.

---

## Step spec location rules

Step spec files follow this structure:

```
steps/
  phase_1/
    step_1.1.md
    step_1.2.md
  phase_2/
    step_2.1.md
  ...
```

If the step spec for the active step does not exist:
- Create it under `steps/phase_N/` using `STEP_SPEC_TEMPLATE.md`
  before beginning work.
- Base it on `DESIGN_STANDARDS.md`, `PLAN.md`, and `PROGRESS.md`.
- Do not begin work until the spec exists and has been read.

---

## Design artifact location rules

Design artifacts produced by steps follow this structure:

```
design/
  domain/
  workflows/
  boundaries/
  compliance/
  architecture/
```

Create the appropriate subdirectory if it does not exist.
Do not place design artifacts at the project root.

---

## What counts as a step output

In a design project, the step output is a document — not code.

A step output is complete when:
- The artifact file exists at the correct path
- It contains a stability marker
- All decisions required by the step spec are documented
- Open questions are recorded

Do not treat an artifact as complete because it is long or detailed.
Completeness is defined by the step spec's completeness criteria.

---

## Issue classification for design projects

Use the same four-level classification from `OPERATING_MODEL.md`,
with these design-specific escalation targets:

### 1. Artifact bug or omission
The step intent is correct but the artifact is wrong or incomplete.
Action: Fix in the current step. Record in HISTORY.md if meaningful.

### 2. Step spec gap or ambiguity
The step is underdefined but the plan and charter are correct.
Action: Update the step spec. Continue.

### 3. Plan issue
The phase sequence, step breakdown, or artifact dependencies are wrong.
Action: Stop. Update PLAN.md. Re-read. Continue.

### 4. Charter or domain model issue
A core constraint, invariant, scope boundary, or foundational
decision is wrong, missing, or in conflict.
Action: Stop. Update PROJECT_CHARTER.md or the relevant domain
artifact. Re-read. Continue.

When uncertain, prefer the lowest level that resolves the issue cleanly.
For class 3 or 4 issues, present findings to the user before mutating
high-level documents.

---

## Stability marker promotion

Do not promote a stability marker without explicit instruction or
a step spec that specifies promotion as part of completeness criteria.

Record all stability promotions in HISTORY.md:
```
Promoted [artifact] from Provisional to Stable — [brief reason]
```

---

## Open questions

Open questions discovered during a step must be recorded in the
artifact under an "Open questions" section.

An open question does not block step completion unless it is
explicitly marked as blocking in the step spec.

Do not resolve open questions by making undocumented assumptions.
If a question must be resolved to complete the step, surface it
to the user.

---

## Consistency checks

Before completing a step, check the produced artifact for consistency
with existing Stable artifacts. If a conflict is found:

1. Identify which artifact is authoritative
2. Resolve the non-authoritative artifact to align
3. Record the resolution in HISTORY.md
4. If authority is unclear, surface to the user

---

## Step completion — required before final commit

The following must happen before the final commit of any step.
Do not commit until all are done:

1. Verify all completeness criteria in the step spec are met
2. Update PROGRESS.md — mark step Done, one-line notes summary
3. Append to HISTORY.md if any meaningful discovery, conflict
   resolution, or stability promotion occurred
4. Confirm staged files match commit scope

---

## Git behavior

Follow the same git behavior as defined in `WORKFLOW_STANDARDS.md`:

1. Stage specific files by name
2. Show staged diff to confirm scope matches commit message
3. Commit with required format

Commit message format for design steps:

```
step-X.Y: short description of artifact produced
```

For non-step changes:
```
charter: clarify compliance scope
plan: add phase 4 dependency
design-standards: add invariant format guidance
```

---

## Human review triggers

Stop and present findings to the user when:

- A class 3 or class 4 issue is discovered before mutating PLAN.md
  or PROJECT_CHARTER.md
- A step spec specifies human review required
- A compliance artifact is being promoted to Stable
- A stability marker is being promoted to Locked
- Two framework documents conflict and cannot be resolved with
  the rules in this file
- An open question is blocking step completion

---

## Document update summary

| Document | When to update |
|----------|---------------|
| `PROGRESS.md` | Step starts, status changes, or step is blocked |
| `HISTORY.md` | Meaningful discovery, conflict resolution, stability promotion — append only |
| `PLAN.md` | Only when phase sequence, step structure, or dependencies are wrong |
| `PROJECT_CHARTER.md` | Only through explicit charter escalation — class 4 issue |
| `DESIGN_STANDARDS.md` | Only when a repeated pattern reveals a reusable improvement |
| `WORKFLOW_STANDARDS.md` | Only when a repeated pattern reveals a reusable improvement |

---

## Scope discipline

These rules apply to every step without exception:

- Do not design future-phase features within a current-phase step
- Do not make implementation decisions in design artifacts unless
  explicitly in scope for that step
- Do not resolve open questions by making undocumented assumptions
- Do not update PROJECT_CHARTER.md or PLAN.md silently
- Do not promote stability markers without explicit instruction or
  step spec authorization

If scope creep is tempting or seems necessary, classify it as an
issue per OPERATING_MODEL.md before acting.

---

## What to do if these instructions conflict with a step spec

Step specs are scoped to a single step and may override general
standards within that scope. If a step spec instruction conflicts
with a framework document:

- Follow the step spec for the current step
- Record the deviation in HISTORY.md if meaningful
- Do not change the framework document unless the deviation reveals
  a structural gap that warrants it
