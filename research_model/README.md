# Research Model

> Status: Incubating
> Alignment: Not yet aligned with the current open-standard rewrite
> Intended role: Earlier research-oriented adapter material now treated as an
> extraction source
> Use it for: selective extraction of reusable patterns, not as a promoted
> example or current builder-path artifact

## What this is

This is earlier research-oriented adapter material for investigative and
analytical work.

It may still be useful as an extraction source for:

- evidence-discipline guidance
- research-specific verification ideas
- plan mutation rules
- research-oriented template structure

It is not currently part of the promoted example set.
Promote only extracted pieces that fill a builder need not already covered by
the current curated examples.

## When to use this adapter vs the design adapter

Use the **research adapter** when:
- The primary output is knowledge, not decisions
- You are discovering facts about an existing landscape
- You are evaluating tools, methods, or approaches for fitness
- You are assessing feasibility before committing to an approach
- You need to answer questions before you can define requirements
- The work is empirical — claims need evidence, not just rationale

Use the **design adapter** when:
- The primary output is a system design with decisions and tradeoffs
- You are defining entities, workflows, boundaries, and architecture
- You are making structural decisions that constrain implementation
- The inputs are well-understood enough to design against

Use them **in sequence** when:
- Research produces findings that become design inputs
- The research charter's transition plan points to a design project
- Research artifacts at Reviewed or Verified confidence become the
  "what is already known" section of a design project charter

## Structural parallel with design adapter

| Design adapter | Research adapter | Purpose |
|---------------|-----------------|---------|
| CLAUDE.md | CLAUDE.md | AI execution instructions |
| DESIGN_STANDARDS.md | RESEARCH_STANDARDS.md | Domain-specific artifact and quality standards |
| PLAN_TEMPLATE.md | PLAN_TEMPLATE.md | Phase and step sequencing |
| PROJECT_CHARTER_TEMPLATE.md | PROJECT_CHARTER_TEMPLATE.md | Scope, goals, constraints |
| STEP_SPEC_TEMPLATE.md | STEP_SPEC_TEMPLATE.md | Individual step definition |

## Key differences from design adapter

### Confidence markers instead of stability markers

Design uses Provisional → Stable → Locked (tracking decision settlement).
Research uses Draft → Reviewed → Verified (tracking evidence quality).

The concepts are parallel but the semantics differ. A "stable" design
decision means it won't change without escalation. A "reviewed" research
finding means it's well-sourced and internally consistent, but new
evidence could change it.

### Plan mutation is expected

Design plans change when the design reveals structural issues.
Research plans change routinely as early findings redirect investigation.
The research adapter explicitly normalizes plan mutation and provides
the "plan mutation expectations" section in the plan template.

### Evidence as a first-class concern

Design artifacts are self-contained — the decisions and rationale live
in the document. Research artifacts are backed by evidence that lives
separately in `research/evidence/`. The evidence discipline section
in RESEARCH_STANDARDS.md and the methodology section in step specs
are not present in the design adapter.

### Artifact types are different

Design produces: entity definitions, workflow models, boundary documents,
compliance surfaces, architecture sketches.

Research produces: landscape surveys, deep analyses, tool evaluations,
feasibility assessments, gap analyses, syntheses, recommendations.

### The rabbit hole problem

Design scope creep is usually about adding features or complexity.
Research scope creep is about following interesting tangents. The
research adapter includes the "investigation rabbit-hole rule" and
the "rabbit hole risks" section in step specs to address this
specifically.

## Files in this directory

- `CLAUDE.md` — AI execution instructions for research projects
- `RESEARCH_STANDARDS.md` — Standards for research artifacts and findings
- `PLAN_TEMPLATE.md` — Research plan template with investigation phases
- `PROJECT_CHARTER_TEMPLATE.md` — Research charter template
- `STEP_SPEC_TEMPLATE.md` — Research step spec template
- `README.md` — This file

## Integration status

This material remains in the incubating layer.

It should not be promoted wholesale into the main builder path.
Instead, use it as source material for selective extraction when the current
example set or guide layer reveals a real gap.
