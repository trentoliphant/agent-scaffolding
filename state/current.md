# Current State

This document captures the active frontier of work for this repository so a new session can resume without reconstructing recent intent from chat history.

## Current Objective

Make the repository strong as both:

- the source of truth for the scaffold itself
- a practical starting point for builders adopting that scaffold

## Current Status

The repository now has:

- a layered definition of the scaffold in `docs/scaffolding/`
- builder-facing adoption guidance in `docs/guide/`
- concrete examples in `docs/examples/`
- a lightweight reference layer in `docs/reference/`
- a local reference copy of `starter_kit` plus a reduced derived example
- an initial `templates/core/` starter set imported from the reference source
- contributor workflow guidance in `CONTRIBUTING.md`
- structural decision records in `history/decisions/`

This means the repository is no longer only conceptual. It is usable as a starting point, but it is still early-stage.

## Active Priorities

The next useful improvements are:

1. integrate the external starter kit into this scaffold cleanly
2. make builder adoption even more direct
3. keep contributor refinement disciplined as the system grows

## Open Questions

The main unresolved questions currently are:

1. Which starter-kit materials should become templates here versus remain example material?
2. What is the minimal copyable template set that gives builders immediate value?
3. Which parts of `starter_kit` should be treated as reference material only, rather than imported?
4. How much orchestration detail belongs in the base scaffold versus project-specific customization?

## Immediate Next Actions

The most reasonable next work items are:

1. decide whether to import periodic review, AI-team, and experiment templates next
2. review whether the imported core templates need renaming or adaptation to fit this repo's terminology more cleanly
3. add another decision record when a substantive interpretation or scope choice is made

## Known Constraints

- Keep system definition separate from application guidance
- Do not let state documents become substitutes for decisions or principles
- Prefer small, durable refinements over broad rewrites
- Preserve builder usability as the primary measure of success for the scaffold itself

## Update Rule

Update this file when:

- the active objective changes
- priorities change
- the main open questions change
- the next most likely work items change

Do not use this file to store durable rationale that belongs in `history/decisions/`.
