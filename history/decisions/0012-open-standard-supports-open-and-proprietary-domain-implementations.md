# 0012 Open Standard Supports Open And Proprietary Domain Implementations

## Context

The rewrite has clarified that this repository defines an open standard, a
baseline implementation, and domain implementations built on top of that
shared structure.

It has also become clear that domain implementations will not all have the
same ownership or publication model.
Some may be open and published alongside the standard.
Others may be proprietary, internal, partner-specific, or maintained by third
parties outside this repository.

Without an explicit decision, two kinds of drift become likely:

- proprietary implementation pressure could silently redefine the standard core
- contributors could assume that only openly published implementations count as
  valid uses of the standard

The repository needs a clearer boundary rule.

## Decision

The open standard supports domain implementations regardless of whether they
are open, proprietary, internal, partner-maintained, or third-party.

The publication model of a domain implementation does not determine whether it
is structurally compatible with the standard.
Compatibility is determined by whether the implementation keeps the standard's
shared modules recoverable, including:

- roles and responsibility boundaries
- tasks and handoffs
- verification contracts
- orchestration
- trace expectations
- session state
- durable decisions
- self-evolution outputs where used

The standard remains open and domain-agnostic.
Domain implementations may specialize it heavily, but they should not be
treated as changes to the standard core unless a reusable cross-domain gap has
been demonstrated and explicitly promoted through the repository's normal
decision process.

This repository may contain:

- the open standard
- the baseline implementation
- a small curated set of teaching-oriented examples
- selected reference or migration material

It should not be treated as the required home for every domain
implementation.
A proprietary or third-party implementation may live elsewhere while still
using the standard.

When a proprietary or external implementation claims alignment with the
standard, it should preserve an inspectable mapping from local domain modules
back to the shared standard categories, even if the implementation itself is
not public.

## Consequences

Positive consequences:

- the standard can remain genuinely open without pretending every useful
  implementation must also be open
- builders can adopt the standard inside internal or commercial environments
  without structural ambiguity
- contributors have a clearer rule for resisting company-specific pressure to
  treat one implementation as the standard by default
- future repository-split decisions stay open because implementation location
  is no longer conflated with structural legitimacy

Boundary consequences:

- proprietary requirements do not justify standard-core changes by themselves
- external implementations should still be describable in standard terms even
  when their internal details stay private
- the repository's promoted examples remain teaching artifacts, not a catalog
  of all valid implementations

Tradeoff:

- some implementation details that would help compare domains may remain
  inaccessible when implementations are private

This tradeoff is acceptable because the standard's main responsibility is to
define portable structure and boundary rules, not to require one publication
model for all adopters.
