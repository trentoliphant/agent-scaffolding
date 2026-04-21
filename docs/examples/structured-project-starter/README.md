# Structured Project Starter

This example is a reduced, teaching-oriented version of the patterns visible in
the `starter_kit` reference implementation.

It is not a full copy of the reference source. It exists to show one richer,
document-structured implementation pattern that informed earlier phases of this
repository.

## Derived From

- reference source: [../../reference/starter_kit](../../reference/starter_kit)

## What This Example Is For

Use this example when you want to understand the pattern of:

- a process document defining execution rules
- a small set of project truth documents
- step-by-step execution contracts
- explicit verification or review documents
- tracked progress and preserved history

This example is best treated as a reference-shaped implementation example, not
as the default baseline for the current standard.

## Minimal Example Shape

```text
project-root/
  process/
    OPERATING_MODEL.md
  docs/
    PROJECT_OPERATIONS_INDEX.md
    SYSTEM_MODEL.md
    PLAN.md
    PROGRESS.md
    HISTORY.md
  steps/
    step_1.1_spec.md
  reviews/
    STEP_REVIEW.md
```

## Why This Is An Example Rather Than A Reference

The full reference source includes:

- more inventory and manifest material
- more template coverage
- optional AI-team documents
- experimental documents
- historical `v1` material

This example leaves those out on purpose so the core workflow is easier to see.

## Relationship To The Reference Source

Use the reference source when you need:

- the full file set
- the original naming and structure
- the source material used for scaffold extraction

Use this example when you need:

- the smallest understandable illustration of that pattern
- a builder-facing explanation of the workflow shape
- a less opinionated teaching artifact
- a migration aid from older coding-oriented scaffold material

## Key Mapping

- `process/OPERATING_MODEL.md` shows orchestration and execution rules
- `docs/SYSTEM_MODEL.md` shows system definition at the project level
- `docs/PLAN.md` shows task sequencing
- `docs/PROGRESS.md` shows current state
- `docs/HISTORY.md` shows preserved learning
- `steps/step_1.1_spec.md` shows the unit-of-work contract
- `reviews/STEP_REVIEW.md` shows verification or review as a separate concern
