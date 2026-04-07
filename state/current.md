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
- contributor workflow guidance in `CONTRIBUTING.md`
- one structural decision record in `history/decisions/`

This means the repository is no longer only conceptual. It is usable as a starting point, but it is still early-stage.

## Active Priorities

The next useful improvements are:

1. strengthen clean-session continuity
2. make builder adoption even more direct
3. keep contributor refinement disciplined as the system grows

## Open Questions

The main unresolved questions currently are:

1. Should the repository include copyable template files or a template directory for builders?
2. Should session state remain simple Markdown, or eventually gain a more structured format?
3. What is the minimum example set needed before the scaffold feels concretely applicable?
4. How much orchestration detail belongs in the base scaffold versus project-specific customization?

## Immediate Next Actions

The most reasonable next work items are:

1. add a builder-ready template or starter layout that can be copied into another repository
2. expand examples so at least one shows a slightly more realistic working flow, not just structure
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
