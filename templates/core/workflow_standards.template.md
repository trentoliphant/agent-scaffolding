# WORKFLOW STANDARDS

> Status: Optional baseline
> Alignment: Aligned with the open-standard rewrite
> Intended role: optional implementation-specific template for repository workflow conventions
> Use it for: local promotion, handoff, and repository workflow rules, not as
> standard core

## Purpose

This document defines local workflow and repository practices for the project.

It governs how changes are prepared, reviewed, recorded, and promoted through
the development process.

It does not define:
- system architecture
- coding or domain-production conventions
- project planning structure or domain task content

Architecture is defined in `SYSTEM_MODEL.md`.
Implementation conventions may be defined in `CODING_STANDARDS.md` or another
domain-specific standards document.
Task sequencing is defined in `PLAN.md` and current status is tracked in
`PROGRESS.md` or an equivalent state record.

---

## Core principles

- Work should be traceable
- Changes should be intentional and scoped
- Repository history should remain understandable
- Durable documents and implementation artifacts should stay aligned
- Task completion should reflect reality, not aspiration
- Shared truth documents should change explicitly

---

## Scope

This document applies to:

- Git usage
- Commits
- Branching
- Task lifecycle updates
- Review and promotion workflow
- Update rules for project documents

Use only the sections that match the project's actual workflow.
Projects that do not use Git, commits, or pull requests should replace those
sections with equivalent local promotion rules.

---

## Workflow roles

### Contributor
Performs work for an assigned task.

### Reviewer
Applies the relevant verification contract before the work is accepted.

### Human approver
Approves promotion of work where required by local authority, risk, or
escalation rules.

---

## Branching conventions

### Required

- Changes must be made on an appropriate branch unless the project explicitly
  uses a different workflow
- Work on unrelated tasks should not be mixed in the same branch
- Branches should reflect the task or purpose of the work

### Preferred

- Use short, descriptive branch names
- Include task identifier when applicable

Examples:
- `task-1.10-exclusions`
- `phase-2-cli-search`
- `fix-task-1.12-index-writer`

### Avoid

- Long-lived branches with many unrelated changes
- Generic names like `test`, `stuff`, `misc`
- Mixing planning, architecture, and implementation changes casually

---

## Commit standards

### Required

- Commits must represent intentional units of change
- Commit messages must be clear and descriptive
- Commits should align with the current task where applicable
- Do not commit broken or knowingly incomplete work as final task completion

### Preferred

- Keep commits small enough to understand
- Separate documentation updates from unrelated code changes when practical
- Use task identifiers in commit messages

### Avoid

- Vague messages like `update`, `fix`, `changes`
- Large commits mixing unrelated concerns
- Hidden architectural or plan changes inside implementation commits

---

## Commit message format

Use a clear, structured format.

### Preferred format

`task-X.Y: short description`

Examples:
- `task-1.10: add exclusion rules component`
- `task-2.4: implement search command output`
- `task-3.2: add hardware detection`

For non-task changes:
- `plan: reorder phase 2 dependencies`
- `system-model: clarify connector boundary`
- `workflow: update review criteria`

---

## Staging and commit behavior

### Required

- Review staged changes before commit
- Ensure commit scope matches commit message
- `git add` and `git commit` should be separate actions unless the project
  explicitly allows otherwise

### Preferred

- Stage only relevant files
- Confirm document updates are included when required

### Avoid

- Blindly committing all modified files
- Combining unrelated fixes into one commit
- Committing generated or temporary files unless intended

---

## Pull Request Or Promotion Standards

Use this section only if the project uses pull requests, merge requests, or an
equivalent promotion flow.

### Required

- PRs must state what changed and why
- PRs must identify the related task or work item
- PRs must note any changes to shared truth documents:
  - `SYSTEM_MODEL.md`
  - `PLAN.md`
  - `PROGRESS.md`
  - workflow standards or equivalent orchestration document
  - templates

### Preferred

- Keep PRs aligned to a single task or closely related unit of work
- Include testing notes
- Include review notes or known limitations when relevant

### Avoid

- Large PRs spanning many unrelated tasks
- Merging without confirming task state and documentation alignment

---

## Task Lifecycle Workflow

The default workflow for a task is:

1. Select task from `PLAN.md` and `PROGRESS.md`
2. Prepare or update a task specification when useful
3. Execute the work
4. Run required checks or collect required evidence
5. Apply the relevant verification contract
6. Record the task-cycle trace
7. Update project documents when the task changes durable truth
8. Promote or commit changes through the local workflow
9. Mark status appropriately

---

## Task Status Rules

Use consistent task statuses.

### Standard statuses

- Not Started
- In Progress
- Pending Verification
- Verification In Progress
- Done
- Blocked

### Required

- Status must reflect real state
- Do not mark a task Done before required verification is complete
- Do not mark a task Done if unresolved verifier concerns remain

---

## Document update rules

### PROGRESS.md

Update when:
- a task starts
- a task changes status
- a task is blocked
- ownership changes

Must remain:
- concise
- state-focused
- free of architecture or planning reasoning

---

### HISTORY.md

Update when:
- a meaningful discovery occurs
- behavior differs from prior assumptions
- a useful implementation or harness insight should be preserved

Must remain:
- append-only
- structured
- insight-focused

---

### PLAN.md

Update only when:
- sequencing is wrong
- dependency structure is wrong
- tasks need to be added, removed, or reorganized

Do not update PLAN.md implicitly during normal implementation.

---

### SYSTEM_MODEL.md

Update only when:
- architecture changes
- responsibilities or invariants change
- a boundary is clarified at the architectural level

Do not update SYSTEM_MODEL.md for ordinary implementation details.

---

### CODING_STANDARDS.md / WORKFLOW_STANDARDS.md

Update only when:
- a repeated pattern suggests the standards are incomplete
- periodic review identifies a reusable improvement
- the team explicitly agrees to a new default

Do not promote a single task-specific preference into a shared standard without
evidence that it should recur.

---

## Review workflow

### Required

Before a task is promoted:
- required checks or evidence must be complete
- required verification must occur
- required document updates must be completed

### Preferred

- Verifier comments should be actionable and concise
- Human approval should focus on trust, risk, and decision rights, not redoing
  all prior verification

---

## Blocking rules

A task should be marked Blocked when:

- required dependencies are not met
- harness, architecture, or domain clarification is needed
- plan sequencing prevents safe progress
- external information or approval is required

Blocked status should include a brief note explaining why.

---

## Repository hygiene

### Required

- Remove temporary artifacts not meant for version control
- Ensure repository state is understandable after each task
- Keep planning and execution artifacts organized consistently

### Preferred

- Update ignore files intentionally
- Keep template and live document directories clearly separated

### Avoid

- Leaving scratch files without purpose
- Letting generated or temporary files accumulate unnoticed

---

## Deviation rules

These standards define the default workflow.

If a project needs to deviate:

- make the deviation explicit
- keep it narrow in scope
- document the reason when meaningful
- avoid silent drift from the local harness

---

## What this document is not

This document does not define:

- Architecture
- Code style or language conventions
- Task-specific implementation instructions
- Model evaluation rules
- Human or agent role capability profiles
