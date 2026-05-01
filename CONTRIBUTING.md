# Contributing

This repository is building an open standard, not collecting disconnected
notes.

Contributions should improve at least one of the following:

- conceptual clarity
- builder usability
- modularity of the standard
- inspectability of mixed human and machine systems
- consistency between standard, guides, examples, references, and templates
- the repository's ability to learn from real usage without silent drift

## Contribution Priority

Builders are the primary audience for the standard itself.

Contributor-facing refinement matters, but it should support the builder path
rather than overwhelm it.

## One-Repo Working Model

This repository intentionally keeps several material types together for now:

- standard definition
- builder guidance
- teaching-oriented examples
- baseline implementation assets
- reference and migration material
- incubating extraction sources

That co-location is a convenience for builders and contributors.
It is not permission to treat all material as equally current or equally
authoritative.

Use [docs/guide/repository-status.md](docs/guide/repository-status.md) to
check whether the material you are editing is `Current`, `Transitional`,
`Reference/Migration`, `Legacy`, or `Incubating`.

When in doubt, preserve the current builder path first and treat supporting
materials as context, not as silent source of truth.

## Before You Change Something

Start by locating the correct layer for the change:

- `docs/scaffolding/` for standard definition
- `docs/guide/` for adoption and extension guidance
- `docs/examples/` for teaching-oriented applications
- `docs/reference/` for reference implementations and extraction sources
- `templates/` for baseline implementation assets
- `state/` for current priorities, open questions, and active rewrite work
- `history/decisions/` for durable rationale

If a proposed change does not clearly belong anywhere, that is a sign to
clarify the concept before expanding it.

Also check [docs/guide/repository-status.md](docs/guide/repository-status.md)
when the status of a document is relevant to your change. Avoid treating
`Transitional`, `Reference/Migration`, `Legacy`, or `Incubating` materials as
if they were automatically current source of truth.

Before editing, identify which contribution type you are making:

- standard change
- guide change
- example change
- template change
- reference or migration change
- incubating extraction work
- state or planning update
- decision-record update

If you cannot name the change type clearly, narrow the change before you edit.

## Core Expectations

- Prefer the smallest coherent change that advances the repository
- Preserve terminology unless a change clearly improves precision
- Keep documents readable by a thoughtful human reader
- Keep standard definition separate from implementation guidance
- Keep the open standard separate from baseline implementation assets
- Keep domain-specific or company-specific needs from silently redefining the
  standard core
- Record meaningful structural changes in `history/decisions/`

## Standard Stewardship Rules

When deciding whether a concept belongs in the standard core, ask whether it:

- is reusable across many domains
- improves inspectability or interoperability
- helps mixed human and machine systems stay legible
- supports traceability, verification, or scaffold improvement

If the answer is no, the concept may still be valuable, but it probably belongs
in:

- an extension
- a template
- a guide
- an example
- a reference implementation

## Common Change Types

Use the following heuristic:

- add or revise a principle when a constraint should apply across the standard
- add or revise a role when a responsibility-bearing position needs definition
- add or revise a task pattern when a repeatable unit of work needs structure
- add or revise a verification contract when reusable evaluation criteria and
  verdict flow need definition
- add or revise orchestration when routing, handoffs, or escalation change
- add or revise trace guidance when the minimum observable task record changes
- add or revise the self-evolution loop when the standard's learning model
  changes
- add or revise a guide when builders need a clearer adoption or extension path
- add or revise an example when a concept needs a concrete application
- add or revise a template when the baseline implementation assets need a more
  useful default
- add a decision record when repository structure or interpretation changes in a
  durable way

## Change Ownership By Layer

Use these working rules when deciding how to change a layer.

### Standard Changes

Standard changes belong in `docs/scaffolding/`.

They should:

- define reusable cross-domain structure
- remain model-agnostic and execution-system-agnostic
- avoid borrowing domain-specific wording unless it is generalized first

They should not:

- be justified only by one example, one company need, or one reference source
- import local workflow conventions as if they were part of the core standard

### Guide Changes

Guide changes belong in `docs/guide/`.

They should:

- make adoption, extension, or interpretation easier for builders
- explain how to apply the standard without redefining it

They should not:

- quietly become new standard definition
- depend on one example or reference source without saying so

### Example Changes

Example changes belong in `docs/examples/`.

They should:

- stay teaching-oriented
- answer a builder question that benefits from a concrete application
- map back to the shared standard categories visibly

They should not:

- become a broad catalog of domain implementations
- introduce a promoted example unless the current set leaves a real builder gap

### Template Changes

Template changes belong in `templates/`.

They should:

- improve the baseline implementation path
- stay smaller and more portable than full reference-source material

They should not:

- turn domain-specific practice into a baseline default without repeated need
- be added just because a source document exists elsewhere in the repository

### Reference Or Migration Changes

Reference and migration changes belong in `docs/reference/` and related
translation guides.

They should:

- preserve source material accurately enough to remain useful
- help contributors trace where patterns came from
- help builders migrate older material when needed

They should not:

- silently redefine current source of truth
- be rewritten into current guidance without an explicit extraction step

### Incubating Extraction Work

Incubating work usually starts from `design_model/` or `research_model/`.

It should:

- identify a reusable gap in the current builder path first
- extract the smallest useful artifact into a guide, template, example, or
  decision record
- preserve the incubating source unless there is a strong reason to do
  otherwise

It should not:

- promote an incubating directory wholesale into the current builder path
- widen the baseline just because the incubating source is thoughtful or rich

### State And Decision Updates

State updates belong in `state/`.
Decision records belong in `history/decisions/`.

Use `state/` for:

- active frontier
- open questions
- working review notes

Use `history/decisions/` for:

- durable structural choices
- durable interpretation changes
- tradeoffs future contributors should not have to rediscover

Do not leave durable repository-boundary changes only in `state/`.

## Allowed Change Bundles

Some multi-file changes are healthy and expected.

Common good bundles include:

- standard plus guide updates when guidance must catch up to a clarified
  concept
- guide plus example updates when a builder-facing explanation needs a concrete
  illustration
- template plus guide updates when baseline assets change
- decision record plus state updates when a durable structural choice changes
- extraction work plus source-preserving notes when a reference or incubating
  pattern is promoted carefully

Be cautious with bundles like:

- standard plus reference rewrites in one step
- promoted example additions plus baseline template expansion in one step
- reference or incubating edits presented as if they were current builder-path
  changes

If a change crosses multiple layers, say why each layer changed.

## Extraction Workflow

When working from `docs/reference/`, `design_model/`, or `research_model/`:

1. Identify the builder or contributor need first.
2. Identify the reusable pattern inside the source.
3. Decide the target layer:
   - `docs/scaffolding/` for standard concepts
   - `docs/guide/` for application guidance
   - `docs/examples/` for teaching-oriented illustration
   - `templates/` for baseline implementation assets
   - `history/decisions/` for durable interpretation
4. Extract the smallest artifact that solves the need.
5. Preserve the source material as reference or incubating material unless a
   separate cleanup decision is justified.

This repository should evolve by selective extraction, not by relabeling older
material as current.

## Contributor Workflow

1. Read the relevant files before changing them.
2. Read [state/current.md](state/current.md) if you are resuming repository
   work from a clean session.
3. Identify the change type and the target layer before editing.
4. Make the smallest coherent change that advances the repository.
5. Update neighboring documents if the meaning or structure changed.
6. Add a decision record when the repository's structure or interpretation
   changes materially.
7. Update `state/current.md`, `state/roadmap.md`, or the active plan file if
   the active frontier changed.
8. Review the result from both the builder and contributor perspective.

## Repository Workflow Preferences

These are local conventions for working in this repository. They are not the
standard definition itself.

### Commits

- Prefer one commit per coherent repository change when practical
- Use commit messages that describe the change in plain language
- When helpful, use a short subject plus bullet points in the body
- Avoid vague commit subjects such as `update`, `fix`, or `changes`
- Avoid mixing unrelated documentation, structure, and template changes in one
  commit unless they form one clear initiative step

### Document Updates

- When a durable interpretation changes, add or update a decision record
- When the active frontier changes, update `state/current.md`
- When a major initiative advances, update its plan file to show completed
  work, remaining work, and next step
- Keep standard definition, guides, examples, references, templates, and state
  documents distinct

## Review Checklist

Before considering a change complete, ask:

- Does the repository remain well-defined?
- Does the repository become more usable for builders?
- Is the correct layer carrying the correct content?
- Are guides, examples, references, and templates still consistent with the
  standard?
- Have important reasons been documented rather than left implicit?
- Has the change kept the open standard distinct from one specific
  implementation pattern?
- Would a later contributor understand whether this was a standard update,
  a builder-path update, a teaching example, a source-preserving reference
  change, or an incubating extraction?

## Decision Records

Write a decision record when:

- the repository structure changes
- a concept is split, merged, reinterpreted, or reclassified
- a naming choice is likely to affect future work
- a tradeoff should remain visible to later contributors
- the boundary between standard core and extension changes materially

Use short, durable records that explain:

- context
- decision
- consequences

## References, Examples, And Templates

Keep these distinctions explicit:

- references are working systems or older materials that inform the standard
- examples are teaching-oriented illustrations
- templates are baseline implementation assets

None of those should silently become the standard definition.

When adding to `docs/examples/`, prefer a small curated set of promoted
examples rather than a broad catalog.
Add another example only when it fills a builder need that the existing
examples do not already address.
If the material needs large local structure or dense domain-specific context to
make sense, it likely belongs in a domain implementation, incubating area, or
reference layer instead.

## Builder Awareness

If contributor-facing refinement makes the repository harder to adopt, that
tradeoff should be justified explicitly and reduced where possible through:

- clearer guides
- better examples
- more explicit template guidance
- simpler entry points
