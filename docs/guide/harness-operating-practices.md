# Harness Operating Practices

This guide collects operating practices that proved themselves in governed
real-world usage of a harness built on this standard.

Provenance: these practices come from one origin project (the Intelligence
Hub harness, 28 governed tasks across three phases, extracted into the
incubating `harness-kit/`). They are stated generically here, but they have
not yet been validated across multiple independent projects. Treat them as
field-tested defaults, not as standard requirements.

Each practice is mapped to the standard concern it serves.

## Fresh Sessions Per Role

Standard concern: roles, verification.

Start a new session (or otherwise reset working context) when an actor
switches roles, especially into a reviewer or auditor role.

Session reuse used to be justified by the cost of re-orientation. Once
orientation is cheap — a single state or briefing command, a short current
state document — reuse trades nothing for accumulated anchoring. A reviewer
who carries the implementer's context judges the implementer's intent rather
than the delivered work.

If orientation in your harness is still expensive enough to tempt session
reuse, treat that as the defect to fix first.

## Capture Issues Immediately, Triage Later

Standard concern: traces, orchestration.

Record an observed problem the moment it is seen, in a cheap append-only
form, without deciding what to do about it. Routing — into the active task,
a new task, a decision, an escalation, or an explicit deferral — is a
separate, later step.

Two rules keep this honest:

- capture never authorizes a fix
- deferral must name a target, not just postpone

Decoupling capture from triage removes the main reason observations go
unrecorded: the fear that recording one creates an immediate obligation.

## Iterate Freely Inside A Task

Standard concern: traces, session state.

Record process events at task boundaries and handoffs, not during the
back-and-forth inside a task. A harness that demands ceremony during
exploration gets bypassed; a harness that demands honesty at boundaries gets
used.

When a human co-drives work that a machine role is responsible for, record
the acting party as mixed rather than letting the record imply autonomous
machine work. Calibration data about what machines can do unassisted is only
useful if it is honest.

## Keep Planning Freeform, Commit Only The Summary

Standard concern: session state, history and decisions.

Planning conversations should stay exploratory and unrecorded. What gets
committed is a short closing summary: decision criteria, options considered,
decisions made, rejected alternatives, overridden warnings with reasons, and
a small set of explicit bets, each with a falsifier.

Score the bets at the next phase break. This converts planning from
narrative into something the self-evolution loop can actually check.

For hard-to-reverse decisions, consult two independent model families and
treat their divergence — not either answer — as the map of uncertainty.
Record any warning that was overridden, with the reason.

## Audit Directs Attention, It Never Approves

Standard concern: verification, orchestration.

A process auditor's output is a pointer to where human judgment should be
spent, never a verdict that substitutes for it. The moment an audit can
approve, the human gate becomes trust theater: a gate a human cannot cheaply
verify at is not a gate.

Design human gates so the cost of genuine verification at the gate is low:
small deltas, judgment-only review records, a signal that recommends how
much attention each item needs.

## Generate State, Never Author It

Standard concern: session state, traces.

Any document that summarizes current process state should be generated from
the underlying factual record, not written by hand. Authored state drifts;
generated state is exactly as trustworthy as the record beneath it.

The corollary: keep the factual record append-only and cheap to validate, so
the generated view stays cheap to trust. See the layered-trust section of
the execution-system integration guide for the substrate pattern this
implies.

## Adopting These Practices

None of these practices require the executable kit they came from. Each can
be adopted on top of the document-based baseline path by adjusting role
definitions, trace conventions, and workflow standards.

If you find a practice here failing in your project, or a practice missing
that earned its place in your usage, that finding is exactly what this
repository wants: route it back as a contribution with its provenance
stated.
