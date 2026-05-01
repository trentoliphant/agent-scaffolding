# 0016 Current Reference And Migration Set Remains In-Repo For Now

## Context

The repository now has an explicit boundary between:

- the open standard
- the baseline implementation path
- the curated teaching-oriented examples
- selected reference and migration material
- incubating extraction sources

That made it reasonable to ask whether the existing reference and migration
set still earns its place in the repository long term.

The current set is still narrow:

- `docs/reference/README.md`
- a local `docs/reference/starter_kit/` reference copy
- `docs/guide/starter-kit-adoption.md`
- `docs/examples/structured-project-starter/README.md`
- a nested legacy `docs/reference/starter_kit/v1/` subtree

This material remains relevant because it explains where some baseline
templates and older workflow assumptions came from, and because it supports
migration from older starter-kit-derived workflows.

The local `starter_kit` copy also remains important because the external
source path named in earlier notes is not a dependable in-repository
dependency.

## Decision

Keep the current reference and migration set in this repository for now.

Treat the local `docs/reference/starter_kit/` copy as the authoritative
in-repo reference source for `starter_kit`.

Keep:

- `docs/reference/README.md`
- `docs/reference/starter_kit/`
- `docs/guide/starter-kit-adoption.md`
- `docs/examples/structured-project-starter/README.md`
- `docs/reference/starter_kit/v1/` only as a nested legacy part of the
  retained reference source

Do not separately promote `v1` material.

Do not add new reference or migration material casually.
Add or retain such material only when it:

1. is a real extraction source for current or likely standard work
2. materially helps builders migrate older workflows
3. preserves context that current guides, templates, or examples would be
   harder to understand without

Revisit this decision only if:

1. the reference layer grows beyond a small, inspectable supporting set
2. the retained source material stops informing real extraction or migration
   work
3. builder confusion begins to come from reference-layer presence rather than
   from wording or classification
4. maintaining local copies becomes meaningfully more expensive than their
   teaching or extraction value

## Consequences

Positive consequences:

- contributors keep an in-repo source-preserving reference for the imported
  starter-kit-derived material
- builders retain migration help for older document-structured workflows
- the reduced teaching example and the fuller source remain understandable in
  relation to one another
- the repository does not become dependent on an external source path for a
  still-relevant reference implementation

Boundary consequences:

- the reference layer stays intentionally small rather than expanding into a
  broader archive
- `v1` remains visible only as legacy context inside the retained source
- status labeling and contributor guidance remain the main tools for
  preventing confusion between current and reference materials

Tradeoff:

- the repository keeps some older material that is not part of the current
  builder path

This tradeoff is acceptable because the retained set is still small and
continues to provide extraction, migration, and provenance value.
