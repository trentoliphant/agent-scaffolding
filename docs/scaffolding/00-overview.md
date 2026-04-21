# Scaffolding Overview

This section defines the scaffolding standard itself.

The scaffold is now framed as an open standard for domain harnesses or
domain-specific guardrails that coordinate work across human and machine
agents.

It is meant to stay:

- modular
- domain-agnostic at the standard level
- model-agnostic
- execution-system-agnostic
- inspectable by humans
- able to improve through structured learning from usage

It does not try to prescribe one runtime, one model provider, one repository
shape, or one proprietary domain implementation.

## Purpose

The scaffold exists to make agentic systems more structured, inspectable, and
evolvable.

It should help builders define:

- what work is being attempted
- which roles may perform it
- what autonomy those roles have
- what must be verified
- what trace of execution is preserved
- what changes should be learned from repeated use

## What The Standard Defines

The standard defines reusable structure for domain harnesses:

- principles
- roles and role boundaries
- tasks and handoffs
- verification contracts
- orchestration
- trace capture
- session state
- history and decisions
- self-evolution loops

These are the parts of the harness that should remain legible and transferable
across domains, models, and execution systems.

## What The Standard Does Not Define

The standard does not require:

- one specific model
- one execution engine
- one storage format
- one domain vocabulary
- one commercial packaging model
- one fixed assignment of roles to humans or machines

Those choices belong to implementations unless a cross-domain rule is needed in
the standard itself.

## Standard, Baseline Implementation, And Domain Implementations

This repository should distinguish between three related but different things:

- the open standard: the reusable contract and conceptual structure
- the baseline implementation: a practical, minimal way to adopt the standard
- domain implementations: domain-specific harnesses built on top of the
  standard

That distinction matters because a domain harness may extend the standard
substantially without redefining the standard itself.

## Core Module Map

The current conceptual map of the standard has two layers: core modules and
optional extensions.

### Core modules

The core modules are:

1. Principles
2. Roles and responsibility boundaries
3. Tasks and handoffs
4. Verification contracts
5. Orchestration
6. Trace contract
7. Session state
8. History and decisions
9. Self-evolution loop

These modules should remain portable across domains.

Every domain harness that claims to implement the standard should make each of
those modules explicit enough to answer four portable questions:

- how work is assigned
- how work is judged
- what evidence is preserved
- how the harness improves from repeated use

The detailed minimum contract for those modules is defined in
[20-components-and-boundaries.md](20-components-and-boundaries.md).

### Optional extensions

Optional extensions may include:

- autonomy or expertise profiles such as junior, regular, and senior
- workflow standards for a specific repository or operating environment
- integration guidance for a specific execution system
- domain-specific task libraries and verification criteria
- regulated-domain controls or compliance overlays
- marketplace or packaging conventions

Extensions are important, but they should plug into the core rather than blur
the core.

## Reading Paths

If you are a builder:

- read this section in order
- focus first on the core module map and the boundary rules
- treat optional extensions as additions, not prerequisites

If you are a contributor:

- read this section in order
- use [../../CONTRIBUTING.md](../../CONTRIBUTING.md) for repository workflow
- consult [../../history/decisions/0006-scaffold-is-reframed-as-an-open-standard-for-domain-harnesses.md](../../history/decisions/0006-scaffold-is-reframed-as-an-open-standard-for-domain-harnesses.md)
  for the current framing decision
- use [../reference/README.md](../reference/README.md) when older or external
  materials are relevant to the rewrite

## What Good Scaffolding Should Achieve

A useful standard should:

- let adopters start small
- support mixed human and machine systems cleanly
- separate execution from verification
- preserve evidence from real task execution
- support improvement without hiding why the harness changed
- remain understandable to a thoughtful human reader

The rest of this section defines the standard in terms of those goals.
