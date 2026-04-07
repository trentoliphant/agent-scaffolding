# Agent Scaffolding

Agent Scaffolding is a repository for defining a structured system for AI-assisted work and showing how to apply that system in real projects.

This repository serves two audiences:

- Builders who want a practical basis for their own agent-assisted system
- Contributors who want to refine the scaffold itself

The repository is organized so those audiences can take different paths without mixing system definition, usage guidance, concrete applications, reference implementations, and current development state.

## Start Here

If you are a builder:

- Read [docs/guide/start-here.md](docs/guide/start-here.md)
- Then use [docs/guide/minimal-adoption.md](docs/guide/minimal-adoption.md)
- Use [docs/guide/starter-kit-adoption.md](docs/guide/starter-kit-adoption.md) if you want to start from the imported starter-kit patterns
- See [docs/examples/minimal/README.md](docs/examples/minimal/README.md) for a concrete small-scale example

If you are contributing to this repository:

- Read [CONTRIBUTING.md](CONTRIBUTING.md)
- Read [state/current.md](state/current.md) for the active frontier of work
- Use [docs/scaffolding/00-overview.md](docs/scaffolding/00-overview.md) as the conceptual entry point
- Use [docs/reference/README.md](docs/reference/README.md) when you need to understand external reference implementations and extraction sources
- Treat [AGENTS.md](AGENTS.md) as the repo-specific operating contract for agent work

## Repository Map

- `docs/scaffolding/` defines the scaffold itself
- `docs/guide/` explains how to apply the scaffold in a real project
- `docs/examples/` shows concrete applications
- `docs/reference/` identifies working reference implementations and extraction sources that inform the scaffold
- `templates/` provides copyable starter assets derived from reference material where appropriate
- `state/` captures current priorities, open questions, and near-term plans
- `history/decisions/` records durable structural decisions
- `AGENTS.md` defines how agents should work in this repository
- `CONTRIBUTING.md` defines how humans and agents should evolve the repository

## What This Repository Is

This repository defines a scaffold that separates concerns such as:

- principles
- roles
- tasks
- review types
- orchestration
- session state
- history and decisions

The goal is to make agent-assisted work:

- more inspectable
- easier to evolve
- easier to apply repeatedly
- more understandable to humans

## What This Repository Is Not

- It is not only a prompt library
- It is not only a conceptual essay
- It is not a finished framework with one required implementation

The scaffold is meant to evolve, but the structure should remain legible and useful while it evolves.

## Current Status

The repository now includes:

- a layered system-definition section
- builder-oriented guides
- concrete examples
- a lightweight reference layer for working extraction sources
- copyable starter templates derived from reference material
- active state documents for clean-session resumption
- contributor guidance
- decision history for structural changes

It is still early-stage, but it should now be usable both as a reference for contributors and as a starting point for builders.
