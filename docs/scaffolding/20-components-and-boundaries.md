# Components And Boundaries

This document defines the primary modules of the standard and the boundaries
between them.

The goal is not to maximize the number of categories. The goal is to keep the
important distinctions visible so domain harnesses can stay modular and
inspectable.

## Principles

Principles are durable interpretive rules that shape the whole standard.

Use principles when a statement should remain true across many domains or
revisions.

Principles are not:

- current status
- one-off implementation advice
- domain-specific policy

## Roles

Roles are responsibility-bearing positions within the harness.

A role answers the question: who is responsible for a kind of work or judgment?

In the standard, roles should be defined independently from whether the actor
is human or machine.

Roles are not:

- individual tasks
- execution transcripts
- verification criteria
- autonomy tiers by themselves

## Tasks

Tasks are units of work.

A task answers the question: what work is being performed right now?

Tasks should define enough structure to support:

- assignment
- execution
- verification
- trace capture
- handoff

Tasks are not:

- durable responsibilities
- a whole workflow policy
- historical rationale

## Verification Contracts

Verification contracts define how work is evaluated.

A verification contract answers the questions:

- what is being verified?
- what criteria apply?
- what verdicts are possible?
- where does the verdict go?

Earlier versions of this repository often used the broader term `review types`.
The newer term is more precise for the standard because it emphasizes explicit
criteria, verdict handling, and downstream consequences.

Verification contracts are not automatically:

- roles
- execution mechanisms
- workflow standards

A role may perform verification, but the contract should remain separately
defined when it is reusable.

## Verification Modeling Rule

In the standard, verification should be modeled primarily as a reusable
contract, not primarily as a role and not merely as a workflow stage label.

That means the standard should keep distinct:

- the verification contract: what is being checked, by what criteria, with what
  verdicts and consequences
- the verifier role: who is authorized or expected to apply the contract
- the orchestration rule: when verification happens and what the harness does
  next

These parts work together, but they should not collapse into one another.

## Verification Roles And Review Language

A role may carry verification responsibility.

Examples:

- reviewer
- approver
- auditor
- domain expert

Those are role assignments, not the verification contract itself.

Similarly, an implementation may still use labels such as `correctness review`
or `compliance review` when those are useful local names.

In the standard, those should be interpreted as one of two things:

- a local name for a verification contract
- a local workflow label for applying one or more verification contracts

They should not remain ambiguous if the harness is meant to be inspectable.

## Orchestration

Orchestration coordinates work across roles, tasks, verification, and state.

It answers questions such as:

- which role acts next?
- what handoff is required?
- when is verification triggered?
- when does work escalate?
- what must be preserved for later review?

Orchestration is not:

- the role definition itself
- the task content itself
- the verification criteria themselves
- a specific execution engine

## Trace Contract

The trace contract defines the minimum observable record of a task cycle.

It answers the question: what evidence from execution must be preserved so the
result can be reviewed and improved later?

The standard-level trace contract should remain lightweight and portable.

A trace contract is not:

- the full session state
- a durable decision record
- the implementation of logging infrastructure

## Session State

Session state captures what matters for continuing current work coherently.

It may include:

- active objective
- open questions
- current assumptions
- in-flight tasks
- pending escalations
- candidate changes suggested by recent work

Session state is not:

- the full execution trace corpus
- adopted historical rationale
- a substitute for the standard definition

## History And Decisions

History and decisions capture why the harness changed and what should remain
visible later.

They answer questions such as:

- why was a structural choice made?
- what tradeoff was accepted?
- what interpretation should future contributors preserve?

History and decisions are not:

- transient status notes
- raw task traces
- unreviewed evolution proposals

## Self-Evolution Loop

The self-evolution loop is the structured process for learning from observed
task cycles.

It answers questions such as:

- what assumption did the task rely on?
- did that assumption hold?
- what failed or degraded?
- what part of the harness should be clarified, tightened, or extended?

The self-evolution loop is not:

- silent prompt drift
- automatic mutation of the standard
- a replacement for review and approval

## Optional Extension Modules

Some modules are important but need not belong to the standard core.

Common extension candidates include:

### Autonomy Or Expertise Profiles

These define how much independent judgment a role may exercise in a given
implementation.

Examples:

- junior
- regular
- senior

These profiles are useful because they let one implementation vary decision
rights and escalation thresholds without redefining the role itself.

### Workflow Standards

Workflow standards define repository-level or organization-level conventions
for how work is recorded, reviewed, and promoted.

Examples:

- branching conventions
- commit conventions
- document update rules
- review-flow conventions

These are often implementation-specific rather than standard-core concepts.

### Integration Profiles

Integration profiles explain how the standard maps onto specific execution
systems or tooling environments.

Examples:

- how a trace is emitted in a given runtime
- how verification verdicts are stored
- how handoffs are represented in a task runner

These profiles belong near the implementation, not in the standard core.

### Domain Modules

Domain modules provide domain-specific content that plugs into the standard.

Examples:

- legal verification criteria
- sales escalation taxonomies
- HR review rules
- medical evidence thresholds

These modules are implementations of the standard, not the standard itself.

## Minimum Harness Contract

Every domain harness that claims to implement this standard should make the
following contracts explicit.

These are the minimum portable commitments, not a full implementation design.

### 1. Principle Contract

The harness should state the durable principles that govern interpretation and
change.

At minimum, those principles should preserve:

- separation between standard and implementation concerns
- explicit distinction between execution and verification
- traceability of task outcomes
- reviewable improvement rather than silent drift

### 2. Role Contract

The harness should define the roles it relies on in terms of responsibility and
boundary, not only named actors.

At minimum, a role definition should make visible:

- what the role is responsible for
- what the role is allowed to decide
- what the role must escalate or hand off

### 3. Task Contract

The harness should define how units of work are represented.

At minimum, a task should make visible:

- the work to be performed
- the role responsible for execution
- the expected output or completion condition
- any required verification or handoff

### 4. Verification Contract

The harness should define how work is judged.

At minimum, a verification contract should make visible:

- the subject being verified
- the criteria being applied
- the role or function allowed to verify
- the possible verdicts
- the consequence of each verdict

### 5. Orchestration Contract

The harness should define how work moves through the system.

At minimum, orchestration should make visible:

- how a task starts
- when handoff occurs
- when verification is triggered
- when escalation is required
- when a task cycle is considered complete

### 6. Trace Contract

The harness should preserve a minimum inspectable record of each task cycle.

At minimum, a trace should make visible:

- what task was attempted
- which role was responsible
- who or what actually acted
- what result or key evidence was produced
- what verification result followed
- what next action, if any, was triggered

### 7. State Contract

The harness should separate current working context from durable history.

At minimum, the implementation should make visible:

- what matters for resuming current work
- what counts as durable rationale
- where candidate changes live before adoption

### 8. Evolution Contract

The harness should define how repeated use can lead to reviewable improvement.

At minimum, the evolution loop should make visible:

- what outcome or pattern triggered review
- what change is being proposed
- which layer the proposed change belongs in
- how the change becomes adopted, deferred, or rejected

## Minimum Completeness Rule

A harness does not need sophisticated implementations of every module to align
with the standard.

It does need each contract above to be explicit enough that a thoughtful human
reader can inspect:

- how work is assigned
- how work is judged
- what evidence is preserved
- how the harness learns from repeated use

If one of those questions can only be answered by inference, hidden runtime
behavior, or undocumented custom practice, the harness is not yet complete at
the standard level.

## Common Boundary Tests

Use these tests when placement is unclear:

- If it should remain true across many domains or revisions, it is probably a
  principle
- If it assigns responsibility, it is probably a role
- If it describes unit work to be performed, it is probably a task
- If it defines evaluation criteria and verdict flow, it is probably a
  verification contract
- If it coordinates routing, handoffs, or escalation, it is probably
  orchestration
- If it defines the minimum evidence preserved from execution, it is probably a
  trace contract
- If it describes what matters right now, it is probably session state
- If it explains why the harness changed, it belongs in history or decisions
- If it proposes a change based on observed use, it belongs in the
  self-evolution loop until adopted
- If it is specific to one repository, runtime, or domain, it is probably an
  extension or implementation detail rather than standard core
