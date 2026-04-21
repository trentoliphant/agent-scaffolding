# Baseline Implementation Guidance

This guide explains how baseline implementation guidance should relate to the
open standard.

The baseline implementation exists to demonstrate the standard in a practical,
minimal form.

It should help builders start quickly without turning one example
implementation into the definition of the standard itself.

## What Baseline Guidance Is For

Baseline guidance should show:

- the smallest useful document and workflow shape
- one practical way to express the standard's core modules
- how a builder can start without adopting every optional extension
- where local implementation choices begin

Its job is to make adoption easier, not to freeze one operating model as the
only valid one.

## What Baseline Guidance Must Not Do

Baseline guidance should not:

- redefine the standard in implementation-specific language
- require one runtime, model provider, or storage system
- imply one repository shape is mandatory for all projects
- treat one role mapping or orchestration pattern as universally correct
- hide implementation choices as if they were standard-core concepts

If a builder should be able to swap it out without breaking cross-domain
understanding, it probably belongs in the baseline or implementation layer, not
in the core standard.

## The Recommended Relationship

Use this three-layer relationship:

- `docs/scaffolding/`: define the reusable standard and its minimum contracts
- `docs/guide/`: explain how to adopt the standard in a practical minimal way
- `templates/` and `docs/examples/`: demonstrate one or more baseline starting
  shapes

That separation lets the standard stay portable while still giving builders a
clear starting point.

## What The Baseline Should Demonstrate

A baseline implementation should demonstrate at least:

- how a project expresses roles, tasks, verification, traces, and durable
  decisions
- how a minimal task cycle moves from execution to verification to trace
  capture
- how a builder can start small and add extensions later
- which parts are illustrative defaults rather than required standard law

This means the baseline should be concrete enough to copy, but explicit enough
to trim, rename, or replace.

## What Belongs In Baseline Guidance

Baseline guidance is the right place for:

- a recommended minimal file set
- a recommended first workflow loop
- example role names
- example document shapes
- practical adoption heuristics
- notes on when to add optional modules

These help builders move, but they should be presented as defaults, examples,
or recommendations rather than universal requirements.

## What Stays In The Standard

The standard should continue to define:

- the core module map
- the minimum harness contracts
- the minimum trace and verification expectations
- the distinction between state, traces, history, and implementation details
- the core-versus-extension boundary

Those concepts should remain valid even if a builder uses a different file
layout, different role names, or a different execution system.

## Heuristic For Boundary Decisions

When deciding where guidance belongs, ask:

1. Would this still be true across many domains and implementations?
2. Is this required for portability or inspectability?
3. Is this merely one useful way to demonstrate the standard?

If the answer to the third question is yes, it belongs in baseline guidance.

## Baseline Design Rule

The baseline should act like a reference starting shape, not a hidden command
to copy every file unchanged.

Good baseline guidance should let a builder say:

- I understand the standard
- I can start from this shape
- I know what I may safely change
- I know which changes are local implementation choices

If the baseline makes those boundaries harder to see, it is too prescriptive.
