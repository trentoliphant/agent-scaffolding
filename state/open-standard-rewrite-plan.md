# Open Standard Rewrite Plan

This document tracks the active rewrite initiative that reframes the repository
from a mostly coding-oriented scaffold into an open standard for domain
harnesses or domain-specific guardrails.

It is an execution plan for repository evolution, not part of the scaffold
definition itself.

## Status

- overall status: in progress
- current phase: direction and architecture definition
- current focus: establish the standard's scope, modules, and rewrite boundary

## Completed

The following clarification work is complete for this initiative:

- the repository purpose has been reframed around an open standard for domain
  harnesses
- the need for mixed human and machine role assignment has been made explicit
- modularity is now a primary design requirement
- model-agnostic and execution-system-agnostic positioning has been made
  explicit
- traces, verification contracts, and self-evolution have been identified as
  first-class additions
- the possibility of separating the standard from domain implementations into
  multiple repositories has been identified as a live structural option
- the standard's module map and minimum harness contracts have been defined in
  the canonical scaffolding docs
- the baseline trace convention and verification verdict flow have been defined
  in the canonical scaffolding docs
- baseline implementation guidance has been separated from the standard more
  explicitly in the builder-facing guide layer
- the repository-status guide now gives a more refined classification of
  current, transitional, reference, legacy, and incubating materials
- top-level repository navigation now routes builders and contributors using
  the refined material classification
- verification is now modeled more explicitly as a reusable contract, distinct
  from roles and orchestration
- the self-evolution loop now defines which outputs belong in session state
  versus durable documents, history, and decisions

## Remaining Work

The main work still remaining in this initiative is:

- define the minimal complete standard
- clarify how expertise tiers map to responsibility, autonomy, and review

## Next Step

The immediate next step is:

1. clarify how expertise tiers map to responsibility, autonomy, and review

Use this decision rule:

- add a concept to the standard core only if it is reusable across domains and
  improves inspectability, interoperability, or scaffold evolution

## Goal

Use this repository to define an open standard that allows different domain
harnesses to share one common structure for:

- roles and role boundaries
- tasks and handoffs
- verification and verdict handling
- traces from execution
- orchestration
- current state
- durable decisions
- scaffold improvement over time

The standard should support users first while keeping contributor guidance
clear enough for safe evolution of the standard itself.

## Working Interpretation

The current working interpretation is:

- the open standard is the durable shared contract
- a baseline implementation may demonstrate the standard without exhausting it
- domain implementations instantiate the standard for specific domains
- domain implementations may be open or proprietary
- domain implementations should be able to mix human and machine agents within
  the same structural framework

## Core Architecture Questions

The main architecture questions to resolve are:

1. What modules belong in the core standard?
2. What extension points should domain implementations be allowed to define?
3. What minimum trace structure should every implementation return?
4. How should self-evolution outcomes feed back into standard documents,
   implementation documents, and history?
5. How should autonomy levels or expertise tiers be represented?
6. How should the standard describe integration with common execution systems
   without becoming dependent on them?

## Proposed Work Sequence

### Phase 1. Reframe the repository

Establish the new purpose, active initiative, and decision history.

Deliverables:

- updated state documents
- decision record for the new framing
- a rewrite plan anchored to the new purpose

### Phase 2. Define the standard architecture

Define the core modules, extension points, and minimum contracts.

Likely outputs:

- revised `docs/scaffolding/` structure
- explicit treatment of traces, verification, and self-evolution
- clarified terminology for standard, baseline implementation, and domain
  implementation

### Phase 3. Redesign the builder path

Create a clean user-facing path for adopting the standard.

Likely outputs:

- rewritten `README.md`
- rewritten builder guides
- a clearer baseline implementation path
- integration guidance for common execution systems

### Phase 4. Reclassify existing materials

Decide which current materials remain core, move to reference, or become
legacy/migration aids.

Likely outputs:

- reference or legacy treatment for older coding-first materials
- clarified status of starter-kit-derived content
- clarified status of domain adapter materials

### Phase 5. Define contribution and ecosystem boundaries

Clarify how external contributors and domain experts participate.

Likely outputs:

- contributor guidance for standard changes
- extension guidance for domain implementations
- a decision on one-repo versus multi-repo structure when justified

## Constraints

- keep the standard domain-agnostic
- keep the standard model-agnostic
- keep the standard execution-system-agnostic
- preserve human legibility and inspectability
- keep the user path primary even as contributor structure grows
- do not hard-code one company's proprietary domain patterns into the core
  standard without explicit justification

## Closing Note

This initiative should be treated as a real reframing rather than a wording
refresh.

The repository already contains useful structure, but the new standard should
be allowed to replace that structure where replacement improves clarity,
modularity, and long-term interoperability.
