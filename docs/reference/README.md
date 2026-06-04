# Reference Implementations And Migration Sources

This section identifies real working systems and older materials that matter to
the development of the standard.

These are not the standard itself.
They are also not merely downstream examples.

They are reference implementations, extraction sources, and migration aids that
can help the standard improve without forcing the standard to mirror them.

## Purpose

Use this section to capture sources that are relevant because they are:

- usable systems in their own right
- evidence of how harness patterns work in practice
- sources from which reusable patterns may be extracted
- migration material for older implementations moving toward the standard

When practical, keep reference sources intact enough to preserve their value as
working systems and extraction inputs.

## Relationship To Other Layers

Keep these distinctions explicit:

- `docs/scaffolding/` defines the open standard
- `docs/guide/` explains how to adopt and extend the standard
- `docs/examples/` shows teaching-oriented applications
- `docs/reference/` preserves older or external systems that inform the
  standard
- `templates/` provides baseline implementation assets

Reference material may influence the standard, but instance-level documents
should not be copied into the standard without generalization.

Examples derived from references belong in `docs/examples/` only when a
reduced, teaching-oriented version materially improves understanding.

Templates derived from references belong in `templates/` only when they are
useful as baseline implementation assets rather than as source-preserving
mirrors.

## How To Use Reference Material

When using a reference implementation to refine the standard:

1. Identify the reusable pattern.
2. Preserve the reference source in `docs/reference/` as-is or close to as-is.
3. Decide whether the pattern belongs in standard definition, guide material,
   examples, templates, or migration guidance.
4. Create a simplified example only if that simplification adds teaching value.
5. Preserve the distinction between generalized concepts and instance-level
   documents.

## Current Reference Source

### `starter_kit`

Location:

- local reference copy: `docs/reference/starter_kit/`
- external source: `/Volumes/Home/Users/trentoliphant/Development/starter_kit`

Current interpretation:

- `starter_kit` is a usable starter package
- `starter_kit` is a working reference implementation
- `starter_kit` is a migration aid for older document-structured workflows
- `starter_kit` is one source from which reusable patterns have been extracted
- the local `docs/reference/starter_kit/` copy is the authoritative in-repo
  reference source for this repository's reference layer

This means it should not be treated as:

- the open standard itself
- the default builder path
- the final baseline for non-coding domains

Related materials:

- migration guide:
  [../guide/starter-kit-adoption.md](../guide/starter-kit-adoption.md)
- reduced example:
  [../examples/structured-project-starter/README.md](../examples/structured-project-starter/README.md)

Retained legacy context:

- nested legacy subtree: `docs/reference/starter_kit/v1/`

## Reference Layer Rules

The reference layer should:

- preserve source material accurately enough to remain useful
- help contributors reason about where patterns came from
- help builders migrate older material when needed

The reference layer should not:

- silently define the standard
- become the default builder onboarding path
- accumulate unrelated archives without clear relevance

Keep the retained reference layer small.
If a reference source stops serving extraction, migration, or provenance
value, reconsider whether it still belongs here.

## Current Note

This section is intentionally lightweight.

At this stage, a simple named place for references and migration sources is
enough. It keeps the relationship visible without creating a heavy new
subsystem.
