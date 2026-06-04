# Research Model Extraction Review

This note records a focused extraction review of `research_model/` against the
current standard, guides, templates, and curated example set.

It is a working review note, not a durable decision by itself.

## Review Goal

Decide which parts of `research_model/` should be:

- extracted now
- deferred for later extraction
- left in the incubating layer

The comparison baseline was:

- `docs/scaffolding/`
- `docs/guide/`
- `templates/core/`
- `docs/examples/research-to-design/`

## Summary Judgment

`research_model/` contains useful source material, but most of it should not be
promoted directly.

The strongest reusable ideas are:

- research-specific evidence discipline
- explicit treatment of open questions as first-class outputs
- plan mutation as an expected property of exploratory work

The weakest candidates for direct extraction are:

- the full research charter template
- the full research plan template
- the current research step template as written
- execution-instruction material such as `CLAUDE.md`

Those artifacts are still too domain-shaped and structurally heavy for the
current builder path.

## File-By-File Recommendations

### `RESEARCH_STANDARDS.md`

Recommendation: partial extraction candidate

Why:

- it contains the clearest reusable domain insights in the directory
- evidence-versus-interpretation separation is useful beyond one research
  domain
- open-question tracking is more explicit here than in the current guide layer
- confidence language is useful, but the exact marker system is probably too
  domain-specific to promote unchanged

What seems worth extracting later:

- a short guide addition on evidence discipline for research-heavy domain
  implementations
- a short guide addition on carrying open questions explicitly
- a note that exploratory domains may need more explicit confidence handling
  than the baseline

What should not be extracted unchanged:

- the full artifact taxonomy
- the exact `Draft / Reviewed / Verified` marker system
- long-form artifact-writing instructions

### `PLAN_TEMPLATE.md`

Recommendation: defer extraction

Why:

- the core idea that research plans mutate is valuable
- the specific phase structure is much too prescriptive for the current
  standard and baseline
- many artifact paths and steps assume a full research-document system that the
  current builder path does not require

What seems worth extracting later:

- a small note or optional template section for exploratory projects stating
  that plan mutation is expected and should be recorded visibly
- possibly a soft-vs-hard dependency distinction if repeated builder pressure
  appears

What should not be extracted unchanged:

- the full multi-phase plan template
- the detailed artifact tree
- the specific research phase sequence as a baseline default

### `STEP_SPEC_TEMPLATE.md`

Recommendation: defer extraction

Why:

- it has several good prompts for investigative work
- the current `templates/core/step_spec.template.md` already covers most of the
  standard-level need in a more portable way
- the current research step template assumes a specialized evidence storage and
  confidence workflow that the repo has not promoted yet

What seems worth extracting later:

- an optional investigative-step appendix or variant with sections for
  questions to address, methodology, evidence to collect, and rabbit-hole risks

What should not be extracted unchanged:

- the full template
- the research-specific confidence and evidence storage assumptions

### `PROJECT_CHARTER_TEMPLATE.md`

Recommendation: keep incubating with no current extraction

Why:

- it is thoughtful, but it behaves more like a full project package than a gap
  in the current builder path
- the repo already has lighter-weight ways to express scope, questions, and
  success criteria across `SYSTEM_MODEL.md`, `PLAN.md`, and examples
- promoting a research charter now would likely over-formalize the baseline

Potential future use:

- source material if repeated builders need a research-project kickoff guide or
  a specialized charter template

### `CLAUDE.md`

Recommendation: leave incubating

Why:

- it is runtime- and prompt-shape-specific
- it does not map cleanly to the current standard core or builder guides
- the repository is trying to stay execution-system-agnostic

## Recommended Extraction Order

If the repo chooses to extract anything from `research_model/`, the best order
is:

1. a short guide note on evidence discipline and explicit open-question
   tracking for research-heavy domains
2. a short guide or template note on expected plan mutation for exploratory
   work
3. only later, if demand appears, an optional research-specific task or charter
   template

## Recommended Immediate Action

Do not extract a full template from `research_model/` yet.

The next sensible move would be a small guide-layer refinement, probably in
`docs/guide/domain-implementation-extensions.md` or a new focused guide, if we
decide the current builder path needs stronger wording around:

- evidence discipline
- open-question tracking
- exploratory plan mutation

If that need is not yet strong, keep `research_model/` as an extraction source
and take no further action.
