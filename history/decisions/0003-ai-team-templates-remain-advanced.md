# 0003 AI-Team Templates Remain Advanced

## Context

The repository has imported an initial core starter set derived from the `starter_kit` reference source.

The next question was whether the AI-team templates should be imported into the default starter path or remain an optional extension.

The AI-team templates introduce additional structure such as:

- separate coding, reviewer, and human roles
- machine-complete vs done distinctions
- explicit review and approval boundaries
- a more opinionated multi-agent operating model

These are useful capabilities, but they add operational complexity beyond the current minimal builder path.

## Decision

AI-team templates remain an advanced extension for now.

They are not part of the default imported starter set.

Builders should encounter them only when they have a clear need for:

- explicit multi-agent role separation
- reviewer-agent workflows
- human approval gates
- stronger promotion and trust-boundary control

## Consequences

Positive consequences:

- the default starter path stays smaller and easier to adopt
- builders can begin with a structured single-project workflow before taking on multi-agent complexity
- the repository preserves a clearer distinction between the base starter and advanced operating modes

Boundary consequences:

- AI-team materials remain available in the reference source
- AI-team materials may later be imported as optional templates without changing the default starter path
- experiment templates remain a separate deferred question

Tradeoff:

- builders who already want multi-agent structure must still consult the reference layer rather than a first-class imported template set

This tradeoff is acceptable because it keeps the base adoption path clearer while preserving access to the fuller reference implementation.
