# 0009 Standard Is Ready For Baseline Implementation Pass

## Context

The open-standard rewrite has been clarifying the minimum reusable structure
needed for domain harnesses.

Recent work has defined:

- the core module map
- minimum harness contracts
- trace and verification expectations
- explicit verification verdict flow
- self-evolution output placement
- expertise profiles as optional implementation extensions

The active question was whether more standard-core definition was needed before
cleaning up the baseline implementation materials.

## Decision

The current standard description is complete enough to support a cleaner
baseline implementation pass.

The baseline pass may proceed using the current standard docs as the source of
truth.

The standard is not frozen, but baseline work should now prefer implementation
alignment over additional standard-core expansion.

## Consequences

Positive consequences:

- builders can get a clearer copyable starting path sooner
- templates and examples can be rewritten against stable enough concepts
- the repository can shift from architecture definition toward adoption
  quality

Boundary consequences:

- baseline materials should not invent missing core concepts silently
- if baseline work reveals a true cross-domain gap, that gap should be promoted
  back into `docs/scaffolding/`
- if baseline work only reveals a useful default file, role name, or workflow,
  it should remain in guide, template, or example material

Tradeoff:

- some future standard refinement is still expected as real implementations use
  the scaffold

This tradeoff is acceptable because the current standard now has enough
inspectable structure to support practical implementation without pretending to
be final.
