# Decision 0001: Separate Triage From Full Intake

## Status

Accepted

## Context

The research landscape and synthesis for this example showed that the current
intake process mixes urgency assessment, information collection, and assignment
into one loose step.

That makes it harder to respond quickly to urgent work and harder to know when
routine work has enough information for assignment.

## Decision

Model triage as a distinct workflow stage before full intake completion.

## Rationale

This separation makes the workflow easier to inspect and easier to adapt across
channels with uneven information quality.

It also preserves a clearer boundary between:

- deciding whether a request needs immediate attention
- collecting the information needed for routine assignment

## Tradeoffs

- the workflow gains another explicit stage
- later operational work will need to define who owns follow-up for missing
  information

## Consequences

- urgent requests can move earlier without waiting for routine intake fields
- assignment should happen only after the intake-complete threshold is met
- future process documentation should use distinct language for triage and
  intake completion
