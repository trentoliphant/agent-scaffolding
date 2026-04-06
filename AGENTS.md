# AGENTS.md

## Purpose

This repository defines and evolves a scaffolding system for AI-assisted work.

The goal is not simply to generate output, but to create a structured environment in which agents can operate with clear boundaries, explicit responsibilities, review criteria, and durable context.

This repository should be treated as the working source of truth for that scaffolding.

---

## Intended Use of the System

This repository serves two distinct but related purposes:

1. Defining a scaffolding system for AI-assisted work
2. Enabling that scaffolding to be applied in real projects

The system should not remain purely abstract or self-referential.
It must support practical use by builders.

The repository should evolve in a way that improves both:

* conceptual clarity (for contributors)
* practical usability (for builders)

---

## Audience Awareness

There are two primary audiences:

### 1. Builders (Primary Audience)

People using this scaffolding to structure AI-assisted systems.

They need:

* clear entry points
* practical guidance
* concrete examples
* minimal required context to get started

When making changes, consider:

* Can a new user understand how to apply this?
* Is there a clear starting point?
* Are concepts actionable, not just defined?

---

### 2. Contributors (Secondary Audience)

People evolving the scaffolding system itself.

They focus on:

* conceptual clarity
* system design
* refinement of structure
* consistency across layers

When making changes, consider:

* Are distinctions precise and well-defined?
* Does this improve the internal coherence of the system?

---

## Design Implication

When evaluating the repository, always consider both:

* **Is the system well-defined?**
* **Is the system usable?**

If usability is lacking, propose additions such as:

* guides
* examples
* simplified entry points

If conceptual clarity is lacking, refine:

* definitions
* boundaries
* terminology

---

## System vs Application Distinction

Maintain a clear separation between:

* **System Definition** (what the scaffolding is)
* **System Application** (how the scaffolding is used)

These should not be mixed within the same documents.

Preferred structure:

* `docs/scaffolding/` → system definition
* `docs/guide/` → how to use the system
* `docs/examples/` → concrete applications

When introducing content:

* Place it in the correct layer
* Do not collapse definition and usage into one artifact

---

## Primary Objectives

1. Define clear structures for agent-assisted work
2. Separate roles, tasks, reviews, and orchestration concerns
3. Preserve continuity across sessions through durable repo context
4. Support iterative refinement rather than repeated reinvention
5. Keep the system understandable by humans, not just usable by models
6. Ensure the system can be applied in real-world scenarios

---

## Working Style

* Prefer incremental refinement over wholesale rewrites
* Preserve existing terminology unless there is a clear reason to change it
* Make distinctions explicit when concepts are easily conflated
* When changing structure, explain the reasoning in the relevant document or commit message
* Keep documents readable, organized, and maintainable
* Avoid introducing abstraction unless it clarifies rather than obscures

---

## Core Principles

### 1. Separate Layers

Do not collapse distinct layers into one another.

Important distinctions include:

* facts vs interpretations vs asserted outputs
* roles vs tasks
* execution vs review
* current state vs historical decisions
* orchestration vs implementation
* system definition vs system application

Where ambiguity exists, preserve the distinction unless there is a deliberate decision to unify concepts.

---

### 2. Iteration Over Replacement

The system is expected to evolve.

Prefer editing and extending existing structures over replacing them.

Do not rewrite an entire file unless:

* explicitly requested, or
* the current structure is no longer viable

---

### 3. Structure Before Expansion

When new ideas are introduced, first determine where they belong.

Questions to ask:

* Is this a role?
* Is this a task pattern?
* Is this a review type?
* Is this orchestration logic?
* Is this session state or durable principle?
* Is this historical reasoning that belongs in decisions documentation?
* Is this system definition or system usage guidance?

---

### 4. Human Legibility Matters

The scaffolding must remain understandable to a thoughtful human reader.

Prefer:

* clear headings
* explicit definitions
* short explanatory sections
* stable terminology
* cross-references when needed

Avoid creating a system that only makes sense through accumulated model inference.

---

### 5. Context Should Be Durable

Important context should be promoted into repository files rather than left implicit in transient chat history.

If a concept repeatedly matters, capture it in the appropriate document.

---

### 6. Usability is Required

A well-defined system that cannot be applied is incomplete.

The repository should make it possible to:

* start small
* apply the scaffold incrementally
* understand how components interact in practice

---

## Conceptual Model

This repository assumes the system may include:

* **Principles** — foundational ideas and constraints
* **Roles** — responsibility-bearing agent positions
* **Tasks** — units of work
* **Review Types** — evaluation lenses applied across layers
* **Orchestration** — coordination, routing, sequencing, escalation
* **Session State** — current working focus and open questions
* **History / Decisions** — distilled evolution of understanding

These components are related but not interchangeable.

---

## Expected Agent Behavior

When working in this repository, the agent should:

1. Read relevant context files before making major edits
2. Update files in place whenever possible
3. Prefer precise local changes over broad restructuring
4. Preserve alignment across related documents
5. Call out inconsistencies when discovered
6. Surface unresolved design tension rather than hiding it
7. Distinguish between:

   * proposing a change
   * implementing a change
   * documenting a change
8. Avoid silently changing established meaning
9. Consider both system clarity and usability in every change

---

## Editing Rules

### Default Behavior

* Make the smallest change that correctly advances the work
* Do not reformat large sections unless needed for clarity
* Do not rename files or concepts casually
* Do not remove historical decisions without explicit reason

---

### When Introducing New Concepts

When adding a new concept:

* define it clearly
* place it in the correct layer
* connect it to related concepts
* note any unresolved ambiguity

---

### When Restructuring

If restructuring is needed:

* preserve underlying meaning unless intentionally revised
* update dependent files
* document the rationale for the change

---

## Review Guidance

Review is a cross-cutting concern, not automatically a role.

Review may apply to:

* planning
* architecture
* implementation
* documentation
* orchestration logic
* output quality
* boundary compliance

If there is uncertainty about whether something is a role or a review type, preserve that uncertainty explicitly.

---

## Usability Checks

When evaluating the repository, consider:

* Is there a clear starting point for a new user?
* Can this be applied without deep knowledge of the system?
* Are there examples of real usage?
* Are concepts actionable, not just defined?
* What is missing for real-world application?

If gaps exist, propose:

* guides
* examples
* simplified workflows

---

## Preferred Output Characteristics

Outputs in this repository should be:

* structured
* explicit
* layered
* iterative
* internally consistent
* easy to extend

Prefer clarity over polish and precision over rhetorical flourish.

---

## File Intent

Documents will typically fall into categories such as:

* overview
* principles
* roles
* review types
* orchestration
* task patterns
* session state
* decisions/history
* guides
* examples

New files should:

* have a clear purpose
* fit an existing category or justify a new one

---

## Change Philosophy

This repository is building a system, not collecting notes.

Changes should improve one or more of:

* conceptual clarity
* operational usefulness
* continuity across sessions
* consistency between layers
* usability by builders

If a change adds complexity without improving these, reconsider it.

---

## Practical Heuristic

Before making a change, ask:

1. What layer does this belong to?
2. What existing concept does it affect?
3. Is this durable or temporary?
4. Should this be added, revised, or recorded as a decision?
5. Does this make the system clearer or just more complex?
6. Does this improve usability for builders?

---

## Default Assumption

If the user is refining the system through conversation, the repository should be updated to reflect durable structure, not just the wording of the latest prompt.
