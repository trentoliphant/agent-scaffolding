# Expertise-Tiered Review Example

This example is a promoted domain-extension pattern for autonomy profiles and
multi-tier review.

It shows how the same role can carry different decision rights without turning
expertise tiers into role replacements.

## Example Context

Imagine a knowledge-operations team that maintains internal guidance used by
support staff and operators.

The team wants:

- junior contributors to move quickly on low-risk edits
- more experienced contributors to complete broader work independently
- explicit escalation thresholds for uncertain or high-impact changes
- a harness where autonomy profiles remain visible instead of being hidden in
  custom norms

## Example Structure

Start from the same baseline shape as the minimal adoption path:

```text
AGENTS.md
SYSTEM_MODEL.md
PLAN.md
PROGRESS.md
history/
  decisions/
state/
  current.md
```

Then add only the expertise-tier extensions the work actually needs:

```text
EXPERTISE_PROFILES.md
WORK_TYPE_MATRIX.md
tasks/
  task_X.md
reviews/
  task_X_verification.md
```

The first group defines the local harness.
The second group makes autonomy boundaries and escalation expectations visible.

## What This Example Demonstrates

This example demonstrates:

- expertise profiles separated from roles
- review requirements that change with risk and profile authority
- escalation thresholds that remain explicit instead of informal
- a pattern builders can adapt when the same role needs different autonomy
  levels
- trace records that preserve which profile acted and why escalation did or did
  not happen

## Extension Pattern Summary

The reusable pattern in this example is:

- stable role definitions
- optional expertise or autonomy profiles layered onto those roles
- a work-type matrix that says what each profile may do independently
- verification rules that vary by scope, uncertainty, or risk

Builders can reuse that pattern in domains such as:

- editorial operations
- customer support knowledge maintenance
- internal policy upkeep
- mixed human and machine analysis workflows

The profile names may change.
The role-versus-authority distinction should stay visible.

## Example Roles And Profiles

The local harness might define roles such as:

- maintainer: updates and organizes the guidance artifacts
- reviewer: applies the verification contracts
- steward: owns the durable standard for the guidance set

Then the implementation may add profiles such as:

- junior: may complete low-risk edits but must escalate broader changes
- regular: may complete routine edits with ordinary review requirements
- senior: may complete broader work and decide some edge cases directly

The role defines responsibility.
The profile defines authority, review requirements, and escalation threshold.

## Example Verification Contracts

An expertise-tiered workflow may use verification contracts such as:

- content correctness: the change is accurate and internally consistent
- scope fit: the acting profile was authorized for the work type and risk
- escalation compliance: required review or handoff happened when thresholds
  were crossed
- trace sufficiency: the task record shows who acted, under which profile, and
  what decision path was used

These are verification contracts, not just mentoring conventions.

## Example Trace Fields

The task trace may need fields such as:

- acting role
- acting profile
- work type
- uncertainty or risk marker
- escalation required or not required
- verification path taken
- approving reviewer if escalation occurred

Those fields keep autonomy visible enough to inspect and improve.

## Why This Example Matters

The current example set already shows:

- the minimal baseline shape
- a coding-focused scaling pattern
- a document-first research-to-design handoff
- a regulated approval overlay

This example fills a different builder need:

- it shows how to represent expertise levels without redefining the role model
- it shows how review can vary by profile and work type without becoming
  arbitrary
- it gives builders a pattern for mixed human and machine systems where
  autonomy needs to scale gradually

## How To Reuse This Pattern

Reuse this pattern when:

- the same role should carry different decision rights in different
  assignments
- escalation thresholds need to be inspectable
- builders need a clearer bridge between expertise and verification
- autonomy drift is creating inconsistent review behavior

If the only difference is who happens to be more experienced, this pattern is
probably unnecessary.
Use it when authority and review requirements actually change.

## What To Read Next

Use [../../guide/customizing.md](../../guide/customizing.md)
for the general rule on expertise profiles.

Use [../../guide/domain-implementation-extensions.md](../../guide/domain-implementation-extensions.md)
when this pattern needs to be combined with other domain-specific modules.
