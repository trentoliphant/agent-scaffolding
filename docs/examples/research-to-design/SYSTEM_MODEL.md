# SYSTEM_MODEL.md

## Purpose

This local harness supports a service-operations team that wants to improve
client intake by moving through two explicit task modes:

- research, to understand the current process and its constraints
- design, to propose a clearer intake workflow based on those findings

The harness is meant to keep findings, decisions, verification, and durable
rationale separate and legible.

## Roles

### Sponsor

Responsible for:

- setting the objective
- accepting scope and tradeoff decisions
- deciding when the proposed workflow is ready to adopt

### Researcher

Responsible for:

- investigating the current intake process
- recording findings with a stated basis
- naming gaps, caveats, and open questions

### Designer

Responsible for:

- turning accepted findings into a proposed workflow
- making decisions and tradeoffs explicit
- identifying where unresolved questions still limit the design

### Verifier

Responsible for:

- applying the relevant verification contracts
- deciding whether artifacts are acceptable, need revision, or should be
  deferred

These roles may be filled by humans, machine agents, or mixed loops.
The role definition stays separate from the actor that fills it.

## Task Types

This harness uses four task types:

- investigate: gather observations, sources, or other evidence
- synthesize: combine findings into a smaller set of actionable conclusions
- design: produce a workflow proposal based on accepted findings
- review: apply verification contracts and determine next action

## Verification Contracts

### Evidence Sufficiency

Applies to research artifacts.

Checks whether:

- important claims have a stated basis
- limitations and caveats are visible
- open questions are named
- unsupported conclusions are avoided

Possible verdicts:

- accepted
- accepted_with_notes
- needs_revision

### Synthesis Coherence

Applies to synthesis artifacts.

Checks whether:

- findings are combined accurately
- contradictions or tensions are visible
- recommended next steps follow from the findings

Possible verdicts:

- accepted
- accepted_with_notes
- needs_revision

### Workflow Clarity

Applies to design artifacts.

Checks whether:

- the proposed workflow has clear stages and transitions
- roles and responsibilities are legible
- constraints and tradeoffs are explicit
- unresolved questions remain visible

Possible verdicts:

- accepted
- accepted_with_notes
- needs_revision

### Decision Traceability

Applies when a design choice becomes durable enough to preserve.

Checks whether:

- the decision is stated clearly
- alternatives or tensions are visible
- the rationale is durable enough to help later work

Possible verdicts:

- accepted
- needs_revision

## Trace Expectations

Each completed task cycle should preserve at least:

- task
- responsible role
- acting party
- output artifact
- verification contract used
- verdict
- next action

Research artifacts should also preserve the basis of important findings.
Design artifacts should preserve major tradeoffs and open questions.

## Orchestration

The intended flow is:

1. The sponsor defines the intake-improvement objective.
2. The researcher investigates the current process.
3. The verifier applies evidence sufficiency.
4. The researcher or sponsor produces a synthesis of findings.
5. The verifier applies synthesis coherence.
6. The designer proposes a revised intake workflow.
7. The verifier applies workflow clarity.
8. Durable structural choices are recorded as decisions.

The flow is directional but not one-way.
If design exposes a missing fact, the work can return to research before the
workflow is finalized.

## Local Extension Boundary

This example adds domain-specific research and design artifacts, but it still
maps back to the shared scaffold structure:

- roles remain roles
- task types remain tasks
- evidence and workflow checks remain verification
- artifact summaries remain trace
- the research-to-design handoff remains orchestration
- durable rationale remains history and decisions

## Extension Categories In This Example

This example uses four explicit extension categories:

- domain roles: sponsor, researcher, designer, verifier
- domain verification contracts: evidence sufficiency, synthesis coherence,
  workflow clarity, decision traceability
- domain artifacts: research landscape, synthesis, workflow proposal
- orchestration overlay: accepted findings become design inputs

Those categories are local to the domain implementation.
They are still recoverable as roles, verification, artifacts, and
orchestration when read against the standard.
