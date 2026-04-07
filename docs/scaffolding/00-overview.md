# Scaffolding Overview

This section defines the scaffolding system itself.

It describes the conceptual parts of the system and the boundaries between them. It does not try to teach adoption step by step, it does not serve as a project-specific example, and it does not directly document external reference implementations.

## Purpose

The scaffold exists to make AI-assisted work more structured, inspectable, and durable.

It is meant to help teams and individual builders move beyond ad-hoc chat workflows by making the working system explicit:

- what responsibilities exist
- how work is shaped
- how review is applied
- how context is preserved
- how decisions accumulate over time

## The Main Components

The scaffold distinguishes between:

- principles
- roles
- tasks
- review types
- orchestration
- session state
- history and decisions

These components are related but not interchangeable.

## Layer Map

This repository separates four kinds of durable documentation plus current-state material:

- `docs/scaffolding/` for system definition
- `docs/guide/` for how to apply the system
- `docs/examples/` for concrete applications
- `docs/reference/` for working reference implementations and extraction sources

In addition:

- `state/` for the current development frontier of this repository

That separation matters because a system can be well-defined but hard to use, easy to imitate but conceptually unclear, or strongly influenced by real working systems whose instance-level documents should not be mistaken for the scaffold itself.

## Reading Paths

If you are a builder:

- start with [../guide/start-here.md](../guide/start-here.md)
- then read [../guide/minimal-adoption.md](../guide/minimal-adoption.md)
- use this section when you need sharper definitions

If you are a contributor:

- read this section in order
- use [../../CONTRIBUTING.md](../../CONTRIBUTING.md) for repository workflow
- use [../reference/README.md](../reference/README.md) when a real working system is relevant to scaffold refinement
- consult [../../history/decisions/0001-repository-structure.md](../../history/decisions/0001-repository-structure.md) for the current structural rationale
- consult [../../history/decisions/0002-reference-implementations-and-extraction-sources.md](../../history/decisions/0002-reference-implementations-and-extraction-sources.md) for how reference implementations relate to the scaffold

## What Good Scaffolding Should Achieve

A useful scaffold should:

- define boundaries clearly
- remain readable to humans
- support iterative refinement
- preserve important context across sessions
- be adoptable without excessive upfront design

The rest of this section defines the scaffold in terms of those goals.
