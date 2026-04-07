# Contributing

This repository is building a system, not collecting notes.

Contributions should improve at least one of the following:

- conceptual clarity
- operational usefulness
- continuity across sessions
- consistency between layers
- usability for builders

## Before You Change Something

Start by locating the correct layer for the change:

- `docs/scaffolding/` for system definition
- `docs/guide/` for application guidance
- `docs/examples/` for concrete usage
- `state/` for current priorities, open questions, and near-term work
- `history/decisions/` for durable rationale

If a proposed change does not clearly belong anywhere, that is a sign to clarify the concept before expanding it.

## Core Expectations

- Prefer refining existing structure over replacing it
- Preserve terminology unless a change clearly improves precision
- Keep documents readable by a thoughtful human reader
- Keep system definition separate from application guidance
- Record meaningful structural changes in `history/decisions/`

## Change Types

Use the following heuristic:

- Add or revise a principle when a constraint should apply across the system
- Add or revise a role when a responsibility-bearing position needs definition
- Add or revise a task pattern when a repeatable unit of work needs structure
- Add or revise a review type when a recurring evaluation lens appears across work
- Add or revise orchestration when routing, sequencing, or escalation changes
- Add or revise a guide when builders need a clearer path to adoption
- Add or revise an example when a concept needs a concrete application
- Add a decision record when repository structure or interpretation changes in a durable way

## Contributor Workflow

1. Read the relevant files before changing them
2. Read `state/current.md` if you are resuming repository work from a clean session
3. Make the smallest coherent change that advances the repository
4. Update neighboring documents if the meaning or structure changed
5. Add a decision record when the repository's structure or interpretation changes materially
6. Update `state/current.md` or `state/roadmap.md` if the active frontier changed
7. Review the result from both the builder and contributor perspective

## Repository Workflow Preferences

This section captures workflow preferences specific to this repository.

These are local conventions for working here. They are not the scaffold definition itself.

### Commits

- Prefer one commit per coherent repository change when practical
- Use commit messages that describe the change in plain language
- When helpful, use a short subject plus bullet points in the body
- Avoid vague commit subjects such as `update`, `fix`, or `changes`
- Avoid mixing unrelated documentation, structure, and template changes in one commit unless they form one clear decision or initiative step

### Document Updates

- When a durable interpretation changes, add or update a decision record
- When the active frontier changes, update `state/current.md`
- When a major initiative advances, update its plan file to show completed work, remaining work, and next step
- Keep scaffold definition, guides, examples, reference materials, and state documents distinct

## Review Checklist

Before considering a change complete, ask:

- Does the repository remain well-defined?
- Does the repository become more usable?
- Is the correct layer carrying the correct content?
- Are examples and guides still consistent with the definitions?
- Have important reasons been documented, not left implicit?

## Decision Records

Write a decision record when:

- the repository structure changes
- a concept is split, merged, or reinterpreted
- a naming choice is likely to affect future work
- a tradeoff should remain visible to later contributors

Use short, durable records that explain:

- context
- decision
- consequences

## Builder Awareness

Builders are the primary audience for the system itself.

If contributor-facing refinement makes the repository harder to adopt, that tradeoff should be justified explicitly and reduced where possible through:

- clearer guides
- better examples
- simpler entry points
