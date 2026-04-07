# 0005 Current Starter Set Is The Default Builder Path

## Context

The repository has imported a starter set derived from the `starter_kit` reference source.

That set now includes:

- `system_model.template.md`
- `plan.template.md`
- `progress.template.md`
- `history.template.md`
- `step_spec.template.md`
- `step_review.template.md`
- `periodic_review.template.md`
- `coding_standards.template.md`
- `workflow_standards.template.md`

The remaining question was whether more material should be imported into the default builder path or whether the current set is already sufficient.

## Decision

The current imported starter set is sufficient as the default builder path for now.

No further starter-kit material is imported into the default path unless a later builder need clearly justifies it.

This means:

- the current base set is the default imported starter
- AI-team templates remain an advanced extension
- experiment templates remain a specialized extension
- fuller material remains available in the reference layer

## Consequences

Positive consequences:

- the default builder path now has a stable baseline
- contributors have a clearer stopping point for default-path template imports
- the repository avoids expanding the starter set toward completeness for its own sake
- future imports can be justified by concrete builder need rather than by pressure to mirror the reference source

Boundary consequences:

- the reference source remains the place to look for fuller operating-model patterns
- advanced and specialized modes remain available without redefining the default path
- future changes to the default path should be recorded as deliberate decisions

Tradeoff:

- some builders may still want imported templates that are available only in the reference source

This tradeoff is acceptable because the current starter set already supports a substantial structured workflow while keeping the default adoption path smaller and clearer.
