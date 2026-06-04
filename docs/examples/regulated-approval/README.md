# Regulated Approval Example

This example is a promoted domain-extension pattern for regulated or
approval-heavy work.

It shows how a domain harness can stay legible when compliance, approvals, and
escalation thresholds affect the task flow directly.

## Example Context

Imagine a team that maintains customer-facing guidance in a regulated service
environment.

The team wants:

- explicit compliance review before publication
- visible escalation rules for higher-risk changes
- approval records that are recoverable from the task trace
- a harness that keeps regulatory overlays visible without redefining the
  standard itself

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

Then add only the regulated-domain extensions that the work actually needs:

```text
COMPLIANCE_OVERLAY.md
APPROVAL_MATRIX.md
artifacts/
  approvals/
    change_X_approval.md
  evidence/
    change_X_basis.md
```

The first group is still the local harness.
The second group makes the approval overlay inspectable.

## What This Example Demonstrates

This example demonstrates:

- a regulated-domain overlay that changes orchestration
- explicit approval routing instead of hidden runtime behavior
- verification contracts that include compliance and release authorization
- trace fields that preserve risk class, applicable rule set, and approval
  outcome
- a pattern builders can adapt when domain controls are central to acceptance

## Extension Pattern Summary

The reusable pattern in this example is:

- domain roles that include both operators and approval authorities
- verification contracts that distinguish correctness from compliance
- an approval overlay that affects handoffs and next actions
- domain trace fields that preserve the basis of an approval decision

Builders can reuse that pattern in domains such as:

- healthcare operations
- financial-service content changes
- legal or policy publishing
- security-sensitive operational change control

The domain rules may differ.
The extension categories stay recognizable.

## Example Roles

The local harness might define roles such as:

- change owner: proposes the change and gathers required evidence
- domain analyst: prepares the substantive update
- compliance reviewer: checks policy, regulatory, or control alignment
- approver: decides whether the change may proceed
- publisher: releases only approved changes

These are roles, not runtime-specific buttons or workflow states.

## Example Verification Contracts

A regulated approval flow may use verification contracts such as:

- content correctness: the change says what it intends to say accurately
- evidence sufficiency: the supporting basis and citations are visible
- compliance alignment: the change satisfies the applicable rules or policies
- approval authorization: the required approval authority has accepted the
  change for release

Each contract should define criteria, verdicts, and next action.
Approval is not just another comment label.

## Example Trace Fields

The task trace may need fields such as:

- risk class
- applicable policy or rule set
- approval authority required
- approval verdict
- approval record location
- release constraint or follow-up note

Those fields are domain-specific extensions to trace, not replacements for the
shared trace category.

## Why This Example Matters

The current example set already shows:

- the minimal baseline shape
- a coding-focused scaling pattern
- a document-first research-to-design handoff

This example fills a different builder need:

- it shows how to represent compliance and approvals as visible overlay
  structure
- it shows how higher-risk work can change orchestration without collapsing
  verification into runtime behavior
- it gives builders a pattern for domains where acceptance depends on
  authority as well as correctness

## How To Reuse This Pattern

Reuse this pattern when:

- release or acceptance requires named approval authority
- compliance or policy review is distinct from ordinary correctness review
- risk level changes who may decide what
- builders need approvals to remain visible in the trace

If the domain pressure is only local terminology, this pattern is probably too
heavy.
Use it when the overlay changes responsibility, verification, or routing in a
real way.

## What To Read Next

Use [../../guide/domain-implementation-extensions.md](../../guide/domain-implementation-extensions.md)
for the general extension rule behind this example.

Use [../../guide/execution-system-integration.md](../../guide/execution-system-integration.md)
when the same approval flow needs to be mapped onto a specific runtime or
workflow engine.
