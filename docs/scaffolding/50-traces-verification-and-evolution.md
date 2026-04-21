# Traces, Verification, And Evolution

This document defines three closely related parts of the standard:

- the trace contract
- verification contracts
- the self-evolution loop

These belong together because they connect execution reality to harness
improvement.

## Why These Modules Matter

A harness cannot improve reliably if it only records whether a task "worked."

It needs a reusable way to capture:

- what was attempted
- what happened
- how the result was judged
- what the harness should learn from the outcome

The standard should define those structures without requiring one storage
system, one review tool, or one execution engine.

## Trace Contract

The trace contract defines the minimum observable record of a task cycle.

At the standard level, a trace should preserve enough information to answer:

- what task was attempted?
- which role performed it?
- who or what actually acted?
- what key observations or evidence were produced?
- what outcome was reached?
- what failed, if anything?
- what should happen next?

Implementations may add more detail, but the standard should stay lightweight.

## Baseline Trace Convention

For a minimal domain harness, the standard should require a trace record that
is explicit enough to reconstruct one task cycle without depending on hidden
runtime behavior.

At minimum, each task-cycle trace should preserve:

- task: what unit of work was attempted
- responsible role: which role owned the work
- acting party: who or what actually performed the task
- outcome: what result was produced
- evidence or observations: what supporting signal, artifact, or notable
  observation the result depends on
- verification result: what judgment followed, if verification occurred
- next action: what the harness expects to happen next

The standard does not require one serialization format for these fields.
It does require that their meaning remain inspectable by a human reader.

## Trace Completeness Rule

The baseline trace convention is meant to answer a small number of portable
questions after the fact:

- What was the harness trying to do?
- Who was responsible, and who actually acted?
- What happened?
- What evidence supports that interpretation?
- How was the result judged?
- What happens next?

If the trace cannot answer those questions for a normal completed or failed
task cycle, it is too thin for the standard baseline.

## Verification Contract

The verification contract defines how a result is judged.

At minimum, it should make explicit:

- the subject being verified
- the criteria applied
- the verifier role or verifier function
- the possible verdicts
- where the verdict is recorded or sent

Possible verdicts may include:

- accepted
- accepted with notes
- revise
- escalate
- blocked

The standard need not require those exact labels, but it should require
explicit verdict handling.

## Verification As A Standard Model

The standard should model verification in a layered way:

- as a contract for judgment
- as an optional role assignment for who performs that judgment
- as orchestration for when the judgment is triggered and what it changes

This means the core reusable unit is the verification contract.

The verifier may be:

- a dedicated human role
- a machine role
- the same role that performed the work, when self-checking is explicitly
  allowed
- a mixed human-machine loop

But the contract should remain legible even when the acting verifier changes.

## Why The Contract Comes First

Modeling verification primarily as a contract makes the standard more
portable.

It allows a harness to preserve the same verification logic even when:

- different roles perform the check in different domains
- the same check is automated in one implementation and manual in another
- one workflow calls the step a review while another calls it approval,
  validation, or audit

If verification is modeled only as a role or only as a stage label, the
standard loses clarity about what is actually being judged.

## Relationship To Older Review-Type Language

Earlier repository material often used `review types` for recurring evaluation
lenses such as correctness, compliance, or usability.

Under the current standard:

- a `review type` is best treated as legacy or local language
- when it defines explicit criteria and verdict flow, it maps to a verification
  contract
- when it only names a workflow step, it belongs to orchestration or local
  implementation guidance

This preserves compatibility with older material without keeping the core model
ambiguous.

## Baseline Verdict Set

To keep minimal implementations portable, the baseline standard should use one
small reusable verdict set.

The recommended baseline verdicts are:

- `accepted`: the result satisfies the required criteria and can proceed or
  conclude
- `accepted_with_notes`: the result is usable, but notable caveats or follow-up
  notes should remain visible
- `revise`: the result is not yet acceptable and should return for correction or
  rework
- `escalate`: the result cannot be resolved within the current authority,
  confidence level, or role boundary
- `blocked`: progress cannot continue because a required dependency,
  permission, input, or condition is missing

An implementation may add domain-specific sub-verdicts or finer labels, but it
should be able to map them back to this portable baseline.

## Verdict Flow

The value of a verdict is not only the label. The harness should also make the
next action inspectable.

At the baseline level, the expected flow is:

- `accepted`: allow completion or transition to the next planned step
- `accepted_with_notes`: allow completion or transition, while preserving the
  notes in the task record or trace
- `revise`: route the work back for rework with the relevant criteria or defect
  made visible
- `escalate`: hand the work to a role, authority, or review path able to make a
  higher-order decision
- `blocked`: pause forward progress until the blocking condition is resolved or
  the task is re-scoped

The standard should require explicit verdict consequences, even if the
implementation uses different routing machinery.

## Verification Is Not The Same As Execution

An executor may also perform self-checking, but that does not remove the need
for explicit verification structure.

The standard should keep distinct:

- execution
- verification criteria
- verification verdict
- downstream action triggered by the verdict

This matters most in high-stakes or regulated domains, but it is useful across
domains.

## Verification Boundary Rule

When placement is unclear, use this rule:

- if it defines what acceptable work means, it belongs in a verification
  contract
- if it defines who may apply that judgment, it belongs in a role definition
- if it defines when the judgment occurs or what follows from it, it belongs in
  orchestration

If one document mixes all three, it should do so deliberately and still keep
the distinctions recoverable to a reader.

## Standard Boundary For Trace And Verification

The core standard should define:

- the minimum questions a trace must answer
- the minimum trace elements needed to answer them
- the need for explicit verification criteria, verdicts, and consequences
- a portable baseline verdict set for cross-domain interpretation

Implementations may define:

- storage format
- field names or schema syntax
- richer evidence payloads
- domain-specific verification criteria
- additional verdict detail or routing logic
- runtime-specific logging, eventing, or automation behavior

This keeps the standard reusable while still allowing concrete harnesses to be
operationally rich.

## Self-Evolution Loop

The self-evolution loop is the structured assessment that happens after a task
cycle or review cycle.

Its purpose is to ask:

- what assumption did the task rely on?
- did the assumption hold?
- what part of the harness helped?
- what part of the harness failed or created friction?
- should any standard, implementation, or domain document be updated?

The loop may be triggered:

- after each task cycle
- after a verification failure
- after repeated similar failures
- during periodic review

## Evolution Outputs

The loop should produce explicit outputs rather than vague commentary.

Typical outputs include:

- no change needed
- clarify a task pattern
- tighten a verification contract
- add or remove a trace field
- adjust an autonomy threshold
- propose a change to orchestration
- record a durable lesson in history or decisions

These outputs are proposals until adopted through the appropriate review path.

## Evolution Output Placement

The self-evolution loop may produce several kinds of output, and each belongs
in a different layer.

Session state should hold:

- the current interpretation of recent trace or verification evidence
- active candidate changes that have not yet been adopted
- unresolved questions about whether a pattern is local or reusable
- pending review, escalation, or promotion work

Durable history and decisions should hold:

- why an adopted harness change was made
- what tradeoff or interpretation future contributors should preserve
- why a repeated pattern was promoted into the standard, baseline
  implementation, or a domain implementation
- why a proposed change was rejected when the rejection affects future
  interpretation

Standard, implementation, or domain documents should hold the adopted change
itself.

For example, if repeated traces show that a verification rule is ambiguous,
session state may track the candidate clarification while it is being assessed.
If the clarification is adopted, the verification contract should be updated.
If the reason for the change affects future interpretation, a history or
decision record should capture that rationale.

## Promotion Path

The baseline promotion path is:

1. trace or verification evidence exposes a possible harness issue
2. session state records the current interpretation and candidate change
3. the candidate change is reviewed through the implementation's approval path
4. adopted changes are made in the appropriate durable document
5. rationale is recorded in history or decisions when future readers need to
   understand why the change was made

This path keeps the standard inspectable without requiring one approval tool,
one storage format, or one automated mutation mechanism.

## What The Standard Should Not Hard-Code

The standard should not hard-code:

- one trace storage backend
- one schema serialization format
- one verifier implementation
- one automatic mutation mechanism
- one policy for who approves evolution changes

Those belong to implementations unless they become true cross-domain needs.

## Common Failure Modes

Watch for these failures:

- traces that are too thin to support diagnosis
- traces that are so verbose they stop being useful
- verification criteria hidden inside role descriptions
- verdicts that do not imply a clear next action
- evolution loops that change the harness without visible review
- execution-system specifics leaking into the core standard

## Practical Rule

Keep the core standard minimal but explicit:

- traces preserve evidence
- verification produces judgment
- evolution turns repeated evidence into reviewable improvement proposals

## Minimum Contract Summary

For a domain harness to satisfy the minimum standard contract in these areas,
it should be possible to answer the following without relying on hidden system
behavior:

- What trace record is preserved for a completed or failed task cycle?
- What criteria or checks determine whether the result is acceptable?
- What verdicts are possible, and what next action does each verdict trigger?
- How do repeated outcomes become an explicit proposal to improve the harness?
- Where do candidate changes, adopted changes, and rationale belong?

If those answers are only implicit, the harness may function operationally, but
it is not yet inspectable enough to fully satisfy the standard.

## Minimum Example Shape

At the level of meaning rather than storage syntax, a minimal compliant task
cycle could be represented as:

- task: draft or review a specific work item
- responsible role: executor
- acting party: human reviewer, machine agent, or mixed loop
- outcome: draft produced, revision made, or no result produced
- evidence or observations: the artifact created, the checks consulted, or the
  issue observed
- verification result: `accepted`, `revise`, `escalate`, `blocked`, or
  `accepted_with_notes`
- next action: complete, hand off, retry, escalate, or wait for an unblocker

The standard does not require that exact wording.
It does require that a minimal harness preserve equivalent meaning.
