# 0008 Expertise Profiles Are Implementation Extensions

## Context

The open-standard rewrite needs to support expertise levels such as junior,
regular, and senior without tying the standard to one company-specific staffing
model or commercial packaging scheme.

Those terms are useful because many domain harnesses need different autonomy,
review, and escalation rules for the same kind of work.

The modeling ambiguity was where those tiers belong:

- as roles
- as verification contracts
- as orchestration rules
- as optional implementation profiles

If this remains unclear, implementations may blur responsibility, authority,
and verification criteria.

## Decision

Expertise levels are modeled as optional autonomy or expertise profiles.

They are implementation extensions, not standard-core roles by themselves.

An expertise profile modifies a role assignment by defining:

- what the actor may decide independently
- what the actor may execute only with review
- what the actor must escalate
- what verification is required before completion

The standard keeps expertise profiles distinct from:

- roles, which define responsibility
- verification contracts, which define criteria, verdicts, and consequences
- orchestration, which defines when profile thresholds change routing,
  escalation, or handoff

The labels `junior`, `regular`, and `senior` may be used as examples, but the
standard does not require those exact names.

## Consequences

Positive consequences:

- the standard can support graded autonomy without baking in one organization
  model
- implementations can adapt expertise labels to their domain while preserving
  a common structure
- role definitions stay stable even when different actors have different
  authority levels
- verification criteria remain explicit rather than hidden inside seniority
  labels

Boundary consequences:

- a profile should not replace a role name
- a profile should not define acceptance criteria directly
- orchestration should state how profile thresholds affect routing, review, and
  escalation

Tradeoff:

- minimal harnesses may ignore expertise profiles until they need graded
  autonomy

This tradeoff is acceptable because the standard remains small while giving
larger or higher-risk implementations a clear extension point.
