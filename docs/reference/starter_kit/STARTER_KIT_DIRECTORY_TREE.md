# STARTER KIT DIRECTORY TREE

## Purpose

This document is the canonical file and directory inventory for the
structured AI-assisted development starter kit.

It shows the recommended layout for:

- core project scaffolding
- AI-team scaffolding
- experimental scaffolding
- template library structure

Use this as the single reference for how the starter kit should be
organized on disk.

---

## Canonical project structure

project-root/
  process/
    OPERATING_MODEL.md
    OPERATING_MODEL_AI_TEAM.md
    REVIEWER_AGENT_MODEL.md
    HUMAN_REVIEW_MODEL.md

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
    step_1.3_spec.md

  reviews/
    STEP_REVIEW.md
    PERIODIC_REVIEW.md

  experiments/
    MODEL_EVALUATION.md
    POST_EXPERIMENT_REVIEW.md

  templates/
    core/
      operating_model.template.md
      project_operations_index.template.md
      system_model.template.md
      coding_standards.template.md
      workflow_standards.template.md
      plan.template.md
      progress.template.md
      history.template.md
      step_spec.template.md
      step_review.template.md
      periodic_review.template.md

    ai_team/
      operating_model_ai_team.template.md
      reviewer_agent_model.template.md
      human_review_model.template.md

    experiments/
      model_evaluation.template.md
      post_experiment_review.template.md

---

## Core file set

### `process/`
- `OPERATING_MODEL.md`

### `docs/`
- `PROJECT_OPERATIONS_INDEX.md`
- `SYSTEM_MODEL.md`
- `CODING_STANDARDS.md`
- `WORKFLOW_STANDARDS.md`
- `PLAN.md`
- `PROGRESS.md`
- `HISTORY.md`

### `steps/`
- `step_X.Y_spec.md`

### `reviews/`
- `STEP_REVIEW.md`
- `PERIODIC_REVIEW.md`

---

## AI-team file set

### `process/`
- `OPERATING_MODEL_AI_TEAM.md`
- `REVIEWER_AGENT_MODEL.md`
- `HUMAN_REVIEW_MODEL.md`

Use these when:
- multiple coding agents are active
- reviewer agents are used
- machine-complete vs done matters
- dependency trust levels matter

---

## Experimental file set

### `experiments/`
- `MODEL_EVALUATION.md`
- `POST_EXPERIMENT_REVIEW.md`

Use these when:
- comparing models
- comparing prompts or context packaging
- testing reviewer behavior
- running experimental agent-only cycles
- improving process rather than shipping code

---

## Template library file set

### `templates/core/`
- `operating_model.template.md`
- `project_operations_index.template.md`
- `system_model.template.md`
- `coding_standards.template.md`
- `workflow_standards.template.md`
- `plan.template.md`
- `progress.template.md`
- `history.template.md`
- `step_spec.template.md`
- `step_review.template.md`
- `periodic_review.template.md`

### `templates/ai_team/`
- `operating_model_ai_team.template.md`
- `reviewer_agent_model.template.md`
- `human_review_model.template.md`

### `templates/experiments/`
- `model_evaluation.template.md`
- `post_experiment_review.template.md`

---

## Minimum viable structure

If keeping the system minimal, start with:

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

  reviews/
    STEP_REVIEW.md

---

## Recommended expansion path

### Solo mode
Use:
- core documents
- core templates
- step review

### Small team mode
Add:
- `OPERATING_MODEL_AI_TEAM.md`
- reviewer/human review models
- ownership in `PROGRESS.md`
- periodic review

### Experimental mode
Add:
- experimental documents
- experimental templates
- model comparison runs
- post-experiment reviews

---

## Naming conventions

Use stable, descriptive file names.

Recommended:
- `SYSTEM_MODEL.md`
- `CODING_STANDARDS.md`
- `WORKFLOW_STANDARDS.md`
- `PLAN.md`
- `PROGRESS.md`
- `HISTORY.md`
- `step_1.10_spec.md`

Avoid:
- `notes.md`
- `ideas.md`
- `misc.md`
- ambiguous or overlapping document names

---

## Separation rules

- Live project documents belong in `process/`, `docs/`, `steps/`, `reviews/`, and `experiments/`
- Reusable template documents belong only in `templates/`
- Do not mix templates and live project files in the same directory
- Do not store ad hoc notes in structured directories unless they have a defined role

---

## What this document is not

This document does not define:
- architecture
- code style
- workflow rules
- project planning decisions
- step-level implementation instructions

It defines the canonical structure of the starter kit.
