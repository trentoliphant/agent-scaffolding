# MODEL EVALUATION

## Purpose

This document defines a structured evaluation of models, agent roles, or
configurations within the AI development operating system.

The goal is to compare performance under identical conditions and identify
which configurations produce the most reliable, correct, and efficient outcomes.

---

## Experiment overview

### Experiment name
[Short descriptive name]

### Date
YYYY-MM-DD

### Objective
What are we trying to learn?

Examples:
- Compare coding performance of Model A vs Model B
- Compare reviewer effectiveness across models
- Evaluate prompt variations for step execution

---

## Fixed inputs

These must remain identical across all runs.

- SYSTEM_MODEL version:
- PLAN version:
- STEP_SPEC:
- Repository state (commit hash or snapshot):
- OPERATING_MODEL version:
- CODING_STANDARDS version:
- WORKFLOW_STANDARDS version:
- Templates used:

---

## Variables

What is being changed?

Examples:
- Coding model (Model A vs Model B)
- Reviewer model
- Prompt variation
- Context packaging
- Number of reviewer agents
- Role assignment strategy

---

## Evaluation dimensions

### 1. Contract compliance
- Did the implementation satisfy `step_X.Y_spec.md`?
- Were acceptance criteria met?
- Was scope respected?

### 2. Architectural integrity
- Were `SYSTEM_MODEL.md` constraints respected?
- Any hidden coupling or abstraction violations?
- Any silent architectural drift?

### 3. Standards compliance
- Were relevant coding standards followed?
- Were workflow expectations followed where applicable?
- Did the output align with project conventions?

### 4. Test quality
- Do tests validate real behavior?
- Do tests avoid false assumptions?
- Are edge cases covered?

### 5. Review outcomes
- Reviewer agent decision: PASS | REVISE | ESCALATE
- Human decision: APPROVE | REQUEST_CHANGES | ESCALATE

### 6. Iteration cost
- Number of revisions required
- Number of review cycles
- Amount of correction needed

### 7. Process compliance
- Followed operating model rules?
- Correct issue classification?
- Correct dependency handling?
- Proper escalation behavior?

### 8. Output quality
- Clarity and maintainability
- Simplicity vs over-engineering
- Consistency with system patterns

---

## Results

### Run 1 — [Model / Configuration]

- Coding model:
- Reviewer model:
- Human review outcome:
- Reviewer result:
- Iterations required:
- Summary:
- Key strengths:
- Key weaknesses:

---

### Run 2 — [Model / Configuration]

- Coding model:
- Reviewer model:
- Human review outcome:
- Reviewer result:
- Iterations required:
- Summary:
- Key strengths:
- Key weaknesses:

---

### Additional runs

Repeat as needed.

---

## Comparative analysis

### Strength comparison

| Dimension | Configuration A | Configuration B | Notes |
|----------|------------------|-----------------|-------|
| Contract compliance | | | |
| Architecture | | | |
| Standards compliance | | | |
| Tests | | | |
| Review burden | | | |
| Process compliance | | | |
| Output quality | | | |

---

## Observations

- Observation 1
- Observation 2
- Observation 3

Focus on meaningful differences, not just superficial variation.

---

## Decision

Which configuration is preferred and why?

- Preferred:
- Reason:

---

## Confidence

- High
- Medium
- Low

---

## Notes

- Additional insights
- Unexpected behaviors
- Ideas for further experiments
