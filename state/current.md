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
6. Use [example-set-gap-review.md](example-set-gap-review.md) for the
   pre-extraction rationale that led to the optional
   `verification_contract` template.
7. Use [post-verification-example-set-review.md](post-verification-example-set-review.md)
   when deciding whether any further reusable extraction is justified now.
8. Use [material-status-review.md](material-status-review.md) when deciding
   whether repository classifications need further rework before boundary
   decisions.
9. Use [repository-boundary-review.md](repository-boundary-review.md) for the
   option comparison that led to the current one-repo decision.
10. Use [release-versioning-review.md](release-versioning-review.md) for the
    option comparison that led to the current narrative-versioning decision.
11. Use [reference-retention-review.md](reference-retention-review.md) for the
    option comparison that led to the current retained reference-layer set.

## Current Objective

Reframe the repository around an open standard for domain-specific harnesses
or guardrails that can support mixed human and machine agent systems.

## Active Initiative

- active initiative: open-standard rewrite
- active initiative record: [open-standard-rewrite-plan.md](open-standard-rewrite-plan.md)
- most recently completed initiative: starter-kit integration
- completed initiative record: [starter-kit-integration-plan.md](starter-kit-integration-plan.md)
- current focus: selective extraction and stability maintenance

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
- builder guidance sharpened to state that the scaffold should remain selective
  and subordinate to the primary project artifacts rather than dominating a
  working repository
- builder guidance sharpened further to frame scaffold modification as expected
  when done deliberately and legibly, rather than as something builders should
  avoid by default
- builder guidance updated to suggest a practical coding-project layout where
  `AGENTS.md` stays at the repository root and the rest of the harness can
  live in one local scaffold directory
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
- an optional `verification_contract` template added to the baseline template
  set as the first reusable extraction from the completed promoted example set
- a post-verification review recorded that no further reusable extension
  artifact is clearly justified yet
- a material-status review recorded that the current classifications still
  broadly hold, with sharper wording needed around partially current
  directories and co-located materials
- a decision recorded that the open standard can support open, proprietary,
  and third-party domain implementations without treating any one of them as
  the standard by default
- a decision recorded to keep the standard, baseline, curated examples,
  selected references, and incubating extraction sources co-located in this
  repository for now
- contributor guidance in `CONTRIBUTING.md` sharpened to distinguish standard,
  guide, example, template, reference, incubating, state, and decision work
  inside the one-repo structure
- a decision recorded to keep the standard narratively versioned for now and
  wait for real release pressure before adding formal tags
- a decision recorded to keep the current reference and migration set in this
  repository for now, including the local `starter_kit` copy as the
  authoritative in-repo reference source
- `harness-kit/` registered as an incubating, evidence-backed executable
  implementation source extracted from governed real-world usage, with
  promotion deferred behind named triggers (`history/decisions/0017`)
- a first usage-driven extraction pass completed: field-tested operating
  practices captured in `docs/guide/harness-operating-practices.md` and a
  layered-trust substrate pattern added to the execution-system integration
  guide
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

1. maintain the current builder path and widen the standard or reference
   surface only when real builder or contributor pressure appears

## Active Priorities

The next useful improvements are:

1. continue extracting reusable material from incubating sources only when a
   real builder gap appears
2. refresh wording when needed so co-located materials are not mistaken for
   one builder path
3. revisit repository boundary only if the split triggers named in
   `history/decisions/0014` begin to appear
4. revisit explicit release tags only if the triggers named in
   `history/decisions/0015` begin to appear

## Open Questions

The main unresolved questions currently are:

1. What repeated builder pressure, if any, would justify another promoted
   example, optional template, or guide extraction?
2. Should the baseline path eventually become executable rather than purely
   document-based, and have the promotion triggers in
   `history/decisions/0017` been met?
3. Which future signals should cause the repository to move from narrative
   versioning to explicit releases or tags?
4. Which future signals should cause the repository to revisit the one-repo
   boundary?

## Immediate Next Actions

The most reasonable next work items are:

1. wait for repeated builder pressure before adding further templates or
   promoted extension artifacts
2. revisit the repository-boundary decision only if the split triggers named
   in `history/decisions/0014` begin to appear
3. revisit the narrative-versioning decision only if the triggers named in
   `history/decisions/0015` begin to appear

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
