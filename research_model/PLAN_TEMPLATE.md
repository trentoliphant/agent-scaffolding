# RESEARCH PLAN — [Project Name]

## Overview

This document defines the phases, sequencing, and steps for the research
phase of [Project Name]. Each step produces a specific research artifact.
Design work begins only after the research phase is complete or explicitly
scoped to begin in parallel based on sufficiently stable research findings.

The plan is based on PROJECT_CHARTER.md and the questions being
investigated. Steps are the execution instructions for the research agent.

---

## Guiding principles

[Copy from PROJECT_CHARTER.md or add research-phase-specific principles
here. These should reflect the project's core investigative philosophy.]

-
-
-

---

## Phase 1 — Scoping and Foundation

**Goal:** Establish the research foundation — confirm scope, identify the
core questions, and set up the investigation infrastructure. No broad
survey work should proceed until the scope is confirmed and the plan
is reviewed.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 1.1 | Initialize research foundation | PROJECT_CHARTER.md, PLAN.md, PROGRESS.md | Confirm charter, create plan, establish state documents |
| 1.2 | Define research questions | research/landscape/questions.md | Canonical list of questions this research must answer, with priority and dependencies |
| 1.3 | Identify known starting points | research/landscape/prior_knowledge.md | What is already known, assumed, or believed — with confidence ratings and sources |
| 1.4 | Define investigation methodology | research/landscape/methodology.md | How each question type will be investigated, what tools will be used, what counts as sufficient evidence |
| 1.5 | Review and confirm scope | — | Human review of scope, questions, and methodology before proceeding |

---

## Phase 2 — Landscape Survey

**Goal:** Establish a broad understanding of the terrain. Identify what
exists, what the major categories are, and where deep investigation is
needed. Breadth over depth — the goal is coverage, not completeness
on any single item.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 2.1 | Survey [area 1] | research/landscape/[area_1].md | Landscape survey of the first major area |
| 2.2 | Survey [area 2] | research/landscape/[area_2].md | |
| 2.3 | Survey [area 3] | research/landscape/[area_3].md | |
| ... | | | Add one step per major survey area |
| 2.N | Consolidate landscape findings | research/landscape/landscape_summary.md | Cross-survey themes, priority areas for deep investigation, initial gap identification |

---

## Phase 3 — Deep Investigation

**Goal:** Conduct focused, evidence-based investigation of the areas
identified as highest priority during landscape survey. Depth over
breadth — each step should produce findings backed by direct
observation or authoritative sources.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 3.1 | Investigate [topic 1] | research/analysis/[topic_1].md | Deep analysis with evidence |
| 3.2 | Investigate [topic 2] | research/analysis/[topic_2].md | |
| 3.3 | Evaluate [tool or method 1] | research/evaluations/[tool_1].md | Structured evaluation against defined criteria |
| 3.4 | Assess feasibility of [approach] | research/analysis/[approach]_feasibility.md | |
| ... | | | Add steps based on phase 2 findings |
| 3.N | Review deep investigation findings | — | Cross-check findings, identify contradictions, update landscape summary |

**Note:** Phase 3 steps are expected to be revised after phase 2
completes. The initial plan should include placeholder steps based
on the charter's research questions, but the specific investigation
targets will be refined based on landscape findings. This is a class
3 plan change and is expected — not an error.

---

## Phase 4 — Synthesis and Gap Analysis

**Goal:** Combine all findings into a coherent picture. Identify what
was learned, what remains unknown, and where the gaps are between
current understanding and what is needed for the next phase of work
(design, implementation, or further research).

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 4.1 | Synthesize findings | research/synthesis/findings_synthesis.md | Cross-cutting themes, key takeaways, confidence assessment |
| 4.2 | Conduct gap analysis | research/synthesis/gap_analysis.md | What is known vs what is needed, with severity ratings |
| 4.3 | Identify risks and unknowns | research/synthesis/risks_and_unknowns.md | What could go wrong, what we still don't know, what assumptions are fragile |
| 4.4 | Review and stabilize synthesis | — | Human review of synthesized findings before recommendations |

---

## Phase 5 — Recommendations

**Goal:** Produce actionable recommendations based on research findings.
These recommendations become inputs to the next phase of work — whether
that is a design project, an implementation project, or a decision by
stakeholders.

| Step | Title | Artifact | Notes |
|------|-------|----------|-------|
| 5.1 | Draft recommendations | research/recommendations/recommendations.md | Specific actions recommended, with rationale and evidence references |
| 5.2 | Define transition criteria | research/recommendations/transition_criteria.md | What must be true before moving from research to the next phase |
| 5.3 | Produce research handoff document | research/recommendations/handoff.md | Summary for the design or implementation team — what they need to know |
| 5.4 | Final review | — | Human review of recommendations and handoff document |

---

## Dependencies

[A map of which steps depend on which other steps. Research dependencies
are often softer than design dependencies — a survey step may inform
but not strictly block an investigation step.]

| Step | Depends on | Dependency type |
|------|-----------|-----------------|
| 1.2 | 1.1 | Hard — cannot start without charter |
| 1.3 | 1.2 | Hard — need questions defined first |
| 1.4 | 1.2 | Hard — methodology follows questions |
| 1.5 | 1.2–1.4 | Hard — scope review requires all foundation docs |
| 2.x | 1.5 | Hard — survey requires confirmed scope |
| 2.N | 2.1–2.(N-1) | Soft — summary benefits from all surveys but can draft incrementally |
| 3.x | 2.N | Soft — investigation targets come from survey, but can begin on high-confidence areas before survey completes |
| 3.N | 3.1–3.(N-1) | Hard — review requires all investigations complete |
| 4.x | 3.N | Hard — synthesis requires completed investigations |
| 5.x | 4.4 | Hard — recommendations require stable synthesis |

### Dependency types

**Hard** — the step cannot meaningfully begin until the dependency is
complete. Starting early would produce work that needs to be redone.

**Soft** — the step benefits from the dependency being complete but can
begin with partial information. Findings may need revision when the
dependency completes.

---

## Plan mutation expectations

Unlike design plans, research plans are expected to mutate significantly
during execution. Common mutations include:

- Phase 3 steps being added, removed, or reordered after phase 2 findings
- New investigation branches appearing when findings reveal unexpected
  complexity
- Steps being split when a topic turns out to be larger than expected
- Steps being merged when two topics turn out to be closely related

All plan mutations must be recorded in the decision log below and in
HISTORY.md.

---

## Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
