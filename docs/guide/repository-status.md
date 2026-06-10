# Repository Status

This guide makes it explicit which parts of the repository are currently
aligned with the open-standard direction and which parts are still transitional,
reference-only, or incubating.

Status applies to the named paths or groupings in this guide.
Do not assume an entire top-level directory has one status unless this guide
states that explicitly.

## Status Labels

Use these labels when reading the repository:

- `Current`: aligned with the current open-standard direction
- `Transitional`: useful and active, but still reflects older framing or is
  still being rewritten
- `Reference/Migration`: preserved mainly to learn from, extract patterns from,
  or migrate from
- `Legacy`: preserved for historical context from an earlier repository phase,
  but not part of the current direction
- `Incubating`: promising material that is not yet integrated into the current
  standard shape

## Current Standard Surface

These areas are the main source of truth for the current direction:

| Path | Status | Notes |
|---|---|---|
| `docs/scaffolding/` | Current | Defines the current standard core |
| current builder guide path in `docs/guide/` | Current | Includes `start-here.md`, `baseline-implementation.md`, `minimal-adoption.md`, `customizing.md`, `execution-system-integration.md`, `domain-implementation-extensions.md`, `harness-operating-practices.md`, and this status guide |
| promoted example directories in `docs/examples/` | Current | Includes `minimal`, `software-project`, `research-to-design`, `regulated-approval`, and `expertise-tiered-review`; not every path under `docs/examples/` is current |
| most of `templates/` | Current | Baseline implementation assets aligned around the current starting path, except explicitly transitional items listed below |
| repository entry and governance documents | Current | Includes `README.md`, `AGENTS.md`, and `CONTRIBUTING.md` |
| active state, planning, and current working review notes in `state/` | Current | Includes `current.md`, `open-standard-rewrite-plan.md`, `roadmap.md`, and the review notes directly referenced from `state/current.md` |
| framing and rewrite decisions in `history/decisions/0006-0014` | Current | Records the current open-standard direction and its main structural decisions |

## Transitional Areas

These areas are active and useful, but not fully aligned yet:

| Path | Status | Notes |
|---|---|---|
| `templates/core/coding_standards.template.md` | Transitional | Useful coding-focused extension, but intentionally deferred from the smallest domain-neutral baseline |

## Reference And Migration Areas

These areas are preserved mainly as sources to learn from or migrate from:

| Path | Status | Notes |
|---|---|---|
| `docs/reference/` | Reference/Migration | Holds older or external systems relevant to the rewrite |
| `docs/reference/starter_kit/` | Reference/Migration | Important reference source, not the current standard |
| `docs/examples/structured-project-starter/` | Reference/Migration | Teaching-oriented example of an older richer implementation pattern |
| `docs/guide/starter-kit-adoption.md` | Reference/Migration | Migration and translation guide, not the default builder path |

## Legacy Areas

These areas are still worth keeping visible, but they mainly reflect the
repository's earlier starter-kit-integration phase rather than the current
open-standard direction:

| Path | Status | Notes |
|---|---|---|
| `history/decisions/0003-0005` | Legacy | Useful historical rationale for earlier starter-path choices, but no longer the main framing |
| `state/starter-kit-integration-plan.md` | Legacy | Completed initiative record from the earlier integration phase |
| `docs/reference/starter_kit/v1/` | Legacy | Older historical material preserved inside the reference source |

## Incubating Areas

These areas may become important later, but they are not yet integrated into
the current standard shape:

| Path | Status | Notes |
|---|---|---|
| `design_model/` | Incubating | Earlier design-oriented adapter material kept as an extraction source, not as a near-term promoted example |
| `research_model/` | Incubating | Earlier research-oriented adapter material kept as an extraction source, not as a near-term promoted example |
| `harness-kit/` | Incubating | Evidence-backed executable implementation extracted from governed real-world usage; an extraction source and possible future baseline, not yet promoted (see `history/decisions/0017`) |

## Co-Location Note

This repository intentionally co-locates, for now:

- current standard materials
- baseline implementation assets
- teaching-oriented examples
- reference and migration material
- incubating extraction sources

That co-location does not mean those materials all have the same builder-path
status.

Use the labels in this guide, not directory proximity alone, when deciding
what is current source of truth.

## Practical Reading Rule

If you are unsure where to start:

1. Start with `Current` materials.
2. Use `Transitional` materials when you need practical baseline assets.
3. Use `Reference/Migration` materials when you need to translate older
   patterns.
4. Use `Legacy` materials when you need historical rationale from an earlier
   repository phase.
5. Use `Incubating` materials only when you are explicitly evaluating future
   integration.
