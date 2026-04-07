# 0002 Reference Implementations And Extraction Sources

## Context

The repository already distinguishes between scaffold definitions, guides, examples, and current repository state.

However, that structure did not yet name a place for real working systems that are relevant in two directions at once:

- they are usable packages or implementations in their own right
- they are sources from which scaffold patterns may be extracted

`starter_kit` is one such case.

Treating `starter_kit` as only a downstream example is inaccurate. The scaffold has also evolved bottom-up from real project usage, including patterns visible in `starter_kit`, while also evolving top-down through generalization.

At the same time, directly merging instance-level documents into scaffold definitions would blur an important boundary.

## Decision

The repository recognizes a separate category for reference implementations and extraction sources.

This category is represented in a lightweight way through:

- `docs/reference/` for naming and describing relevant sources

The role of this category is to document systems that:

- are usable in practice
- embody patterns relevant to the scaffold
- may inform scaffold refinement through extraction and generalization

These sources are not automatically:

- scaffold definitions
- mere examples

## Consequences

Positive consequences:

- the relationship between the scaffold and real working systems is made explicit
- contributors can reference extraction sources without confusing them with definitions
- `starter_kit` can be treated accurately as both usable and instructive
- the repository gains a named place for this concept without overbuilding

Boundary consequences:

- instance-level documents still require generalization before entering `docs/scaffolding/`
- examples in this repository remain distinct from external reference implementations
- guide and template work can draw from reference implementations without collapsing the layers

Tradeoff:

- the repository now has an additional named layer to maintain

This tradeoff is acceptable because it resolves an important ambiguity with a minimal structural change.
