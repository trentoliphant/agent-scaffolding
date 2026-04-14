# RESEARCH STANDARDS

## Purpose

This document defines standards for research artifacts, research steps, and
research findings in a structured research project.

It governs how investigative work is written, organized, validated, and
maintained. Operating model, workflow practices, and execution governance
are defined elsewhere.

---

## Core principles

- Claims must be sourced and traceable
- Evidence and interpretation must be clearly separated
- Gaps and limitations are first-class findings
- Provisional findings are preferable to unsupported conclusions
- Confidence levels must be stated, not implied
- Scope boundaries prevent investigation sprawl
- Later phases depend on earlier phases being at least Reviewed

---

## Research artifact types

Research produces several distinct artifact types. Each has different
standards because they serve different purposes.

### Landscape survey

A broad inventory of what exists in a domain. Answers: "What is out
there?"

Purpose: Establish the terrain before deep investigation.
Typical contents: categorized inventory, brief descriptions, initial
assessment of relevance, identification of areas requiring deeper
investigation.

### Deep analysis

A focused investigation of a specific area identified during survey.
Answers: "How does this actually work?"

Purpose: Produce detailed understanding of a specific topic.
Typical contents: methodology, detailed findings, evidence references,
limitations, comparison to expectations.

### Tool or method evaluation

An assessment of whether a specific tool, library, or approach is
fit for purpose. Answers: "Can we use this? How well does it work?"

Purpose: Produce actionable assessment of fitness for purpose.
Typical contents: evaluation criteria, test methodology, results,
strengths, weaknesses, verdict, conditions under which the verdict
would change.

### Feasibility assessment

An analysis of whether a proposed approach is practical. Answers:
"Can this be done? What would it take?"

Purpose: Inform go/no-go or prioritization decisions.
Typical contents: approach description, requirements, risks, effort
estimate, dependencies, blocking unknowns, recommendation.

### Gap analysis

An identification of what is missing between the current state and
a desired state. Answers: "What don't we have that we need?"

Purpose: Drive prioritization and identify blockers.
Typical contents: desired state description, current state findings,
gaps identified, severity/impact of each gap, potential approaches
to closing each gap.

### Synthesis document

A consolidated view that combines findings from multiple research
artifacts into a coherent picture. Answers: "What does all of this
mean together?"

Purpose: Make accumulated research actionable.
Typical contents: key findings from source artifacts, cross-cutting
themes, contradictions or tensions, overall assessment, open
questions, recommendations for next steps.

### Recommendation document

A decision-ready summary that proposes specific actions based on
research findings. Answers: "What should we do?"

Purpose: Bridge from research to action (design, implementation,
or further investigation).
Typical contents: recommendation with rationale, evidence summary,
risks, alternatives considered, conditions for revisiting.

---

## Required properties of every research artifact

- Has a clear stated purpose
- Identifies what questions it addresses
- States the methodology or approach used
- Separates evidence from interpretation
- Identifies gaps, limitations, and caveats
- States confidence level (see below)
- Records open questions it surfaces
- Is understandable without oral explanation

---

## Confidence markers

Every research artifact carries one of three confidence markers:

**Draft** — the artifact captures initial findings but has not been
checked for completeness, accuracy, or consistency with other
artifacts. Claims may be unsourced. Downstream work should treat
draft findings as hypotheses.

**Reviewed** — the artifact has been checked for internal consistency,
claims are sourced, gaps are identified, and downstream work may
depend on it with appropriate caution. Changes are expected as new
evidence emerges but should be tracked.

**Verified** — the artifact has been validated against external
sources, tested where applicable, and reviewed by a human with
domain knowledge. Changes require explicit escalation.

Mark confidence explicitly at the top of each artifact. Default is
Draft until explicitly promoted.

---

## How to write a landscape survey entry

A landscape survey entry must include:

- **Name** — the canonical name of the thing being surveyed
- **Category** — what kind of thing it is within the survey taxonomy
- **Brief description** — one to three sentences describing what it
  does or what it is
- **Relevance** — why it matters to the research question, rated
  as high / medium / low / unclear
- **Status** — active, deprecated, experimental, etc.
- **Source** — where this information came from
- **Notes** — anything notable discovered during survey
- **Further investigation needed** — yes/no, and if yes, what
  questions remain

### Example structure

```
### auditwheel

Category: Wheel packaging tool
Description: A tool that adds external shared libraries into Linux
wheel files so they are self-contained. Part of the PyPA toolchain.
Used by most scientific Python packages to produce manylinux wheels.
Relevance: High — this is the primary tool that creates the vendored
wheels we are trying to unvendor.
Status: Active, maintained by PyPA
Source: https://github.com/pypa/auditwheel, PyPA documentation
Notes: Works by copying .so files into the wheel and patching
RPATH/RUNPATH. The inverse operation (removing .so files and
relinking) is not natively supported.
Further investigation needed: Yes — need to understand exactly what
metadata auditwheel adds and whether it can be used to identify
what was vendored.
```

---

## How to write a finding

A finding is a discrete factual claim produced by research. Findings
are the atoms of research artifacts — they are what get combined
into analyses and syntheses.

Every finding must:
- State the claim clearly and specifically
- Cite the evidence basis (observation, source, inference, or expert)
- State the confidence level: confirmed, probable, uncertain
- Note any caveats or conditions under which the finding might not hold

### Finding format

```
**Finding:** [clear factual claim]
**Basis:** [direct observation / source citation / inference / expert input]
**Confidence:** [confirmed / probable / uncertain]
**Caveats:** [conditions, limitations, or exceptions]
```

### Example

```
**Finding:** numpy 1.26.4 manylinux wheel contains 14 vendored .so
files including libopenblas64_.so (63MB) and libgfortran.so
**Basis:** Direct observation — ran `unzip -l` and `ldd` on
numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.whl
**Confidence:** Confirmed
**Caveats:** Specific to this version and platform. Other platforms
and versions may differ.
```

---

## How to write an evaluation

An evaluation assesses fitness for purpose. It is not a review or
opinion — it is a structured assessment against defined criteria.

Every evaluation must include:

- **Subject** — what is being evaluated
- **Purpose** — what it is being evaluated for
- **Criteria** — the specific dimensions of assessment, defined
  before testing begins
- **Methodology** — how the evaluation was conducted
- **Results** — findings organized by criteria
- **Verdict** — overall assessment with explicit rationale
- **Conditions for revisiting** — what would change the verdict

Define criteria before conducting the evaluation. Do not let results
shape criteria retroactively.

---

## How to handle open questions

An open question is a research question that has not yet been
answered. Open questions are first-class artifacts — they must be
tracked, not buried.

Every open question must include:

- **Question** — what needs to be answered
- **Why it matters** — what downstream work it blocks or affects
- **What we know so far** — any partial information available
- **Investigation approach** — how this could be answered
- **Owner** — who is responsible for resolving it (human, specific
  future step, or deferred)

Open questions do not block a step from completing unless they are
explicitly marked as blocking. A step may complete with open
questions carried forward, provided those questions are recorded
and their downstream impact is noted.

Research steps frequently generate more open questions than they
resolve. This is expected and healthy.

---

## Research step completeness criteria

A research step is complete when:

- The specified artifact exists and has a confidence marker
- All questions the step was meant to address are either answered
  or explicitly recorded as open
- All claims in the artifact have a stated evidence basis
- Gaps and limitations are identified
- Dependencies on other research artifacts are identified
- No out-of-scope investigation was performed
- PROGRESS.md and HISTORY.md are updated per the completion gate

A research step is not complete because:
- The artifact looks thorough
- The artifact is long
- No open questions remain (open questions are expected and normal)
- All findings are positive (negative and null findings are valuable)

---

## Evidence management

Evidence is the raw material that supports findings. It must be
preserved so findings can be verified or re-evaluated.

### What counts as evidence

- Command output (terminal logs, tool output)
- File contents (inspected files, configuration, source code)
- Screenshots or recordings of tool behavior
- Data files (CSV exports, JSON responses)
- Source documents (papers, documentation pages, READMEs)
- Conversation records (expert input with attribution)

### Evidence storage rules

- Store evidence files under `research/evidence/`
- Use descriptive filenames: `numpy_wheel_so_inventory.txt`,
  not `output.txt`
- Reference evidence from research artifacts by relative path
- Do not embed large evidence blocks inline in research
  artifacts — reference them
- Small evidence (a few lines of command output) may be quoted
  inline if it aids readability

### Evidence does not expire

Once committed, evidence should not be modified or deleted. If
evidence is superseded by newer findings, create new evidence
and note the supersession in the research artifact.

---

## Draft vs Reviewed promotion rules

Promote an artifact from Draft to Reviewed when:

- All claims have a stated evidence basis
- Internal consistency has been checked
- Gaps and limitations are explicitly stated
- The artifact has been checked against other Reviewed artifacts
  for contradictions
- Open questions are recorded with investigation approaches

Promote from Reviewed to Verified only when:

- A human with domain knowledge has reviewed the findings
- Key claims have been cross-referenced against independent sources
- Reproducible findings have been reproduced at least once
- The artifact is being depended upon for decision-making

Do not promote confidence markers automatically. Promotion is an
explicit act recorded in HISTORY.md.

---

## Scope discipline for research steps

- Do not investigate future-phase topics within a current-phase step
- Do not make design decisions in research artifacts
- Do not resolve open questions by making undocumented assumptions
- Do not treat a hypothesis as a finding
- Do not suppress negative or null results

If scope creep is tempting, classify it as an issue per
OPERATING_MODEL.md before acting.

### The investigation rabbit-hole rule

Research naturally uncovers interesting tangents. When a tangent
appears:

1. Record it as an open question in the current artifact
2. Assess whether it affects the current step's findings
3. If it does not, continue with the current step
4. If it does, classify as a class 2 or class 3 issue
5. Do not follow the tangent within the current step unless the
   step spec explicitly allows exploratory investigation

---

## Cross-artifact consistency rules

Research artifacts must be consistent with each other. When findings
from different steps contradict:

- This is a valuable discovery, not an error
- Record the contradiction explicitly in both artifacts
- Identify what would resolve the contradiction
- Do not silently resolve by choosing one finding over another
- If resolution is possible within the current step, resolve and
  document the reasoning
- If not, carry it as an open question

The authority order for research artifacts: verified findings take
precedence over reviewed findings, which take precedence over draft
findings. When two artifacts at the same confidence level conflict,
escalate to human review.

---

## What research standards do not govern

- Git workflow (WORKFLOW_STANDARDS.md)
- Operating model and issue classification (OPERATING_MODEL.md)
- Project scope and phase sequencing (PLAN.md and PROJECT_CHARTER.md)
- Design decisions (a separate design domain adapter when design begins)
- Implementation (a separate coding domain adapter when implementation begins)

---

## Deviation rules

These standards define the default for research-phase work.

If a step requires deviation:

- Make the deviation explicit in the step spec
- Keep it narrow in scope
- Record the reason in HISTORY.md if meaningful
- Do not silently drift from the standard
