# STARTER KIT MANIFEST

> Status: Reference/Migration
> Alignment: Preserved as a reference source, not aligned as current standard core
> Intended role: extraction source and migration aid
> Use it for: learning from older patterns or migrating older workflows

## Purpose

This document defines the standard scaffolding set for a structured,
AI-assisted development project.

It lists the core documents, their purpose, where they belong, and whether
they are typically:
- copied from a template
- created per project
- maintained during execution
- used only in special modes

This manifest is the quick reference for assembling a new project starter kit.

---

## Directory structure

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

  reviews/
    STEP_REVIEW.md
    PERIODIC_REVIEW.md

  experiments/
    MODEL_EVALUATION.md
    POST_EXPERIMENT_REVIEW.md

---

## Core document set

| Document | Location | Role | Template? | Required? |
|----------|----------|------|-----------|-----------|
| OPERATING_MODEL.md | process/ | Process governance and execution rules | Yes | Yes |
| PROJECT_OPERATIONS_INDEX.md | docs/ | Orientation and navigation | Yes | Yes |
| SYSTEM_MODEL.md | docs/ | Architecture, invariants, responsibilities | Yes | Yes |
| CODING_STANDARDS.md | docs/ | Code-writing conventions | Yes | Yes |
| WORKFLOW_STANDARDS.md | docs/ | Git/repo/process conventions | Yes | Yes |
| PLAN.md | docs/ | Phases, sequencing, step structure | Yes | Yes |
| PROGRESS.md | docs/ | Current execution state | Yes | Yes |
| HISTORY.md | docs/ | Meaningful discoveries and learning | Yes | Yes |
| step_X.Y_spec.md | steps/ | One-step execution contract | Yes | Yes |
| STEP_REVIEW.md | reviews/ | Step completion quality gate | Yes | Yes |
| PERIODIC_REVIEW.md | reviews/ | Recurring pattern review | Yes | Recommended |

---

## Optional AI-team document set

| Document | Location | Role | Template? | Required? |
|----------|----------|------|-----------|-----------|
| OPERATING_MODEL_AI_TEAM.md | process/ | Multi-agent execution governance | Yes | Optional |
| REVIEWER_AGENT_MODEL.md | process/ | Reviewer-agent role definition and rubric | Yes | Optional |
| HUMAN_REVIEW_MODEL.md | process/ | Human review role definition and rubric | Yes | Optional |

---

## Optional experimental document set

| Document | Location | Role | Template? | Required? |
|----------|----------|------|-----------|-----------|
| MODEL_EVALUATION.md | experiments/ | Structured comparison of models/configurations | Yes | Optional |
| POST_EXPERIMENT_REVIEW.md | experiments/ | Extract process improvements from experiments | Yes | Optional |

---

## Starter kit initialization order

1. Create directory structure
2. Add OPERATING_MODEL.md
3. Add PROJECT_OPERATIONS_INDEX.md
4. Create SYSTEM_MODEL.md
5. Create CODING_STANDARDS.md
6. Create WORKFLOW_STANDARDS.md
7. Create PLAN.md
8. Initialize PROGRESS.md
9. Initialize HISTORY.md
10. Add review documents
11. Create first step_X.Y_spec.md

If using AI-team mode:
12. Add OPERATING_MODEL_AI_TEAM.md
13. Add reviewer/human review models

If using experimental mode:
14. Add experiment documents

---

## Minimum viable starter kit

- OPERATING_MODEL.md
- PROJECT_OPERATIONS_INDEX.md
- SYSTEM_MODEL.md
- CODING_STANDARDS.md
- WORKFLOW_STANDARDS.md
- PLAN.md
- PROGRESS.md
- HISTORY.md
- step_X.Y_spec.md
- STEP_REVIEW.md

---

## Recommended template library

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

## What this manifest is not

This document does not define:
- architecture
- code style
- workflow rules
- project plan content
- step implementation details

It is the assembly guide for the scaffolding system.
