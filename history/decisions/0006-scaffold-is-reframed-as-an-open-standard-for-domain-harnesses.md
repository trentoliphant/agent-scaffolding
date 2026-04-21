# 0006 Scaffold Is Reframed As An Open Standard For Domain Harnesses

## Context

The repository originally grew out of a coding-oriented scaffold and later
expanded toward a more general system for AI-assisted work.

That evolution created useful structure, but it also left an unresolved
question at the center of the repository: whether this project is primarily:

- a coding workflow scaffold
- a general methodology for human and machine collaboration
- a starter-kit extraction project

The intended direction is now clearer.

The scaffold is meant to become an open standard for domain-specific
guiderails or domain harnesses:

- modular rather than monolithic
- model-agnostic rather than tied to one provider
- execution-system-agnostic rather than tied to one runtime
- usable for mixed human and machine agent systems
- explicit about what responsibilities, permissions, and verification apply
- able to improve over time through structured learning from usage

This standard is not the same thing as any one proprietary domain
implementation built on top of it.

## Decision

This repository is now interpreted first as the home of an open standard for
domain harnesses.

That standard should define reusable structural patterns for:

- roles and responsibility boundaries
- task shaping and handoff points
- verification contracts and verdict flow
- orchestration rules
- session state and durable history
- trace capture from task execution
- self-evolution loops that refine the scaffold from observed usage
- expertise-level variation in agent autonomy and decision rights

The standard should remain domain-agnostic while making it easy to build
domain-specific harnesses on top of it.

The builder or user path remains the primary audience for the standard itself.
Contributor guidance should remain explicit, but it should support the user
path rather than dominate it.

The standard should stay compatible with mixed human and machine execution.
It should define what a role is expected to do and what constraints apply,
while allowing adopters to decide whether a given role is filled by a human,
a machine, or a combination.

The repository may later be split so that:

- one repository contains the open standard and baseline implementation
- separate repositories contain domain-specific implementations

That structural split remains an open implementation question rather than a
decision made here.

## Consequences

Positive consequences:

- the repository has a clearer north star than the earlier coding-first framing
- future changes can be judged against the standard's usefulness for real
  mixed-agent systems
- domain-specific harnesses can share one common structural contract even when
  expertise tiers, execution engines, and models differ
- the repository now has an explicit place for traceability and scaffold
  improvement loops

Required implications:

- existing coding-centric and starter-kit-derived material should be reviewed
  against the new standard framing
- the scaffold should gain explicit treatment of traces, verification
  contracts, and self-evolution
- repository navigation should eventually distinguish clearly between the open
  standard, baseline implementation patterns, and domain implementations
- integration guidance should explain how the standard maps onto common
  execution systems without making those systems part of the standard itself

Tradeoffs:

- the repository will need a significant rewrite to align older documents with
  the new purpose
- some currently central materials may become secondary, legacy, or reference
  content

These tradeoffs are acceptable because the new framing better matches the
intended product strategy, contributor model, and long-term value of the
scaffold.
