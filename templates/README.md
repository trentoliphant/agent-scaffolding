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

It includes assets such as:

- local system or harness definition
- planning and progress tracking
- unit-of-work specification
- verification record structure
- history and periodic review
- workflow and coding standards where those are useful for the implementation

Some of these templates reflect earlier coding-oriented phases of the
repository more strongly than others.

That is acceptable during the rewrite as long as:

- the templates are clearly treated as implementation assets
- the standard remains defined in `docs/scaffolding/`
- template evolution remains visible and deliberate

## How To Use Templates

Use templates as follows:

1. Start from the smallest subset that helps your project.
2. Rename or trim files to fit your local implementation.
3. Add domain modules, expertise profiles, or runtime integration guidance only
   when needed.
4. Do not assume every template belongs in every project.

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

The template layer is still being rewritten to align with the open-standard
framing.

For now, treat it as a practical baseline kit in transition rather than a
finished canonical implementation.
