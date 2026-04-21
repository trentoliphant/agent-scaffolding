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

## Contributor Workflow

1. Read the relevant files before changing them.
2. Read [state/current.md](state/current.md) if you are resuming repository
   work from a clean session.
3. Make the smallest coherent change that advances the repository.
4. Update neighboring documents if the meaning or structure changed.
5. Add a decision record when the repository's structure or interpretation
   changes materially.
6. Update `state/current.md`, `state/roadmap.md`, or the active plan file if
   the active frontier changed.
7. Review the result from both the builder and contributor perspective.

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

## Builder Awareness

If contributor-facing refinement makes the repository harder to adopt, that
tradeoff should be justified explicitly and reduced where possible through:

- clearer guides
- better examples
- more explicit template guidance
- simpler entry points
