# Templates

This directory contains baseline implementation assets for projects adopting
the standard.

Templates are useful because they shorten the path from understanding the
standard to trying it in a real project.

They are not the standard itself.

## What Templates Are For

Use these templates when you want:

- a practical starting point
- a small document set you can copy and adapt
- baseline implementation structure without inventing every file from scratch

Use [../docs/guide/baseline-implementation.md](../docs/guide/baseline-implementation.md)
when you want the explicit boundary between these implementation assets and the
standard core.

## What Templates Are Not

Templates are not:

- the open standard definition
- a required file set for every project
- a complete set of domain modules
- a substitute for understanding the standard's boundaries

## Current Template Layer

The current `core/` set should be understood as a baseline implementation kit.

The smallest domain-neutral subset is:

- `system_model.template.md`
- `plan.template.md`
- `progress.template.md`
- `history.template.md`

Additional templates are available when the implementation needs more
structure:

- `step_spec.template.md` for a fuller unit-of-work contract
- `verification_contract.template.md` for defining one reusable verification
  contract
- `step_review.template.md` for a fuller verification record
- `periodic_review.template.md` for the self-evolution loop
- `workflow_standards.template.md` for local promotion and repository workflow
- `coding_standards.template.md` for coding-focused implementations

That is acceptable as long as:

- the templates are clearly treated as implementation assets
- the standard remains defined in `docs/scaffolding/`
- coding-specific templates are not treated as required for non-coding domains

## Baseline Template Classification

For the current baseline path, classify the `core/` templates as follows:

| Template | Baseline status | Why |
|---|---|---|
| `system_model.template.md` | Keep | Gives the local harness a clear purpose, boundaries, roles, and verification or trace expectations. |
| `plan.template.md` | Keep | Gives builders a simple task or phase map without requiring a specific runtime. |
| `progress.template.md` | Keep | Provides lightweight session state and task-cycle visibility. |
| `history.template.md` | Keep | Preserves durable observations and follow-ups when a full decision record would be too heavy. |
| `step_spec.template.md` | Keep | Defines a portable unit-of-work contract with role, verification, and trace expectations. |
| `verification_contract.template.md` | Keep | Gives builders a compact reusable way to define one local verification contract before it is applied in reviews. |
| `step_review.template.md` | Keep | Maps older review language onto the current verification-record model. |
| `periodic_review.template.md` | Keep | Supports the self-evolution loop by turning repeated trace and verification evidence into reviewed proposals. |
| `workflow_standards.template.md` | Keep | Provides optional local promotion and repository workflow rules without making them standard core. |
| `coding_standards.template.md` | Defer | Keep available for coding implementations, but do not include it in the smallest domain-neutral baseline. |

This classification is about the baseline starting path, not file validity.
Deferred templates may still be the right choice for a specific domain
implementation.

## How To Use Templates

Use templates as follows:

1. Start from the smallest subset that helps your project.
2. Rename or trim files to fit your local implementation.
3. Add domain modules, expertise profiles, or runtime integration guidance only
   when needed.
4. Add reusable verification-contract definitions when local review criteria
   would otherwise be reconstructed repeatedly from prose.
5. Do not assume every template belongs in every project.

Use [../docs/guide/domain-implementation-extensions.md](../docs/guide/domain-implementation-extensions.md)
when you need to add domain-specific modules around the templates.

Use [../docs/guide/execution-system-integration.md](../docs/guide/execution-system-integration.md)
when the templates need to be connected to a specific runtime.

## Template Design Rules

When revising or adding templates:

- prefer domain-neutral wording where possible
- keep the baseline useful for mixed human and machine systems
- preserve compatibility with coding workflows without making coding the only
  implied use case
- keep the templates smaller than the full reference source unless a stronger
  builder need appears
- record meaningful template strategy changes in `history/decisions/`

## Current Note

The template layer is now aligned around a practical baseline path, but it is
still an implementation kit rather than the standard itself.

Treat `coding_standards.template.md` as a coding-focused extension.
Use it when the project produces code, and replace it with domain-specific
production standards when the project does not.
