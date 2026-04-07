# Starter Kit Integration Plan

This document defines how the external `starter_kit` materials should relate to and be integrated into this repository.

It is an execution plan for repository evolution, not part of the scaffold definition itself.

## Goal

Use the `starter_kit` materials to make this repository more directly usable for builders without collapsing the distinction between:

- scaffold definition
- usage guidance
- examples
- reference implementations and extraction sources
- copyable starter assets

## Source Being Mapped

This plan now works from the local reference copy in:

- `docs/reference/starter_kit/`

The original external source remains:

- `/Volumes/Home/Users/trentoliphant/Development/starter_kit`

Those materials define a concrete, opinionated project document system. The goal is not to collapse that system into the scaffold. The goal is to place what we learn from it into the correct layer of this repository while preserving the reference source.

## Core Interpretation

The `starter_kit` is best understood as a working reference implementation and extraction source that also functions as a usable starter package. It is not the scaffold definition itself.

That means:

- reusable concepts may influence `docs/scaffolding/`
- builder-facing adoption patterns belong in `docs/guide/`
- illustrative material derived from it may appear in `docs/examples/`
- its status as a real working source should be named in `docs/reference/`
- copyable assets belong in a future `templates/` directory

Operational rule:

- keep the reference source intact in `docs/reference/`
- create reduced examples only when simplification adds teaching value

## Integration Categories

### 1. Keep as scaffold definition only if the concept is cross-project

Only promote material into `docs/scaffolding/` when it expresses a durable, reusable concept such as:

- orchestration logic
- task and review boundaries
- state vs history separation
- role distinctions

Candidate source documents:

- `process/OPERATING_MODEL.md`
- `templates/ai_team/operating_model_ai_team.template.md`
- `templates/ai_team/reviewer_agent_model.template.md`
- `templates/ai_team/human_review_model.template.md`

Promotion rule:

- extract concepts, not project-file prescriptions

### 2. Convert builder-facing assembly guidance into guide material

Documents that explain what files to create, how to initialize them, and how to adopt them belong primarily in `docs/guide/`.

Candidate source documents:

- `STARTER_KIT_MANIFEST.md`
- `STARTER_KIT_FILE_SET.md`
- `STARTER_KIT_FILE_INVENTORY.md`
- `STARTER_KIT_DIRECTORY_TREE.md`

Planned outputs in this repository:

- `docs/guide/starter-kit-adoption.md`
- updates to `docs/guide/minimal-adoption.md`
- updates to `docs/guide/customizing.md`

### 3. Represent the starter kit as a reference implementation first, and as example material only where helpful

The starter kit should appear in this repository as a named reference implementation and extraction source. Example material derived from it may also be created where that helps builders understand the scaffold.

Candidate source materials:

- `docs/PROJECT_OPERATIONS_INDEX.md`
- `process/OPERATING_MODEL.md`
- the overall file set and directory tree

Planned outputs in this repository:

- `docs/reference/README.md` and `docs/reference/starter_kit/`
- `docs/examples/structured-project-starter/README.md`
- a mapping table from scaffold concepts to starter-kit files

### 4. Create copyable templates as reusable starter assets

The templates are the most direct builder-facing value in the external repository and should become a first-class part of this repository.

Candidate source materials:

- `templates/core/*.template.md`
- `templates/ai_team/*.template.md`
- `templates/experiments/*.template.md`

Planned outputs in this repository:

- `templates/core/`
- `templates/ai-team/`
- `templates/experiments/`
- a short template usage guide

Adaptation rule:

- keep them copyable
- align names and structure with this repository's layer model
- avoid importing redundant files without explaining their purpose

## File Mapping

The following mapping should guide future import work.

| Starter kit source | Best fit in this repository | Notes |
|---|---|---|
| `STARTER_KIT_MANIFEST.md` | `docs/guide/` | Builder assembly guidance |
| `STARTER_KIT_FILE_SET.md` | `docs/guide/` or example appendix | Compact builder reference |
| `STARTER_KIT_FILE_INVENTORY.md` | `docs/guide/` | Builder reference and onboarding |
| `STARTER_KIT_DIRECTORY_TREE.md` | `docs/reference/`, `docs/examples/`, and template docs | Reference layout with example value |
| `process/OPERATING_MODEL.md` | `docs/reference/` plus selective conceptual extraction | Mostly an application-level orchestration document |
| `docs/PROJECT_OPERATIONS_INDEX.md` | `docs/reference/`, `docs/examples/`, and future template | Strong example of project orientation |
| `templates/core/system_model.template.md` | `templates/core/` | Direct template candidate |
| `templates/core/plan.template.md` | `templates/core/` | Direct template candidate |
| `templates/core/progress.template.md` | `templates/core/` | Direct template candidate |
| `templates/core/history.template.md` | `templates/core/` | Direct template candidate |
| `templates/core/step_spec.template.md` | `templates/core/` | Direct template candidate |
| `templates/core/step_review.template.md` | `templates/core/` | Direct template candidate |
| `templates/core/periodic_review.template.md` | `templates/core/` | Direct template candidate |
| `templates/core/coding_standards.template.md` | `templates/core/` | Direct template candidate |
| `templates/core/workflow_standards.template.md` | `templates/core/` | Direct template candidate |
| `templates/ai_team/*.template.md` | `templates/ai-team/` and advanced example docs | Optional role/review extension |
| `templates/experiments/*.template.md` | `templates/experiments/` | Optional experimentation extension |

## Proposed Work Sequence

### Phase 1. Explain the relationship

Create the repository-level documents that explain how the starter kit fits into the scaffold.

Deliverables:

- `docs/reference/README.md`
- `docs/reference/starter_kit/`
- `docs/guide/starter-kit-adoption.md`
- `docs/examples/structured-project-starter/README.md`
- updates to `README.md` and relevant guide pages

Current status:

- `docs/reference/README.md` is complete
- `docs/reference/starter_kit/` is complete
- `docs/examples/structured-project-starter/README.md` is complete
- `docs/guide/starter-kit-adoption.md` is complete

### Phase 2. Import the minimal reusable template set

Create a `templates/` directory in this repository with the most useful core templates first.

Priority templates:

1. `system_model`
2. `plan`
3. `progress`
4. `history`
5. `step_spec`
6. `step_review`
7. `coding_standards`
8. `workflow_standards`

Current status:

- `templates/core/` now contains this initial minimal template set

### Phase 3. Import advanced modes

Add optional templates and examples for:

- AI-team mode
- periodic review
- experiments

These should remain clearly optional.

### Phase 4. Reconcile terminology and structure

After import, review whether:

- this repository's concepts and the template names align cleanly
- any starter-kit terms should be generalized
- any guide pages need cross-links or clarifications

### Phase 5. Record durable choices

When the repository commits to a template strategy or to the starter kit as a canonical example, record that in `history/decisions/`.

## Constraints

- Do not turn this repository into only a copy of `starter_kit`
- Do not promote application-specific file structure directly into scaffold definition
- Do not import templates without explaining when builders should use them
- Keep the minimal path small even if advanced modes are available
- Preserve the distinction between current state, durable decisions, and scaffold definition

## Immediate Recommendation

The best next implementation step is:

1. decide whether to import periodic review, AI-team, and experiment templates next
2. review the imported core templates for terminology alignment
3. record any durable template-strategy decision in `history/decisions/`

That sequence gives builders immediate value while keeping the repository architecture clean.
