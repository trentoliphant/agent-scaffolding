# Current State

This document captures the active frontier of work for this repository so a new session can resume without reconstructing recent intent from chat history.

## Start Here

If you are resuming work in a clean session, start in this order:

1. Read [open-standard-rewrite-plan.md](open-standard-rewrite-plan.md).
2. Focus first on the `Current Phase`, `Remaining Work`, and `Next Step` sections in that plan.
3. Use this file to confirm repository-level priorities, open questions, and constraints.
4. Use [research-model-extraction-review.md](research-model-extraction-review.md)
   when evaluating whether `research_model/` should yield a guide or template.
5. Use [investigative-step-template-evaluation.md](investigative-step-template-evaluation.md)
   when evaluating whether research-heavy work now needs a template variant.
6. Use [example-set-gap-review.md](example-set-gap-review.md) when deciding
   whether the completed example set implies a reusable extraction.

## Current Objective

Reframe the repository around an open standard for domain-specific harnesses
or guardrails that can support mixed human and machine agent systems.

## Active Initiative

- active initiative: open-standard rewrite
- active initiative record: [open-standard-rewrite-plan.md](open-standard-rewrite-plan.md)
- most recently completed initiative: starter-kit integration
- completed initiative record: [starter-kit-integration-plan.md](starter-kit-integration-plan.md)
- current focus: first promoted domain extension pattern

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
- explicit modeling of expertise tiers as optional autonomy or expertise
  profiles rather than roles or verification contracts
- a readiness decision that the current standard description is complete
  enough for a cleaner baseline implementation pass
- baseline implementation guidance, the minimal adoption guide, the minimal
  example, and the template index aligned around the same starting shape
- `periodic_review` and `workflow_standards` templates revised against the
  current standard framing
- `coding_standards` explicitly deferred from the smallest domain-neutral
  baseline while remaining available for coding implementations
- the baseline guide, minimal adoption guide, minimal example, template index,
  start-here guide, and repository-status guide checked as one coherent
  builder path
- the software-project example refreshed as a coding-focused scaling example
  aligned with the current baseline path
- roadmap refreshed around remaining post-baseline-alignment work
- an execution-system integration guide added to map the standard onto real
  runtimes without making them part of the standard core
- a domain implementation extension guide added to help builders specialize
  the harness without redefining the standard core
- the research-to-design example promoted as the first current
  domain-extension pattern for builders
- a decision recorded to keep promoted extension examples few and
  non-overlapping
- a curated example set completed across minimal, coding-focused,
  research-to-design, regulated-approval, and expertise-tiered patterns
- a decision recorded to treat `design_model/` and `research_model/` as
  extraction sources rather than near-term promoted examples
- a focused extraction review recorded for `research_model/`
- domain extension guidance strengthened with a compact research-heavy-domain
  note on evidence discipline, open questions, and exploratory plan mutation
- an evaluation recorded that an investigative-step template note is not yet
  justified
- a gap review recorded that the strongest repeated optional artifact shape is
  a verification-contract definition artifact
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
- open structural questions about repository boundaries and which reusable
  extension patterns deserve promotion beyond the guide layer

This means the repository is usable, the baseline path is now coherent, and
the next builder-facing frontier is underway.

## Immediate Task

The next task to work on is:

1. use the first promoted domain-extension pattern to decide what reusable
   extension artifact should come next

## Active Priorities

The next useful improvements are:

1. evaluate which additional extension patterns deserve examples, templates, or
   decision records next
2. decide whether the completed example set suggests a guide, template, or
   decision gap
3. extract reusable material from incubating sources only when the current
   example set reveals a real gap
4. keep the user or builder path primary while making contributor standards
   explicit
5. decide how the open standard relates structurally to proprietary or
   third-party domain implementations

## Open Questions

The main unresolved questions currently are:

1. Which extension patterns should remain guide-only, and which now deserve
   templates or decision records after the curated example set is in place?
2. Should the standard and the baseline implementation live in this repository
   together, or should they later separate from domain implementations into
   multiple repositories?
3. Which existing materials should be preserved as reference or migration aids
   rather than rewritten into the new standard directly?

## Immediate Next Actions

The most reasonable next work items are:

1. review whether any current example exposes a reusable template need
2. review whether any example exposes a missing guide or decision record
3. review `design_model/` and `research_model/` only for selective extraction
   candidates that fill uncovered builder needs
4. wait for repeated builder pressure before adding any investigative-step
   template appendix or variant
5. decide whether to extract an optional verification-contract template as the
   next reusable artifact

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
