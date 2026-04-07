# 0004 Experiment Templates Remain Specialized

## Context

The repository has already imported a base starter set derived from the `starter_kit` reference source.

The next question was whether experiment templates should become part of the default imported starter path or remain a specialized extension.

The experiment templates focus on process and model evaluation work such as:

- comparing model or configuration behavior
- evaluating reviewer or prompting strategies
- extracting process improvements from controlled experiments

These are valuable activities, but they are more specialized than the repository's current default builder path.

## Decision

Experiment templates remain a specialized extension for now.

They are not part of the default imported starter set.

Builders should encounter them only when they have a clear need for:

- model comparison
- prompt or context evaluation
- process-level experimentation
- structured extraction of lessons from experiments

## Consequences

Positive consequences:

- the default starter path remains focused on practical project setup rather than experimentation infrastructure
- builders can adopt the scaffold without taking on model-evaluation overhead
- the repository keeps a clearer distinction between general project scaffolding and specialized experimental modes

Boundary consequences:

- experiment materials remain available in the reference source
- experiment materials may later be imported as optional templates without changing the default starter path
- the base template set stays oriented toward ordinary project execution

Tradeoff:

- builders who want experiment support must still consult the reference layer rather than a first-class imported experiment template set

This tradeoff is acceptable because it keeps the base adoption path smaller and clearer while preserving access to the fuller reference implementation.
