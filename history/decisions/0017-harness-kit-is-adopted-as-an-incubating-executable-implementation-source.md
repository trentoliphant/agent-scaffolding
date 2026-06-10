# 0017 Harness Kit Is Adopted As An Incubating Executable Implementation Source

## Context

A harness derived from this repository was built and used in a real project
(Intelligence Hub) across three phases and 28 governed tasks. After that
usage, a portable kit was extracted from the project's `harness/v2` and
brought back here as `harness-kit/` (kit-0.1).

This is the first material in the repository produced by completing the
self-evolution loop against real usage rather than by forward design. The
repository's active state had been explicitly waiting for "real builder
pressure" before widening the standard or reference surface; this is that
pressure arriving.

The kit differs from the existing incubating sources (`design_model/`,
`research_model/`) in two ways:

- it is evidence-backed by governed usage rather than speculative
- it is a complete executable implementation (validator script, append-only
  ledger schema, generated state, hooks) that positions itself as a baseline
  implementation of the standard

That second property raises a boundary question: the current baseline path is
the document-template set in `templates/core/`, and the kit is effectively a
rival baseline on an enforced substrate. Contributor rules warn against
promoting an incubating directory wholesale and against standard changes
justified by a single project.

## Decision

Register `harness-kit/` as an `Incubating` area in the repository, alongside
but distinguished from the earlier extraction sources.

Do not promote it wholesale into the current builder path now.

Perform a first selective extraction pass at the same time, limited to the
guide layer:

- a new guide capturing operating practices that proved out in governed
  usage (`docs/guide/harness-operating-practices.md`)
- a layered-trust substrate section in
  `docs/guide/execution-system-integration.md`

Both extractions state their single-project provenance explicitly. The
standard core in `docs/scaffolding/` is deliberately untouched: one project
is not sufficient justification for core changes.

Treat possible promotion of the kit — as a second, executable baseline path
or as a promoted reference implementation — as a separate future decision.

Revisit promotion when any of these triggers appears:

1. a second independent project adopts the kit (the kit's own portability
   experiment) and reports findings
2. repeated builder pressure appears for executable validation rather than
   document-template structure
3. further real usage shows the document-template baseline failing in ways
   the enforced substrate addresses

## Consequences

Positive consequences:

- the repository's self-evolution loop is exercised for real: usage findings
  flow back into guides without silently redefining the standard
- builders gain field-tested operating guidance and an integration pattern
  for enforcement substrates
- the kit remains intact and inspectable as a source for future extraction

Boundary consequences:

- `Incubating` now contains both speculative sources and an evidence-backed
  executable source; the status guide must keep that distinction visible
- the question of whether the baseline path should eventually be executable
  rather than purely document-based is now explicit and deferred, not hidden

Tradeoff:

- builders may discover the kit and adopt it directly before it is promoted;
  the status label and its own README make its standing clear, and such
  adoption would itself produce the evidence trigger named above
