# Current State

This document captures the active frontier of work for this repository so a new session can resume without reconstructing recent intent from chat history.

## Start Here

If you are resuming work in a clean session, start in this order:

1. Read [starter-kit-integration-plan.md](starter-kit-integration-plan.md).
2. Focus first on the `Current Phase`, `Remaining Work`, and `Next Step` sections in that plan.
3. Use this file to confirm repository-level priorities, open questions, and constraints.

## Current Objective

Make the repository strong as both:

- the source of truth for the scaffold itself
- a practical starting point for builders adopting that scaffold

## Active Initiative

- active initiative: none
- most recently completed initiative: starter-kit integration
- completed initiative record: [starter-kit-integration-plan.md](starter-kit-integration-plan.md)
- current focus: maintain the established baseline and only expand it when a concrete builder need appears

## Current Status

The repository now has:

- a layered definition of the scaffold in `docs/scaffolding/`
- builder-facing adoption guidance in `docs/guide/`
- concrete examples in `docs/examples/`
- a lightweight reference layer in `docs/reference/`
- a local reference copy of `starter_kit` plus a reduced derived example
- an initial `templates/core/` starter set imported from the reference source
- `periodic_review.template.md` added to the base core template set
- AI-team templates explicitly kept as an advanced extension
- experiment templates explicitly kept as a specialized extension
- the current imported starter set explicitly treated as the default builder path
- contributor workflow guidance in `CONTRIBUTING.md`
- structural decision records in `history/decisions/`

This means the repository is no longer only conceptual. It is usable as a starting point, but it is still early-stage.

## Immediate Task

The next task to work on is:

1. shift active attention from starter-kit integration to the next meaningful repository refinement when one is identified

Until a concrete new need appears, the current starter set should be treated as the stable baseline and the integration work should be treated as complete.

## Active Priorities

The next useful improvements are:

1. maintain the current starter baseline unless a stronger builder need appears
2. make builder adoption even more direct where gaps are discovered
3. keep contributor refinement disciplined as the system grows

## Open Questions

The main unresolved questions currently are:

1. Which starter-kit materials should become templates here versus remain example material?
2. What concrete future builder need, if any, would justify expanding the default starter set?
3. Which parts of `starter_kit` should be treated as reference material only, rather than imported?
4. How much orchestration detail belongs in the base scaffold versus project-specific customization?

## Immediate Next Actions

The most reasonable next work items are:

1. treat the current imported starter set as the stable default path unless a stronger builder need appears
2. record any later change to that baseline as a deliberate decision
3. identify the next repository refinement thread only when there is a concrete problem to solve

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
