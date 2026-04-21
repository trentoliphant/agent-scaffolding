# WORKFLOW STANDARDS

> Status: Transitional
> Alignment: Partially aligned with the open-standard rewrite
> Intended role: optional implementation-specific template for repository workflow conventions
> Use it for: baseline implementation workflow, not as standard core

## Purpose

This document defines workflow and repository practices for the project.

It governs how changes are prepared, reviewed, recorded, and promoted through
the development process.

It does not define:
- system architecture
- coding conventions
- project planning structure

Architecture is defined in `SYSTEM_MODEL.md`.
Coding conventions are defined in `CODING_STANDARDS.md`.
Execution governance is defined in the project's operating model or equivalent orchestration/workflow document.

---

## Core principles

- Work should be traceable
- Changes should be intentional and scoped
- Repository history should remain understandable
- Documentation and code should stay aligned
- Step completion should reflect reality, not aspiration
- Shared truth documents should change explicitly

---

## Scope

This document applies to:

- Git usage
- Commits
- Branching
- Step lifecycle updates
- Review and promotion workflow
- Update rules for project documents

---

## Workflow roles

### Contributor
Implements work for an assigned step.

### Reviewer
Validates work against step and project standards.

### Human approver
Approves promotion of work where required by the operating model.

---

## Branching conventions

### Required

- Changes must be made on an appropriate branch unless the project explicitly
  uses a different workflow
- Work on unrelated steps should not be mixed in the same branch
- Branches should reflect the step or purpose of the work

### Preferred

- Use short, descriptive branch names
- Include step identifier when applicable

Examples:
- `step-1.10-exclusions`
- `phase-2-cli-search`
- `fix-step-1.12-index-writer`

### Avoid

- Long-lived branches with many unrelated changes
- Generic names like `test`, `stuff`, `misc`
- Mixing planning, architecture, and implementation changes casually

---

## Commit standards

### Required

- Commits must represent intentional units of change
- Commit messages must be clear and descriptive
- Commits should align with the current step where applicable
- Do not commit broken or knowingly incomplete work as final step completion

### Preferred

- Keep commits small enough to understand
- Separate documentation updates from unrelated code changes when practical
- Use step identifiers in commit messages

### Avoid

- Vague messages like `update`, `fix`, `changes`
- Large commits mixing unrelated concerns
- Hidden architectural or plan changes inside implementation commits

---

## Commit message format

Use a clear, structured format.

### Preferred format

`step-X.Y: short description`

Examples:
- `step-1.10: add exclusion rules component`
- `step-2.4: implement search command output`
- `step-3.2: add hardware detection`

For non-step changes:
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

## Pull request / merge standards

Use this section only if the project uses PRs or equivalent review flow.

### Required

- PRs must state what changed and why
- PRs must identify the related step(s)
- PRs must note any changes to shared truth documents:
  - `SYSTEM_MODEL.md`
  - `PLAN.md`
  - operating model or equivalent execution-governance document
  - templates

### Preferred

- Keep PRs aligned to a single step or closely related unit of work
- Include testing notes
- Include review notes or known limitations when relevant

### Avoid

- Large PRs spanning many unrelated steps
- Merging without confirming step state and documentation alignment

---

## Step lifecycle workflow

The default workflow for a step is:

1. Select step from `PLAN.md` and `PROGRESS.md`
2. Prepare or update `step_X.Y_spec.md`
3. Execute implementation
4. Run tests
5. Perform review
6. Update project documents
7. Commit changes
8. Mark status appropriately

---

## Step status rules

Use consistent step statuses.

### Standard statuses

- Not Started
- In Progress
- Agent Review
- Machine Complete
- Human Review
- Done
- Blocked

### Required

- Status must reflect real state
- Do not mark a step Done before required review is complete
- Do not mark a step Machine Complete if reviewer concerns remain unresolved

---

## Document update rules

### PROGRESS.md

Update when:
- a step starts
- a step changes status
- a step is blocked
- ownership changes

Must remain:
- concise
- state-focused
- free of architecture or planning reasoning

---

### HISTORY.md

Update when:
- a meaningful discovery occurs
- a fix-forward correction is made
- behavior differs from prior assumptions
- a useful implementation insight should be preserved

Must remain:
- append-only
- structured
- insight-focused

---

### PLAN.md

Update only when:
- sequencing is wrong
- dependency structure is wrong
- steps need to be added, removed, or reorganized

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

---

## Review workflow

### Required

Before a step is promoted:
- required tests must pass
- required review must occur
- required document updates must be completed

### Preferred

- Reviewer comments should be actionable and concise
- Human approval should focus on trust and correctness, not redoing all prior review

---

## Blocking rules

A step should be marked Blocked when:

- required dependencies are not met
- architectural clarification is needed
- plan sequencing prevents safe progress
- external information or approval is required

Blocked status should include a brief note explaining why.

---

## Experimental workflow

If operating in experimental mode:

- mark the run or step clearly as experimental
- do not treat experimental output as Done for production purposes
- keep outputs separate or clearly labeled
- use post-experiment review before promoting process changes

---

## Repository hygiene

### Required

- Remove temporary artifacts not meant for version control
- Ensure repository state is understandable after each step
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
- avoid silent drift from the standard

---

## What this document is not

This document does not define:

- Architecture
- Code style or language conventions
- Step-specific implementation instructions
- Model evaluation rules
- Human or agent role capability profiles
