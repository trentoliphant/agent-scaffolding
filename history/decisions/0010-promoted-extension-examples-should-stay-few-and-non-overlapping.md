# 0010 Promoted Extension Examples Should Stay Few And Non-Overlapping

## Context

The repository now has its first promoted domain-extension pattern in
`docs/examples/research-to-design/`.

That creates a new curation question for the `docs/examples/` layer.

If promoted examples grow without a limit, the example layer risks becoming:

- a loose catalog of domain implementations
- too large for builders to scan quickly
- blurry about the difference between a teaching example and a fuller
  domain-specific implementation

The repository still needs enough example variety to show that extensions can
take multiple shapes.
But variety should not come at the cost of clarity.

## Decision

Treat the promoted example layer as a small curated set rather than an
expanding catalog.

The working target is roughly three to five promoted extension artifacts.

Add another promoted example only when it fills a builder need that is not
already addressed by the current examples.

When evaluating whether a new promoted example is justified, ask:

- what builder question does it answer that the current examples do not
- whether it demonstrates a distinct extension pattern rather than a small
  variation in domain language
- whether the same need would be better served by a template, guide, or
  reference implementation instead

If an artifact needs extensive local terminology, large supporting structure,
or many domain-specific rules to make sense, it should no longer be treated as
an example first.
In that case it likely belongs in a domain-specific implementation, an
incubating area, or a reference layer.

## Consequences

Positive consequences:

- builders get a smaller, clearer example surface
- contributors have a clearer threshold for adding new examples
- examples remain teaching-oriented rather than drifting into vertical
  implementations
- the distinction between example material and domain implementation stays
  visible

Tradeoffs:

- some useful domain patterns will need to stay guide-only or reference-only
  for longer
- contributors must justify example additions against the existing example set

Those tradeoffs are acceptable because the repository's example layer should
optimize first for clarity and coverage of distinct builder needs, not for
breadth by itself.
