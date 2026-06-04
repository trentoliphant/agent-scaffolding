# Starter Kit Reference And Migration

This guide explains how the older `starter_kit` reference implementation
relates to the current standard rewrite.

Use this guide when:

- you want to learn from the older starter-kit-derived workflow
- you are migrating existing material that follows that shape
- you want to extract useful patterns without treating the reference source as
  the standard itself

This is no longer the default builder path.

## What `starter_kit` Is Now

The `starter_kit` materials remain useful as:

- a reference implementation
- an extraction source for reusable patterns
- a migration aid for older document-structured workflows

They should not be treated as:

- the open standard itself
- the default baseline adoption path
- the final answer for non-coding domains

## When To Use This Guide

Use this guide if one of these is true:

- your team already has documents shaped like `PLAN.md`, `PROGRESS.md`, and
  `STEP_REVIEW.md`
- you want a richer document workflow than the minimal baseline
- you are porting older coding-oriented scaffold material into the new standard
- you want to understand where some of the repository's template assets came
  from

If none of those are true, start with [start-here.md](start-here.md) and
[minimal-adoption.md](minimal-adoption.md) instead.

## Current Sources

- full reference source: [../reference/starter_kit](../reference/starter_kit)
- reduced derived example:
  [../examples/structured-project-starter/README.md](../examples/structured-project-starter/README.md)
- imported template set:
  [templates/core](/Users/trentoliphant/Development/openteams/agent-scaffolding/templates/core)

## How To Read The Older Material

Read the older material as one implementation pattern, not as the standard.

The main translation is:

- `OPERATING_MODEL.md` maps mostly to orchestration and workflow guidance
- `SYSTEM_MODEL.md` maps to local system or harness definition
- `PLAN.md` and `PROGRESS.md` map to local planning and session state
- `STEP_REVIEW.md` maps to explicit verification structure
- template and process documents map to implementation conventions, not to the
  whole standard

## Recommended Migration Approach

If you are migrating from starter-kit-derived material:

1. Identify which documents express reusable standard concepts.
2. Separate implementation conventions from standard-core concepts.
3. Reframe review material as explicit verification contracts where helpful.
4. Add or clarify trace expectations and the self-evolution loop.
5. Keep older file shapes only when they still improve usability for your team.

## What Still Transfers Well

Useful patterns from the older material still include:

- explicit task decomposition
- explicit state and progress tracking
- separation of work artifacts from review artifacts
- durable history of meaningful structural change
- disciplined document updates for multi-session work

## What Needs Care During Migration

Be careful not to carry forward these assumptions without review:

- coding-first terminology as if it were domain-neutral
- repository workflow rules as if they were standard-core concepts
- implicit verification criteria hidden inside role expectations
- file layouts treated as if they were required by the standard

## Templates And Reference Material

The current `templates/core/` set remains available because it can still help
teams bootstrap a structured baseline.

However:

- the templates should be treated as baseline implementation assets, not the
  standard itself
- older reference material may remain more prescriptive than the new standard
- some imported templates may eventually be revised or reclassified as the
  rewrite continues

## Adoption Rule

Start from the minimal standard path when possible.

Move to starter-kit-derived material only when:

- you need migration help
- you need a richer document workflow immediately
- you are extracting reusable patterns from older reference material
