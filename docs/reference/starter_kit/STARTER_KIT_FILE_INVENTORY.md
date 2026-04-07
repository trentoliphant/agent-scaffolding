# STARTER KIT FILE INVENTORY

## Purpose

This document provides a concise inventory of the starter kit files,
their roles, and when they are used.

Use it as a quick reference when assembling a new project or checking
whether a project has the full scaffolding set in place.

---

## Core files

| File | Role | Required |
|------|------|----------|
| `process/OPERATING_MODEL.md` | Process governance and execution rules | Yes |
| `docs/PROJECT_OPERATIONS_INDEX.md` | Orientation and navigation | Yes |
| `docs/SYSTEM_MODEL.md` | Architecture and invariants | Yes |
| `docs/CODING_STANDARDS.md` | Coding conventions | Yes |
| `docs/WORKFLOW_STANDARDS.md` | Git/repo/workflow conventions | Yes |
| `docs/PLAN.md` | Phases and sequencing | Yes |
| `docs/PROGRESS.md` | Current state tracking | Yes |
| `docs/HISTORY.md` | Meaningful discoveries and lessons | Yes |
| `steps/step_X.Y_spec.md` | Single-step execution contract | Yes |
| `reviews/STEP_REVIEW.md` | Step completion quality gate | Yes |
| `reviews/PERIODIC_REVIEW.md` | Multi-step pattern review | Recommended |

---

## AI-team files

| File | Role | Required |
|------|------|----------|
| `process/OPERATING_MODEL_AI_TEAM.md` | Multi-agent operating model | Optional |
| `process/REVIEWER_AGENT_MODEL.md` | Reviewer-agent rubric and role definition | Optional |
| `process/HUMAN_REVIEW_MODEL.md` | Human review rubric and trust-boundary review | Optional |

Use when:
- multiple agents work in distinct roles
- machine-complete vs done matters
- human trust checkpoints are explicit

---

## Experimental files

| File | Role | Required |
|------|------|----------|
| `experiments/MODEL_EVALUATION.md` | Controlled comparison of models/configurations | Optional |
| `experiments/POST_EXPERIMENT_REVIEW.md` | Improvement extraction from experiments | Optional |

Use when:
- comparing model behavior
- testing alternate prompts or contexts
- running agent-only experimental cycles
- improving the process itself

---

## Core template inventory

| Template | Purpose |
|----------|---------|
| `templates/core/operating_model.template.md` | Base operating model |
| `templates/core/project_operations_index.template.md` | Navigation/orientation guide |
| `templates/core/system_model.template.md` | Architecture/system model template |
| `templates/core/coding_standards.template.md` | Coding standards template |
| `templates/core/workflow_standards.template.md` | Workflow standards template |
| `templates/core/plan.template.md` | Development plan template |
| `templates/core/progress.template.md` | Progress tracker template |
| `templates/core/history.template.md` | History/log template |
| `templates/core/step_spec.template.md` | Step specification template |
| `templates/core/step_review.template.md` | Step review checklist template |
| `templates/core/periodic_review.template.md` | Periodic review template |

---

## AI-team template inventory

| Template | Purpose |
|----------|---------|
| `templates/ai_team/operating_model_ai_team.template.md` | Multi-agent operating model template |
| `templates/ai_team/reviewer_agent_model.template.md` | Reviewer-agent model template |
| `templates/ai_team/human_review_model.template.md` | Human-review model template |

---

## Experimental template inventory

| Template | Purpose |
|----------|---------|
| `templates/experiments/model_evaluation.template.md` | Model evaluation template |
| `templates/experiments/post_experiment_review.template.md` | Post-experiment review template |

---

## Minimum viable starter kit

A project can begin with only these files:

- `process/OPERATING_MODEL.md`
- `docs/PROJECT_OPERATIONS_INDEX.md`
- `docs/SYSTEM_MODEL.md`
- `docs/CODING_STANDARDS.md`
- `docs/WORKFLOW_STANDARDS.md`
- `docs/PLAN.md`
- `docs/PROGRESS.md`
- `docs/HISTORY.md`
- `steps/step_X.Y_spec.md`
- `reviews/STEP_REVIEW.md`

Everything else can be added as the project grows.

---

## Recommended adoption order

1. Core files
2. Core templates
3. Periodic review
4. AI-team files
5. Experimental files

---

## What this document is not

This document does not define how the files should be written.
It only identifies what the file set contains and what each file is for.
