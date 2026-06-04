# Orchestration

Orchestration is the part of the standard that coordinates work across roles,
tasks, verification, traces, and state.

It defines how the harness behaves, not just what parts the harness contains.

## What Orchestration Is Responsible For

Orchestration is responsible for:

- routing work to the right role
- sequencing task cycles
- defining handoff points
- deciding when verification is triggered
- deciding when escalation is required
- ensuring required trace information is preserved
- keeping session state aligned with active work

## Mixed Human And Machine Operation

The standard should allow orchestration to work regardless of whether a role is
performed by a human or machine.

That means orchestration should define:

- responsibility and handoff rules first
- actor assignment second

The implementation may decide whether a given step is handled by:

- a human
- a machine
- a mixed human-machine loop

But the harness should remain inspectable either way.

## What Orchestration Should Not Absorb

Orchestration should not become a vague catch-all for everything the harness
does.

It should not replace:

- the definition of roles
- the content of tasks
- the criteria of verification contracts
- the trace schema itself
- the full historical rationale of the harness
- the specifics of one runtime or execution engine

## Minimal Orchestration

A minimal harness can use lightweight orchestration.

For example:

1. A task is defined
2. A role is assigned
3. The task is performed
4. Verification is applied
5. A trace is recorded
6. Any durable lesson is proposed through the evolution loop

That is still orchestration, even if it is simple.

## Growing Orchestration

As a harness becomes more capable, orchestration may need to define:

- routing rules by task type
- autonomy thresholds by role profile
- escalation triggers
- approval points
- retry or recovery behavior
- cross-role collaboration patterns
- failure handling and rollback paths

These additions should be introduced only when they make the harness clearer,
safer, or easier to improve.

## Orchestration And Expertise Profiles

Expertise profiles affect orchestration when they change what a role assignment
may do without additional review.

For example, an implementation might allow:

- a senior executor to complete low-risk work after self-checking
- a regular executor to complete the same work after a reviewer accepts it
- a junior executor to draft the work but require handoff before completion

Those differences do not redefine the executor role.
They define autonomy thresholds, review requirements, and escalation triggers
for that role assignment.

Orchestration should make those consequences inspectable:

- which profile may start or complete which task types
- which profile requires verification before completion
- which profile must escalate uncertainty or high-risk changes
- which verdicts route work back, forward, or upward

The verification criteria themselves still belong in verification contracts.

## Orchestration And Verification

Orchestration decides when verification happens and how verdicts affect the next
step.

Typical questions include:

- Must verification happen before completion?
- Does a given verdict trigger retry, revision, escalation, or handoff?
- Is a second verifier required for high-risk tasks?
- What part of the trace is available to the verifier?

Those questions belong to orchestration even though the verification criteria
themselves belong to the verification contract.

The modeling rule is:

- the verification contract defines the judgment
- the verifier role defines who may carry it out
- orchestration defines when it happens and how its verdict changes the flow

## Orchestration And Traces

Orchestration should specify when trace capture occurs and what events must not
be lost.

At minimum, it should ensure the harness can recover:

- what task was attempted
- who or what performed it
- what was observed
- what outcome was reached
- what verification result followed
- what should happen next

## Orchestration Questions

If orchestration is underspecified, ask:

- Who decides which role acts next?
- What must happen before a task can begin?
- What handoff is required before another role can continue?
- What verification is required before work is accepted?
- When does uncertainty trigger escalation?
- What trace must be emitted before the cycle is considered complete?
- What information must be preserved for later improvement?

Answers to those questions usually reveal where the harness needs more explicit
coordination logic.
