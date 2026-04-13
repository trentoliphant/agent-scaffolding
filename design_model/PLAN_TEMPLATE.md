# DESIGN PLAN — [Project Name]

## Overview

This document defines the phases, sequencing, and steps for the design
phase of [Project Name]. Each step produces a specific design artifact.
Implementation planning begins only after the design phase is complete
or explicitly scoped to begin in parallel.

The plan is based on PROJECT_CHARTER.md and the domain being designed.
Steps are the execution instructions for the design agent.

---

## Guiding principles

[Copy from PROJECT_CHARTER.md or add design-phase-specific principles
here. These should reflect the project's core design philosophy.]

-
-
-

---

## Phase 1 — Domain Modeling

**Goal:** Establish the canonical entities, their relationships, invariants,
and constraints. This is the foundation all later design depends on.
No workflow, boundary, or technical design should proceed until the
domain model is stable.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 1.1 | Initialize design foundation | PROJECT_CHARTER.md, PLAN.md, PROGRESS.md | Confirm charter, create plan, establish state documents |
| 1.2 | Define core entities | domain/entities.md | Canonical entity list with purposes, responsibilities, key attributes |
| 1.3 | Define entity relationships | domain/relationships.md | Cardinality, ownership, dependency between entities |
| 1.4 | Define core invariants | domain/invariants.md | Hard rules that must always hold across the domain |
| 1.5 | Define domain constraints | domain/constraints.md | What is explicitly excluded or deferred from each entity |
| 1.6 | Review and stabilize domain model | — | Resolve cross-artifact inconsistencies; promote to Stable |

---

## Phase 2 — Workflow Modeling

**Goal:** Define the key processes in terms of states, transitions, actors,
and rules. Depends on a stable domain model.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 2.1 | Identify workflows | workflows/index.md | Canonical list of workflows with brief descriptions |
| 2.2 | Define [workflow 1] | workflows/[name].md | States, transitions, actors, invariants |
| 2.3 | Define [workflow 2] | workflows/[name].md | |
| ... | | | Add one step per significant workflow |
| 2.N | Review and stabilize workflows | — | Resolve conflicts with domain model; promote to Stable |

---

## Phase 3 — Boundary and Integration Definition

**Goal:** Define what this system owns versus what it defers, and how it
interacts with adjacent systems or future phases.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 3.1 | Define system boundaries | boundaries/system_boundaries.md | What this system owns, what it explicitly does not |
| 3.2 | Define external dependencies | boundaries/external_dependencies.md | What adjacent systems this depends on and how |
| 3.3 | Define integration surfaces | boundaries/integrations.md | APIs, import/export, data exchange points |
| 3.4 | Review and stabilize boundaries | — | Resolve conflicts; promote to Stable |

---

## Phase 4 — Compliance and Constraint Surface

**Goal:** Make explicit the regulatory, legal, and professional standard
constraints that shape the design. Produces a reviewable document
suitable for legal or domain expert review before implementation begins.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 4.1 | Map compliance surface | compliance/compliance_surface.md | Regulatory and legal areas that touch the system |
| 4.2 | Define compliance constraints | compliance/constraints.md | Specific rules each compliance area imposes on design |
| 4.3 | Identify review requirements | compliance/review_requirements.md | What needs legal or expert review before implementation |
| 4.4 | Review and stabilize compliance surface | — | Human review required before promoting to Stable |

---

## Phase 5 — Technical Architecture Sketch

**Goal:** Produce a technology-level architecture that implementation can
begin from. Depends on stable domain, workflow, boundary, and compliance
artifacts.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 5.1 | Define technology stack | architecture/stack.md | Language, framework, storage, key libraries |
| 5.2 | Sketch data model | architecture/data_model.md | Tables/collections, key relationships, migration approach |
| 5.3 | Define API surface | architecture/api_surface.md | Key endpoints, request/response shapes, auth approach |
| 5.4 | Define deployment model | architecture/deployment.md | Local-first vs hosted, environment structure |
| 5.5 | Review and stabilize architecture | — | Human review required; produces SYSTEM_MODEL.md for implementation |

---

## Dependencies

[A map of which steps depend on which other steps. This is what makes
parallelization decisions possible.]

| Step | Depends on |
|------|-----------|
| 1.2 | 1.1 |
| 1.3 | 1.2 |
| 1.4 | 1.2 |
| 1.5 | 1.2, 1.3, 1.4 |
| 1.6 | 1.2–1.5 |
| 2.1 | 1.6 |
| 2.x | 2.1, 1.6 |
| 3.x | 1.6, 2.N |
| 4.x | 1.6 (can run in parallel with phases 2–3) |
| 5.x | 1.6, 2.N, 3.4, 4.4 |

---

## Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
