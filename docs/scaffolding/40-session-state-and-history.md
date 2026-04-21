# Session State And History

This document distinguishes current working context from durable historical
context and from raw execution evidence.

That distinction matters because harnesses become difficult to trust when
temporary status, raw traces, and durable rationale are mixed together.

## Session State

Session state captures what matters for continuing current work coherently.

It may include:

- current objective
- active tasks
- open questions
- blocking issues
- important temporary assumptions
- pending verifications
- candidate harness changes surfaced by recent execution

Session state should be easy to update and easy to discard once it no longer
matters.

## Traces Are Not The Same As Session State

Execution traces are evidence from task cycles.

They may inform session state, but they are not the same thing.

Examples:

- a trace may show that a role failed to verify a task correctly
- session state may record that verification rules need clarification

The trace is the evidence.
The session state is the current working interpretation.

## History And Decisions

History and decisions capture context that should remain useful after the
current task or session ends.

They may include:

- why a structure was adopted
- why a verification rule changed
- why an autonomy threshold was tightened
- what tradeoff a contributor accepted
- what interpretation future builders should preserve

## Candidate Changes vs Adopted Changes

A healthy harness distinguishes between:

- candidate changes suggested by use
- adopted changes that become part of the durable system

Candidate changes may appear in session state or an evolution record.

Adopted changes belong in durable documents such as:

- standard definitions
- implementation documents
- history or decision records

## Self-Evolution Placement

The self-evolution loop sits across state and history, but its outputs should
not all land in the same place.

Session state is the right place for current evolution work:

- what recent evidence seems to imply
- which harness change is being considered
- what question is still unresolved
- who or what needs to review the proposed change
- what promotion work remains pending

Durable documents are the right place for adopted evolution outcomes:

- updated standard language
- updated implementation guidance
- updated domain-specific rules
- decision records explaining structural choices
- history entries preserving important rationale

The boundary is proposal versus adoption.

A candidate improvement may live in session state while it is being evaluated.
Once accepted, the change should move into the document that owns the behavior
being changed, with history or decisions capturing rationale when the reason
matters beyond the current task.

## Promotion Rule

When a point stops being merely situational and starts affecting future
interpretation, it should move out of session state and into a durable
document.

Examples:

- a repeated verification need becomes a reusable verification contract
- a repeated trace field becomes part of the trace standard
- a structural tradeoff becomes a decision record
- a recurring improvement pattern becomes part of the evolution loop

## Common Failure Modes

Watch for these failure modes:

- decision rationale hidden inside temporary status notes
- raw traces treated as if they were already interpreted conclusions
- current blockers mixed into permanent definitions
- examples treated as if they were general rules
- candidate harness changes adopted without visible review

## Practical Implication

A healthy scaffold keeps current work easy to resume, preserves enough evidence
to explain what happened, and records durable interpretation in the right
layer.

See [50-traces-verification-and-evolution.md](50-traces-verification-and-evolution.md)
for the dedicated treatment of traces, verification, and the improvement loop.
