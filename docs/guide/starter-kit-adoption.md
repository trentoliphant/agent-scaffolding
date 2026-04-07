# Starter Kit Adoption

This guide explains how the `starter_kit` reference implementation relates to this scaffold and how to use it without confusing reference material, examples, and copyable assets.

## Purpose

Use this guide when you want to:

- understand how the `starter_kit` reference informs the scaffold
- decide what to read first
- choose between the full reference, the reduced example, and the imported templates

## Use The Right Layer

Use the reference source when you need:

- the full original file set
- the original naming and structure
- the richest source for extracting patterns

Use the derived example when you need:

- a smaller teaching-oriented view of the same workflow shape
- a quick way to understand the main documents and their relationships

Use the imported templates when you need:

- copyable starter assets for a real project
- a shorter path from scaffold understanding to practical adoption

## Current Sources

- Full reference source: [../reference/starter_kit](../reference/starter_kit)
- Reduced derived example: [../examples/structured-project-starter/README.md](../examples/structured-project-starter/README.md)
- Imported core templates: [../../templates/core](/Volumes/Home/Users/trentoliphant/Development/personal/agent-scaffolding/templates/core)

## Recommended Builder Path

1. Read [start-here.md](start-here.md).
2. Read [../examples/structured-project-starter/README.md](../examples/structured-project-starter/README.md).
3. Copy from [../../templates/core](/Volumes/Home/Users/trentoliphant/Development/personal/agent-scaffolding/templates/core) if you want a working project starter.
4. Consult [../reference/starter_kit](../reference/starter_kit) when you need the full source context or want to extract more patterns.

## Concept Mapping

The table below shows how scaffold concepts connect to the full reference source and the reduced example.

| Scaffold concept | Reference source | Derived example |
|---|---|---|
| Orchestration and execution rules | `process/OPERATING_MODEL.md` | `process/OPERATING_MODEL.md` |
| Project orientation | `docs/PROJECT_OPERATIONS_INDEX.md` | `docs/PROJECT_OPERATIONS_INDEX.md` |
| Project-level system definition | `templates/core/system_model.template.md` and project `docs/SYSTEM_MODEL.md` | `docs/SYSTEM_MODEL.md` |
| Task sequencing | `templates/core/plan.template.md` and project `docs/PLAN.md` | `docs/PLAN.md` |
| Current execution state | `templates/core/progress.template.md` and project `docs/PROGRESS.md` | `docs/PROGRESS.md` |
| Preserved learning | `templates/core/history.template.md` and project `docs/HISTORY.md` | `docs/HISTORY.md` |
| Unit-of-work contract | `templates/core/step_spec.template.md` and project `steps/step_X.Y_spec.md` | `steps/step_1.1_spec.md` |
| Structured review | `templates/core/step_review.template.md` and project `reviews/STEP_REVIEW.md` | `reviews/STEP_REVIEW.md` |
| Coding conventions | `templates/core/coding_standards.template.md` and project `docs/CODING_STANDARDS.md` | omitted in the reduced example |
| Workflow conventions | `templates/core/workflow_standards.template.md` and project `docs/WORKFLOW_STANDARDS.md` | omitted in the reduced example |

## Minimal Copyable Template Set

The current imported template set is:

- `templates/core/system_model.template.md`
- `templates/core/plan.template.md`
- `templates/core/progress.template.md`
- `templates/core/history.template.md`
- `templates/core/step_spec.template.md`
- `templates/core/step_review.template.md`
- `templates/core/coding_standards.template.md`
- `templates/core/workflow_standards.template.md`

This set is intentionally smaller than the full reference source.

## Adoption Rule

Start from the templates when possible.

Move to the reduced example when you need help understanding the workflow shape.

Move to the full reference source when:

- you need the fuller document set
- you want AI-team or experimental extensions later
- you are extracting new scaffold patterns rather than just adopting the current starter
