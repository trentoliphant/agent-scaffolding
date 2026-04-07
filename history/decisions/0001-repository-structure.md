# 0001 Repository Structure

## Context

The repository originally described a layered scaffolding system, but the actual files did not yet reflect that structure.

This created a mismatch:

- contributors could understand the intent, but had no clear document map for evolving it
- builders could read the vision, but had no practical entry point, guide, or example to apply

## Decision

The repository is structured around four separate documentation layers:

- `docs/scaffolding/` for system definition
- `docs/guide/` for builder-facing application guidance
- `docs/examples/` for concrete applications
- `history/decisions/` for durable rationale

In addition:

- `README.md` serves as the audience router and top-level entry point
- `AGENTS.md` is narrowed to repo-specific operating guidance
- `CONTRIBUTING.md` defines contribution workflow and placement rules

## Consequences

Positive consequences:

- builders have a clearer path from overview to adoption to examples
- contributors have clearer boundaries for where new content belongs
- system definition is easier to keep conceptually clean
- repository-level operating guidance is separated from the scaffold itself

Tradeoffs:

- the repository now has more files to keep aligned
- contributors must think harder about document placement

Those tradeoffs are acceptable because they improve both clarity and usability, which are primary objectives of the repository.
