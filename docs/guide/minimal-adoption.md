# Minimal Adoption

This guide shows the smallest useful version of the standard for a real
project.

## Goal

The goal of a minimal adoption is not completeness.

The goal is to make a domain harness more legible, inspectable, and improvable
without adding unnecessary process.

Use
[baseline-implementation.md](baseline-implementation.md)
alongside this guide when you want to stay clear about which recommendations
are baseline defaults and which parts belong to the standard itself.

## What A Minimal Adoption Must Clarify

Even the smallest useful adoption should make these things explicit:

- what the harness is trying to achieve
- what roles exist
- which roles are filled by humans, machines, or mixed loops
- what a task cycle looks like
- what must be verified
- what trace is preserved from each task cycle
- where durable harness decisions are recorded

## Recommended Minimal Structure

In your own project, start with something like:

```text
AGENTS.md
scaffold/
  SYSTEM_MODEL.md
  PLAN.md
  PROGRESS.md
  history/
    decisions/
```

Optional when work spans multiple sessions:

```text
scaffold/
  state/
    current.md
```

This gives you:

- a repo-specific operating contract
- a small but explicit local harness definition
- a baseline implementation shape that is easy to adapt
- a place to define trace and verification expectations
- a place for durable rationale
- an optional continuity layer for multi-session work

For many coding projects, this is enough structure to start.
The scaffold should describe how work is coordinated around the codebase, not
replace the codebase as the repository's main content.

Keeping `AGENTS.md` at the repository root while placing the rest of the
scaffold in a single directory is often a good default for coding projects.
It keeps the top level focused on the actual product while still making the
harness easy to find.

## What To Put In Those Files

Use `AGENTS.md` for:

- how agents should work in the project
- local editing and review expectations
- escalation expectations
- where the rest of the scaffold lives if it is grouped in one directory

Use `SYSTEM_MODEL.md` for:

- what the local harness is trying to achieve
- the roles, tasks, verification, trace, and orchestration shape you are
  actually using
- the local choices you are making so they stay visible and reviewable later

Use `PLAN.md` for:

- the current phases, tasks, or work sequence
- which pieces of the harness are being introduced first
- what is intentionally deferred

Use `PROGRESS.md` for:

- current task status
- responsible role and acting party
- verification state
- trace state or links to task records

Use `SYSTEM_MODEL.md` or a task-specific record for:

- the minimum trace expected from a task cycle
- the verification contract used locally
- the improvement loop used to learn from real usage

Use `history/decisions/` for:

- naming choices
- structural tradeoffs
- changes in interpretation
- durable lessons that should outlive the current task

Use `state/current.md` when needed for:

- the active objective
- open questions
- active tasks or blocking issues
- candidate harness changes not yet adopted

The exact directory name is a local choice.
For many software projects, a dedicated directory such as `scaffold/` is
clearer than spreading harness files across the repository root.

## Suggested First Workflow

A simple first workflow is:

1. Define a task.
2. Assign or imply the role responsible for doing it.
3. Execute the task.
4. Apply an explicit verification contract.
5. Record a lightweight trace of what happened.
6. Record any durable structural lesson as a decision.

That loop is often enough to prove whether the harness is helping.

## Keep The Scaffold Small Relative To The Project

In most projects, the scaffold should occupy a small surface area compared with
the primary project artifacts.

For example:

- in a software project, source code, tests, product docs, and operational
  assets should remain primary
- in a research workflow, notes, sources, syntheses, and outputs should remain
  primary
- in a design workflow, briefs, explorations, decisions, and deliverables
  should remain primary

The scaffold is successful when it clarifies the work without demanding that
every project create a large parallel document system.

If the scaffold starts to dominate repository attention, trim it back to the
smallest set that still makes roles, verification, traces, and decisions
explicit.

That does not mean your first version has to be perfect.
It means changes to the scaffold should be intentional enough that the team can
tell why a file, rule, or workflow exists.

## When To Add More

Add more structure only when the project needs it.

Common triggers include:

- more than one recurring role
- repeated confusion about who may decide what
- repeated confusion about what verification is required
- work spanning multiple sessions
- recurring failures that reveal missing trace fields
- domain-specific escalation or compliance needs
- different expertise tiers needing different autonomy levels

## What To Add Next

The next useful additions are often:

- a more explicit orchestration document
- reusable verification-contract definitions when acceptance criteria repeat
  across tasks
- autonomy or expertise profiles such as junior, regular, and senior
- domain-specific verification modules
- integration guidance for a specific execution system
- richer examples for common task patterns

For coding work in particular, treat `CODING_STANDARDS.md`,
`WORKFLOW_STANDARDS.md`, task specs, review records, or reusable verification
contracts as optional scaling tools.
They are not the default entry price for using the scaffold.

Use [execution-system-integration.md](execution-system-integration.md) when the
next pressure is runtime-specific.

Use
[domain-implementation-extensions.md](domain-implementation-extensions.md)
when the next pressure is domain-specific roles, verification, or overlays.

Use [../examples/research-to-design/README.md](../examples/research-to-design/README.md)
when you want one current example of a promoted domain-extension pattern.

If older starter-kit-derived patterns are relevant to your project, use
[starter-kit-adoption.md](starter-kit-adoption.md) as reference or migration
material rather than as the default baseline.
