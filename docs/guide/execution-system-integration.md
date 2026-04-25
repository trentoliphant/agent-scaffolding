# Execution-System Integration

This guide explains how to map the standard onto a real execution system
without turning the standard into vendor-specific runtime guidance.

Use it when the standard and baseline make sense conceptually, but you need to
decide how the harness will operate in the actual system your project uses.

## Goal

The goal of execution-system integration is not to bless one engine, model
provider, workflow runner, or storage stack.

The goal is to preserve the standard's distinctions while making them concrete
inside a real operating environment.

Good integration should let a builder answer:

- how tasks enter the system
- how roles map to humans, machines, or mixed loops
- how verification is triggered and recorded
- how traces are preserved
- how session state is kept separate from durable history and decisions

## What Must Stay Portable

When integrating with an execution system, keep these parts portable:

- role definitions
- task definitions
- verification contracts
- orchestration rules
- the meaning of the trace fields
- the distinction between session state and durable rationale

Those parts may be represented differently in different systems, but their
meaning should remain inspectable.

## What The Execution System May Specialize

The execution system may specialize:

- how tasks are queued, assigned, or triggered
- how role assignments are represented
- how messages or artifacts move between actors
- how verification requests are initiated
- where trace records are stored
- how session state is loaded between runs
- how notifications, approvals, or escalations are surfaced

Those are implementation choices.
They should support the harness rather than redefine it.

## Integration Mapping Questions

Before choosing a concrete integration, answer these questions:

1. How does new work enter the system?
2. What concrete object represents a task?
3. Where is the responsible role recorded?
4. How is the acting party identified when work is actually performed?
5. How is verification requested, executed, and recorded?
6. Where is the task-cycle trace stored?
7. Where is short-lived current state kept?
8. Where are durable decisions recorded?
9. What event or condition triggers escalation?
10. How does the system resume work across sessions?

If the implementation cannot answer those questions clearly, it is probably
hiding too much behavior inside the runtime.

## Minimal Mapping

At minimum, an execution-system integration should provide a concrete answer
for each standard module in the active harness:

| Standard concern | Minimum integration question |
|---|---|
| Roles | Where is responsibility defined and who may fill each role? |
| Tasks | What concrete record or object represents one unit of work? |
| Verification contracts | Where are criteria, verifier, verdicts, and next actions defined? |
| Orchestration | What actually routes work from one actor or stage to the next? |
| Trace contract | Where is the minimum task-cycle record preserved? |
| Session state | Where is in-flight continuity kept between runs? |
| History and decisions | Where is durable rationale recorded? |

You do not need one tool to do all of this.
You do need the boundaries to stay legible.

## Mapping Tasks

Execution systems often offer tickets, jobs, threads, runs, prompts, or queue
items.

Any of those can represent a task if they make visible:

- the task objective
- scope or constraints
- the responsible role
- any required handoff
- any required verification
- the next action when work completes or fails

Do not rely on the runtime's existence of a job alone as the task definition.
The harness still needs inspectable task meaning.

## Mapping Roles

The most important rule is:

- define the role first
- bind the actor second

An execution system may assign work to:

- a named human
- a configured machine agent
- a service account or automation
- a mixed human-machine loop

That assignment is an implementation detail unless it changes decision rights,
review requirements, or escalation thresholds.

If it does change those things, make the change visible in orchestration or an
expertise profile rather than leaving it implicit in the runtime.

## Mapping Verification

Execution systems vary widely in how they run review or approval steps.

Keep the integration model explicit:

- the verification contract defines what is being judged
- the verifier role defines who may judge it
- the execution system defines how the judgment is requested and where the
  result is recorded

A good integration should make visible:

- what triggered verification
- which contract was applied
- who or what applied it
- what verdict was produced
- what next action followed

Do not let verification disappear into a generic status change with no visible
criteria.

## Mapping Traces

The execution system may store traces in logs, task comments, structured
records, artifacts, or event streams.

Whatever the storage form, the integration should preserve the meaning of the
baseline trace convention:

- task
- responsible role
- acting party
- outcome
- evidence or observations
- verification result
- next action

The system may preserve more than that.
It should not preserve less if the harness is meant to stay inspectable.

## Mapping Session State

Session state is for continuity of current work, not for permanent rationale.

Good places for session state may include:

- a current-state file
- a thread memory document
- an active work tracker
- a run-resume record

Session state should hold:

- the current objective
- open questions
- in-flight tasks
- pending escalations
- candidate changes not yet adopted

Do not use session state as the only place where durable harness meaning lives.

## Mapping History And Decisions

Durable decisions should survive runtime changes.

That means they should not exist only as:

- hidden metadata in a task runner
- ephemeral chat context
- one run's internal memory
- system logs with no durable interpretation layer

Use a durable, human-readable location for decisions whenever a structural
choice or recurring interpretation should persist.

## Common Integration Mistakes

Watch for these mistakes:

- treating the runtime's native status labels as a full verification model
- encoding role meaning only in implementation permissions
- storing trace evidence in places humans cannot inspect later
- merging session state and durable rationale into one running log
- assuming one engine's retry or approval behavior is the same as orchestration
- promoting vendor-specific workflow features into the standard core

## Safe Integration Pattern

A safe default pattern is:

1. Define the harness in human-readable project documents.
2. Map each active standard concern to a runtime object or behavior.
3. Keep the mapping documented in implementation guidance.
4. Record task-cycle traces in a way humans can inspect.
5. Keep durable rationale outside the runtime's transient execution memory.

That pattern works across many systems because it treats the execution system
as a host for the harness, not as the source of the harness's meaning.

## Practical Heuristic

If you changed execution systems tomorrow, ask:

1. Would the role definitions still make sense?
2. Would the verification contracts still make sense?
3. Would the trace fields still mean the same thing?
4. Would the difference between current state and durable decisions still be
   recoverable?

If the answer is no, the integration is carrying too much of the standard's
meaning.

## When To Add More Specific Guidance

Add more specific integration guidance only when:

- a project uses one execution system heavily enough to need local conventions
- repeated friction shows the mapping is ambiguous
- a regulated or high-risk domain needs explicit runtime controls
- a common integration pattern appears across multiple real implementations

When that happens, add the guidance as implementation material or an extension
profile first.
Promote it into the standard only if it proves reusable across domains and
systems.
