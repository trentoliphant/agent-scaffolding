# Current State

This document captures the active frontier of work for this repository so a new session can resume without reconstructing recent intent from chat history.

## Start Here

If you are resuming work in a clean session, start in this order:

1. Read [open-standard-rewrite-plan.md](open-standard-rewrite-plan.md).
2. Focus first on the `Current Phase`, `Remaining Work`, and `Next Step` sections in that plan.
3. Use this file to confirm repository-level priorities, open questions, and constraints.

## Current Objective

Reframe the repository around an open standard for domain-specific harnesses
or guardrails that can support mixed human and machine agent systems.

## Active Initiative

- active initiative: open-standard rewrite
- active initiative record: [open-standard-rewrite-plan.md](open-standard-rewrite-plan.md)
- most recently completed initiative: starter-kit integration
- completed initiative record: [starter-kit-integration-plan.md](starter-kit-integration-plan.md)
- current focus: redefine the scaffold's scope, modules, and audience path around
  the new standard direction before broad document rewrites

## Current Status

The repository currently has:

- a layered definition of the scaffold in `docs/scaffolding/`
- builder-facing adoption guidance in `docs/guide/`
- concrete examples in `docs/examples/`
- a lightweight reference layer in `docs/reference/`
- a local reference copy of `starter_kit` plus a reduced derived example
- an initial `templates/core/` starter set imported from the reference source
- `periodic_review.template.md` added to the base core template set
- first-class trace, verification, and self-evolution definitions in
  `docs/scaffolding/`
- explicit guidance for where self-evolution outputs belong across session
  state, durable documents, history, and decisions
- AI-team templates explicitly kept as an advanced extension
- experiment templates explicitly kept as a specialized extension
- the current imported starter set explicitly treated as the default builder path
- contributor workflow guidance in `CONTRIBUTING.md`
- structural decision records in `history/decisions/`

However, the repository's current shape still reflects an earlier center of
gravity:

- a coding-oriented starting point
- strong influence from the imported `starter_kit` reference
- limited treatment of modular domain harnesses
- limited treatment of mixed human and machine role assignment
- incomplete treatment of expertise tiers, autonomy, and review boundaries

This means the repository is usable, but it is no longer aligned cleanly with
the intended direction.

## Immediate Task

The next task to work on is:

1. clarify how expertise tiers map to responsibility, autonomy, and review

## Active Priorities

The next useful improvements are:

1. clarify the standard's purpose, scope, and modular boundaries
2. define how roles, autonomy levels, and verification work across mixed human
   and machine systems
3. add first-class concepts for traces and scaffold self-evolution
4. keep the user or builder path primary while making contributor standards
   explicit
5. decide how the open standard relates structurally to proprietary or
   third-party domain implementations

## Open Questions

The main unresolved questions currently are:

1. What is the smallest complete version of the open standard that should work
   for builders without reference to proprietary domain material?
2. Which modules belong in the standard core versus optional extensions?
3. How should expertise levels such as junior, regular, and senior be
   represented without tying them to one company-specific commercial model?
4. What trace format is minimal, reusable, and execution-system-agnostic?
5. Should the standard and the baseline implementation live in this repository
   together, or should they later separate from domain implementations into
   multiple repositories?
6. Which existing materials should be preserved as reference or migration aids
   rather than rewritten into the new standard directly?

## Immediate Next Actions

The most reasonable next work items are:

1. clarify how expertise tiers map to responsibility, autonomy, and review
2. decide whether the current standard description is now complete enough to
   support a cleaner baseline implementation pass

## Known Constraints

- Keep system definition separate from application guidance
- Do not let state documents become substitutes for decisions or principles
- Prefer small, durable refinements over broad rewrites
- Preserve builder usability as the primary measure of success for the scaffold itself
- Keep the standard model-agnostic and execution-system-agnostic
- Do not let company-specific proprietary needs silently redefine the open
  standard without an explicit decision
- Preserve a clean distinction between the open standard and domain-specific
  implementations built on top of it

## Update Rule

Update this file when:

- the active objective changes
- priorities change
- the main open questions change
- the next most likely work items change

Do not use this file to store durable rationale that belongs in `history/decisions/`.
