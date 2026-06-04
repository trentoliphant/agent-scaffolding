# CLAUDE.md — AI Execution Instructions for [Project Name]

> Status: Incubating
> Alignment: Not yet aligned with the current open-standard rewrite
> Intended role: earlier research-domain adapter material
> Use it for: reference or future integration work, not as current standard core

This file is read automatically by Claude Code at the start of every session.
It resolves conflicts and ambiguities across framework documents and defines
how AI agents should behave in this research project.

---

## Project type

Domain adapter: **research**
Scaffold version: [version]
Project: [Project Name]

---

## Required reading order

Before generating or executing any step, read these documents in order:

1. `OPERATING_MODEL.md`
2. `RESEARCH_STANDARDS.md`
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
- Base it on `RESEARCH_STANDARDS.md`, `PLAN.md`, and `PROGRESS.md`.
- Do not begin work until the spec exists and has been read.

---

## Research artifact location rules

Research artifacts produced by steps follow this structure:

```
research/
  landscape/
  analysis/
  evaluations/
  synthesis/
  recommendations/
  evidence/
```

Create the appropriate subdirectory if it does not exist.
Do not place research artifacts at the project root.

The `evidence/` directory holds raw data, logs, scripts, and
reproducible outputs that back the claims in other artifacts.
Evidence files are referenced from research artifacts, not read
as standalone documents.

---

## What counts as a step output

In a research project, the step output is a document backed by
evidence — not an opinion or summary.

A step output is complete when:
- The artifact file exists at the correct path
- It contains a confidence marker
- All claims cite evidence or state their basis
- Gaps and limitations are identified
- Open questions are recorded

Do not treat an artifact as complete because it is long or detailed.
Completeness is defined by the step spec's completeness criteria.

---

## Issue classification for research projects

Use the same four-level classification from `OPERATING_MODEL.md`,
with these research-specific escalation targets:

### 1. Artifact error or omission
The step intent is correct but the artifact has a factual error,
missing evidence, or unsupported claim.
Action: Fix in the current step. Record in HISTORY.md if meaningful.

### 2. Step spec gap or ambiguity
The step is underdefined but the plan and charter are correct.
Action: Update the step spec. Continue.

### 3. Plan issue
The investigation sequence, step breakdown, or artifact dependencies
are wrong — typically because early findings change what needs to be
investigated next.
Action: Stop. Update PLAN.md. Re-read. Continue.

### 4. Charter or scope issue
A core research question, scope boundary, or foundational assumption
is wrong, missing, or invalidated by findings.
Action: Stop. Update PROJECT_CHARTER.md or the relevant research
artifact. Re-read. Continue.

When uncertain, prefer the lowest level that resolves the issue cleanly.
For class 3 or 4 issues, present findings to the user before mutating
high-level documents.

### Research-specific escalation note

Research frequently produces class 3 issues — early findings that
change what needs to be investigated. This is expected and normal.
Plan mutations in research projects are more frequent than in design
projects. Do not treat plan changes as failure; treat resistance to
plan changes when evidence demands them as failure.

---

## Confidence marker promotion

Do not promote a confidence marker without explicit instruction or
a step spec that specifies promotion as part of completeness criteria.

Record all confidence promotions in HISTORY.md:
```
Promoted [artifact] from Draft to Reviewed — [brief reason]
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

Research steps frequently generate more open questions than they
resolve. This is expected and healthy. Track them rigorously.

---

## Evidence discipline

Every factual claim in a research artifact must have a stated basis.
Acceptable bases are:

- **Direct observation** — the agent ran a command, inspected a file,
  or tested a tool and recorded the result
- **Source citation** — a specific document, repository, or
  authoritative reference was consulted
- **Inference from evidence** — a conclusion drawn from multiple
  observations, with the reasoning stated
- **Expert input** — the user or a named expert provided the claim

Unattributed claims are not acceptable. If a claim cannot be
attributed, mark it as an open question or a hypothesis.

---

## Consistency checks

Before completing a step, check the produced artifact for consistency
with existing Reviewed artifacts. If a conflict is found:

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
   resolution, or confidence promotion occurred
4. Confirm staged files match commit scope

---

## Git behavior

Follow the same git behavior as defined in `WORKFLOW_STANDARDS.md`:

1. Stage specific files by name
2. Show staged diff to confirm scope matches commit message
3. Commit with required format

Commit message format for research steps:

```
step-X.Y: short description of artifact produced
```

For non-step changes:
```
charter: narrow research scope based on phase 1 findings
plan: add investigation branch for [topic]
research-standards: add evaluation framework guidance
```

---

## Human review triggers

Stop and present findings to the user when:

- A class 3 or class 4 issue is discovered before mutating PLAN.md
  or PROJECT_CHARTER.md
- A step spec specifies human review required
- A recommendation artifact is being promoted to Reviewed
- A confidence marker is being promoted to Verified
- Two framework documents conflict and cannot be resolved with
  the rules in this file
- An open question is blocking step completion
- Findings contradict a charter assumption — this is always a
  human review moment regardless of issue class

---

## Document update summary

| Document | When to update |
|----------|---------------|
| `PROGRESS.md` | Step starts, status changes, or step is blocked |
| `HISTORY.md` | Meaningful discovery, conflict resolution, confidence promotion — append only |
| `PLAN.md` | When investigation sequence or step structure needs to change based on findings |
| `PROJECT_CHARTER.md` | Only through explicit charter escalation — class 4 issue |
| `RESEARCH_STANDARDS.md` | Only when a repeated pattern reveals a reusable improvement |
| `WORKFLOW_STANDARDS.md` | Only when a repeated pattern reveals a reusable improvement |

---

## Scope discipline

These rules apply to every step without exception:

- Do not investigate future-phase topics within a current-phase step
- Do not make design decisions in research artifacts — research
  informs design, it does not replace it
- Do not resolve open questions by making undocumented assumptions
- Do not update PROJECT_CHARTER.md or PLAN.md silently
- Do not promote confidence markers without explicit instruction or
  step spec authorization
- Do not present hypotheses as findings

If scope creep is tempting or seems necessary, classify it as an
issue per OPERATING_MODEL.md before acting.

---

## Transition to design

When research is complete, its outputs become inputs to a design
project. The transition works as follows:

- Research artifacts at Reviewed or Verified confidence become
  input documents for the design PROJECT_CHARTER.md
- Open questions from research that require design decisions
  become entries in the design charter's "Key assumptions" or
  the plan's open questions
- The research project is not modified after transition — it
  becomes a reference, not a living document

Do not begin design work within the research project. If a step
starts producing design artifacts, that is a scope violation.

---

## What to do if these instructions conflict with a step spec

Step specs are scoped to a single step and may override general
standards within that scope. If a step spec instruction conflicts
with a framework document:

- Follow the step spec for the current step
- Record the deviation in HISTORY.md if meaningful
- Do not change the framework document unless the deviation reveals
  a structural gap that warrants it
