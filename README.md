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

The practical default is to adopt only the smallest useful harness for your
project.
Do not assume you should reproduce the full repository structure inside a
working software, research, or design project.
The scaffold should support the project's primary artifacts, not dominate them.
You should also expect to adapt the scaffold to the project.
The main discipline is to do that deliberately, so your local use stays easy to
understand later.

For many coding projects, that means keeping `AGENTS.md` at the repository root
and grouping the rest of the scaffold in a single directory rather than
spreading harness files across the top level.

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
- it is not a command to copy every scaffold file into every project

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

For the boundary between the open standard and open, proprietary, or
third-party domain implementations, see
[history/decisions/0012-open-standard-supports-open-and-proprietary-domain-implementations.md](history/decisions/0012-open-standard-supports-open-and-proprietary-domain-implementations.md).

For the current repository-boundary choice, see
[history/decisions/0014-standard-baseline-and-curated-supporting-materials-stay-co-located-for-now.md](history/decisions/0014-standard-baseline-and-curated-supporting-materials-stay-co-located-for-now.md).
The repository intentionally keeps the standard, baseline path, curated
examples, selected references, and incubating extraction sources together for
now, while preserving different status labels inside that shared location.

For the current release stance, see
[history/decisions/0015-standard-remains-narratively-versioned-until-release-pressure-is-real.md](history/decisions/0015-standard-remains-narratively-versioned-until-release-pressure-is-real.md).
The repository currently uses `Current` materials, decision records, and
active-state documents as its stability signals rather than formal release
tags.

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

If you are unsure which files are current, use that guide rather than
inferring status from repository location alone.

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

`design_model/` and `research_model/` remain at the repository root as
incubating extraction sources from an earlier phase, not as current builder
entry points. Use [docs/guide/repository-status.md](docs/guide/repository-status.md)
if you need to confirm their status.
