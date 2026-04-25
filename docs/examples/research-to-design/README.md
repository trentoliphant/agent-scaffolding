# Research-To-Design Example

This example is the repository's first promoted domain-extension pattern.

This example shows a non-software domain harness where research work feeds a
design decision.

It uses the same baseline shape as the other examples, then adds a small
artifact layer for domain-specific outputs.

## Example Context

Imagine a service organization that wants to redesign how new clients enter
its intake workflow.

The team first needs to understand:

- how intake works today
- where friction appears
- which constraints are real
- which questions still need answers

Then the team needs to turn those findings into a clearer proposed workflow.

## Example Structure

```text
AGENTS.md
SYSTEM_MODEL.md
PLAN.md
PROGRESS.md
state/
  current.md
artifacts/
  research/
    landscape.md
    synthesis.md
  design/
    intake-workflow.md
history/
  decisions/
    0001-separate-triage-from-full-intake.md
```

This example stays close to the baseline path while showing one domain
extension: document-first research and design artifacts.

## What This Example Demonstrates

This example demonstrates:

- a non-coding domain implementation
- a research phase that produces explicit findings
- a design phase that turns findings into a proposed workflow
- a visible handoff between task modes
- verification that changes by mode without changing scaffold categories
- a reusable extension pattern that builders can adapt for other
  document-first domains

## Extension Pattern Summary

The reusable pattern in this example is:

- domain roles split across research, design, and acceptance
- mode-specific verification contracts for research and design work
- domain artifacts kept visible instead of hidden inside general project state
- a handoff rule that lets accepted research become design input

Builders can reuse that pattern in domains such as:

- service operations improvement
- policy analysis feeding operating design
- product discovery feeding workflow design
- audit or assessment work feeding implementation planning

The domain nouns may change.
The extension categories stay recognizable.

## Mapping Back To The Standard

The files map to the standard this way:

- `AGENTS.md` defines local agent behavior and escalation expectations
- `SYSTEM_MODEL.md` defines roles, task types, verification contracts, trace,
  and orchestration
- `PLAN.md` defines the intended work sequence
- `PROGRESS.md` tracks active work, actor, verification state, and trace state
- `state/current.md` preserves continuity across sessions
- `artifacts/research/` holds research outputs that establish what is known
- `artifacts/design/` holds design outputs that turn findings into decisions
- `history/decisions/` records durable structural rationale

The extension categories map back to the standard this way:

- domain roles: sponsor, researcher, designer, verifier
- domain verification contracts: evidence sufficiency, synthesis coherence,
  workflow clarity, decision traceability
- domain artifacts: research landscape, synthesis, workflow proposal
- orchestration overlay: accepted research feeds design rather than remaining
  an isolated artifact layer

## Verification Contrast

The most important teaching point in this example is that verification differs
by mode without becoming hidden:

- research verification asks whether claims are supported, limitations are
  visible, and gaps are named
- design verification asks whether the workflow is coherent, decisions are
  explicit, and tradeoffs are documented

Both are still verification contracts.
The content changes, but the scaffold category does not.

## Example Flow

The orchestration can stay simple:

1. Investigate the current intake process and constraints.
2. Record findings in a research landscape artifact.
3. Synthesize the findings into a smaller set of actionable conclusions.
4. Use those conclusions to draft a proposed intake workflow.
5. Record one durable structural decision.

## Why This Example Matters

The minimal example proves the harness can stay small.
The software-project example shows how the harness can scale in a coding
context.

This example fills a different gap:

- it is document-first
- it is non-software
- it shows a real handoff between two work modes
- it keeps domain-specific material visible without redefining the standard
- it demonstrates what should become an example before it becomes a template

## How To Reuse This Pattern

Reuse this pattern when:

- one work mode discovers or evaluates
- a later work mode decides, designs, or proposes
- each mode needs a different verification contract
- the handoff between modes should stay inspectable

Adapt the nouns and artifacts locally, but keep these distinctions explicit:

- findings versus decisions
- mode-specific verification versus generic review language
- domain artifacts versus shared scaffold categories
- durable rationale versus active project state

## What To Read Next

Use [../../guide/domain-implementation-extensions.md](../../guide/domain-implementation-extensions.md)
when you want to specialize this pattern for another domain.

Use [../../guide/execution-system-integration.md](../../guide/execution-system-integration.md)
when the project needs explicit runtime integration.
