# 0014 Standard, Baseline, And Curated Supporting Materials Stay Co-Located For Now

## Context

The rewrite clarified that this repository contains multiple kinds of material:

- the open standard
- a baseline implementation path
- a small curated set of teaching-oriented examples
- selected reference and migration material
- incubating extraction sources

That created a repository-boundary question.

One possible response would be to split those materials across multiple
repositories now.
Another would be to keep them co-located while relying on clearer boundaries
inside the repository.

Recent work already established several guardrails that matter here:

- the repository has explicit layers for standard, guide, example, reference,
  state, and decision material
- the promoted example set is intentionally small and non-overlapping
- reference and incubating materials are explicitly classified rather than
  treated as builder-path defaults
- the standard supports open, proprietary, and third-party domain
  implementations without requiring this repository to host all of them

The question is therefore not whether a split is ever possible.
It is whether a split is the best next move now.

## Decision

Keep the open standard, baseline implementation assets, curated teaching
examples, selected reference and migration material, and incubating extraction
sources co-located in this repository for now.

Do not treat that co-location as meaning all materials share the same source
of truth status.
Preserve the distinction through:

- the repository's layered structure
- the status guide
- contributor guidance
- a small curated promoted-example surface
- explicit reference and incubating classifications

Do not treat this repository as the required home for all domain
implementations.
External, proprietary, internal, partner-maintained, or third-party domain
implementations may live elsewhere while still aligning to the standard.

Revisit the one-repo versus multi-repo question only when real pressure
appears, such as:

1. the promoted example layer needs to grow beyond a small curated teaching
   set
2. reference or incubating material begins to dominate contributor work or
   navigation
3. standard changes and domain-implementation changes repeatedly interfere
   with each other in review
4. the standard and baseline need a release cadence that diverges from
   examples or reference material
5. source-of-truth clarity requires heavier status machinery than one
   repository can comfortably support

## Consequences

Positive consequences:

- builders keep one clear place to learn the standard, adopt the baseline,
  review examples, and understand reference sources
- contributors can compare current materials against references and incubating
  sources without cross-repository context switching
- the repository avoids premature governance and versioning overhead
- the distinction between structural compatibility and implementation location
  remains explicit

Boundary consequences:

- co-location must be maintained through active curation rather than assumed
- contributor guidance now matters more because structure alone will not
  prevent drift
- the repository can continue to host supporting material without claiming to
  be the home of every valid implementation

Tradeoff:

- the repository remains somewhat noisier than a fully split ecosystem would
  be

This tradeoff is acceptable because current pressures are better addressed by
clearer boundaries and contributor rules than by immediate structural
separation.
