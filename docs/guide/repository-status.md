# Repository Status

This guide makes it explicit which parts of the repository are currently
aligned with the open-standard direction and which parts are still transitional,
reference-only, or incubating.

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
| `docs/guide/start-here.md` | Current | Primary builder entry point |
| `docs/guide/baseline-implementation.md` | Current | Defines how the baseline relates to the standard |
| `docs/guide/minimal-adoption.md` | Current | Default builder adoption path |
| `docs/guide/customizing.md` | Current | Explains safe extension of the standard |
| `docs/guide/repository-status.md` | Current | Tracks the current classification pass |
| `README.md` | Current | Top-level audience router aligned to the rewrite |
| `AGENTS.md` | Current | Repo-specific operating contract for agent work |
| `CONTRIBUTING.md` | Current | Contributor workflow aligned to the rewrite |
| `history/decisions/0006-...` | Current | Records the current framing decision |
| `state/current.md` | Current | Names the active rewrite and current priorities |
| `state/open-standard-rewrite-plan.md` | Current | Tracks the rewrite initiative |

## Transitional Areas

These areas are active and useful, but not fully aligned yet:

| Path | Status | Notes |
|---|---|---|
| `templates/` | Transitional | Baseline implementation assets still being rewritten around the standard |
| `templates/core/coding_standards.template.md` | Transitional | Useful but still strongly coding-oriented |
| `templates/core/workflow_standards.template.md` | Transitional | Useful but still more implementation-specific than standard-core |
| `docs/examples/minimal/README.md` | Transitional | Strongly aligned to the new direction, but still only one teaching example |
| `docs/examples/software-project/README.md` | Transitional | Useful scaling example, but still uses older scaffold and review-type framing |
| `state/roadmap.md` | Transitional | Useful planning aid, but not yet fully refreshed around completed rewrite steps |

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
| `design_model/` | Incubating | Domain-adapter material from an earlier phase, not yet aligned |
| `research_model/` | Incubating | Domain-adapter material from an earlier phase, not yet aligned |

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
