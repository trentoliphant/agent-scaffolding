# Agent Scaffolding

Agent Scaffolding is a repository for defining an open standard for
domain-specific harnesses or guardrails used in mixed human and machine agent
systems.

The repository is evolving away from a coding-first scaffold and toward a
modular standard that can be used across domains, models, and execution
systems.

## Who This Is For

This repository serves two audiences:

- builders who want a practical way to define or adopt a domain harness
- contributors who want to refine the open standard itself

Builders are the primary audience for the standard.

## Start Here

If you are a builder:

- read [docs/guide/start-here.md](docs/guide/start-here.md)
- read
  [docs/guide/baseline-implementation.md](docs/guide/baseline-implementation.md)
  when you want the boundary between the standard and the recommended baseline
- then use [docs/guide/minimal-adoption.md](docs/guide/minimal-adoption.md)
- use [docs/guide/customizing.md](docs/guide/customizing.md) when you need to
  add domain-specific modules, expertise tiers, or runtime integrations
- read
  [docs/guide/execution-system-integration.md](docs/guide/execution-system-integration.md)
  when you need to map the harness onto a specific runtime
- read
  [docs/guide/domain-implementation-extensions.md](docs/guide/domain-implementation-extensions.md)
  when you need domain-specific roles, verification, or overlays without
  redefining the shared standard
- review [docs/examples/minimal/README.md](docs/examples/minimal/README.md)
  for a deliberately small example
- review
  [docs/examples/research-to-design/README.md](docs/examples/research-to-design/README.md)
  for a non-software example that shows research feeding design and a current
  domain-extension pattern
- review
  [docs/examples/software-project/README.md](docs/examples/software-project/README.md)
  for a coding-focused scaling pattern
- review
  [docs/examples/regulated-approval/README.md](docs/examples/regulated-approval/README.md)
  for a regulated or approval-heavy pattern
- review
  [docs/examples/expertise-tiered-review/README.md](docs/examples/expertise-tiered-review/README.md)
  for an expertise-tiered autonomy and review pattern
- use [docs/guide/starter-kit-adoption.md](docs/guide/starter-kit-adoption.md)
  only if you want to learn from or migrate older starter-kit-derived patterns

If you are contributing to this repository:

- read [CONTRIBUTING.md](CONTRIBUTING.md)
- read [state/current.md](state/current.md) for the active frontier of work
- use [docs/scaffolding/00-overview.md](docs/scaffolding/00-overview.md) as
  the conceptual entry point
- consult
  [history/decisions/0006-scaffold-is-reframed-as-an-open-standard-for-domain-harnesses.md](history/decisions/0006-scaffold-is-reframed-as-an-open-standard-for-domain-harnesses.md)
  for the current framing decision
- use [docs/reference/README.md](docs/reference/README.md) when older or
  external reference material is relevant
- treat [AGENTS.md](AGENTS.md) as the repo-specific operating contract for
  agent work here

If you are not sure which materials are current:

- use [docs/guide/repository-status.md](docs/guide/repository-status.md)
  first
- treat `Current` materials as the source of truth
- treat `Transitional` materials as usable but still being rewritten
- treat `Reference/Migration` materials as learning or translation aids
- treat `Legacy` materials as historical context rather than current direction
- treat `Incubating` materials as future-facing and not yet integrated

## What This Repository Is

This repository defines a reusable standard for structuring domain harnesses.

The standard is meant to make agentic systems:

- more inspectable
- easier to evolve
- easier to review
- easier to adapt across domains
- less dependent on any one model or runtime

The standard currently emphasizes reusable structure for:

- principles
- roles and responsibility boundaries
- tasks and handoffs
- verification contracts
- orchestration
- trace capture
- session state
- history and decisions
- self-evolution loops

## What This Repository Is Not

- it is not only a prompt library
- it is not only a coding workflow package
- it is not one proprietary domain implementation
- it is not tied to one model provider or execution engine
- it is not a complete marketplace of domain harnesses

## Standard, Baseline Implementation, And Domain Implementations

This repository is increasingly organized around a three-part distinction:

- the open standard: reusable concepts and contracts that should transfer
  across domains
- the baseline implementation: a practical, minimal adoption path for the
  standard
- domain implementations: domain-specific harnesses built on top of the
  standard

That distinction matters because the standard should remain stable enough to
support many implementations without collapsing into any one of them.

## Repository Navigation

Use the repository in this order when you need the cleanest path:

1. Start with `Current` materials.
2. Use `Transitional` materials only when you need practical baseline assets
   or in-progress examples.
3. Use `Reference/Migration` materials when translating older patterns or
   tracing where a pattern came from.
4. Use `Legacy` materials only when older decisions or past initiative context
   matter.
5. Use `Incubating` materials only when evaluating possible future integration.

The status index for those categories lives in
[docs/guide/repository-status.md](docs/guide/repository-status.md).

## Repository Map

- `docs/scaffolding/` defines the standard itself
- `docs/guide/` explains how to adopt and extend the standard
- `docs/examples/` shows concrete applications and teaching-oriented examples
- `docs/reference/` identifies older or external reference implementations and
  extraction sources
- `templates/` provides copyable starter assets where they remain useful
- `state/` captures current priorities, open questions, and active rewrite work
- `history/decisions/` records durable structural decisions
- `AGENTS.md` defines how agents should work in this repository
- `CONTRIBUTING.md` defines how humans and agents should evolve the repository

## Current Status

The repository is in the middle of a deliberate rewrite.

The core scaffolding definition has been reframed around the open-standard
direction, and the builder path is being updated to match that framing.

Some older materials still reflect:

- the earlier coding-oriented center of gravity
- the starter-kit integration phase
- older terminology such as `review types`

Those materials remain useful as reference or migration aids, but they should
not be mistaken for the final shape of the standard.

## Current Vs Transitional Material

The easiest way to understand what is current versus still in transition is:

- current builder and contributor surface:
  [docs/scaffolding/](/Users/trentoliphant/Development/openteams/agent-scaffolding/docs/scaffolding),
  [docs/guide/start-here.md](/Users/trentoliphant/Development/openteams/agent-scaffolding/docs/guide/start-here.md),
  [docs/guide/baseline-implementation.md](/Users/trentoliphant/Development/openteams/agent-scaffolding/docs/guide/baseline-implementation.md),
  [docs/guide/minimal-adoption.md](/Users/trentoliphant/Development/openteams/agent-scaffolding/docs/guide/minimal-adoption.md),
  [CONTRIBUTING.md](/Users/trentoliphant/Development/openteams/agent-scaffolding/CONTRIBUTING.md),
  and [state/current.md](/Users/trentoliphant/Development/openteams/agent-scaffolding/state/current.md)
- classification index:
  [docs/guide/repository-status.md](/Users/trentoliphant/Development/openteams/agent-scaffolding/docs/guide/repository-status.md)

Materials marked `Transitional`, `Reference/Migration`, `Legacy`, or
`Incubating` may still be useful, but they should not be mistaken for the
current standard core.
