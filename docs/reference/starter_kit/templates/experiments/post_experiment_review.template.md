# POST-EXPERIMENT REVIEW

## Purpose

This document captures insights from experimental runs and translates them
into improvements for the operating model, templates, standards, and
development process.

The goal is not to evaluate code itself, but to improve how the system
produces code and decisions.

---

## Experiment scope

### Experiment name
[Reference to MODEL_EVALUATION]

### Steps included
- Step X.Y
- Step X.Z

### Date
YYYY-MM-DD

### Reviewer
[Human / Team / Agent-supported review]

---

## 1. What worked well

Patterns that should be reinforced:

- Pattern 1
- Pattern 2
- Pattern 3

---

## 2. Failure patterns

Where agents consistently failed or struggled:

- Failure 1
- Failure 2
- Failure 3

---

## 3. Reviewer gaps

What reviewer agents missed:

- Missed issue 1
- Missed issue 2

---

## 4. Misclassifications

Where issues were classified incorrectly:

- Should have been escalation but was not
- Should have been fix-forward but escalated
- Dependency level misclassified
- Standards issue treated as architecture issue
- Architecture issue treated as local bug

---

## 5. Template weaknesses

Where `STEP_SPEC` or other templates were insufficient:

- Missing constraints
- Ambiguous instructions
- Repeated clarification needed
- Missing standard references

---

## 6. Standards gaps

Where coding or workflow standards were insufficient:

### Coding standards gaps
- Gap 1
- Gap 2

### Workflow standards gaps
- Gap 1
- Gap 2

---

## 7. Operating model gaps

Where the operating model failed to guide behavior:

- Missing rule
- Unclear boundary
- Weak enforcement
- Missing escalation trigger

---

## 8. System model pressure

Where `SYSTEM_MODEL.md` showed tension:

- Abstraction unclear
- Responsibility overlap
- Invariant violated or unclear
- Project boundary not well defined

---

## 9. Model-specific behavior

Differences observed between models or configurations:

- Model A tendency:
- Model B tendency:
- Reviewer pairing effect:
- Prompting/context effect:

---

## 10. Promotion decisions

This is the most important section.

### Promote to `OPERATING_MODEL*.md`
- [ ] Improvement 1
- [ ] Improvement 2

### Promote to `SYSTEM_MODEL.md`
- [ ] Improvement 1
- [ ] Improvement 2

### Promote to `PLAN.md`
- [ ] Improvement 1
- [ ] Improvement 2

### Promote to `CODING_STANDARDS.md`
- [ ] Improvement 1
- [ ] Improvement 2

### Promote to `WORKFLOW_STANDARDS.md`
- [ ] Improvement 1
- [ ] Improvement 2

### Promote to templates
- [ ] Improvement 1
- [ ] Improvement 2

### Reviewer agent improvements
- [ ] New rule or check
- [ ] Prompt refinement
- [ ] Additional rubric criteria

### Human review improvements
- [ ] Clarify trust boundary
- [ ] Clarify approval criteria
- [ ] Improve review prompt or rubric

---

## 11. Process adjustments

What should change in future execution:

- Adjustment 1
- Adjustment 2
- Adjustment 3

---

## 12. Anti-pattern detection

Did any of the following occur?

- [ ] Scope creep
- [ ] Silent architectural change
- [ ] Over-reliance on tests
- [ ] Incorrect dependency usage
- [ ] Reviewer false positives
- [ ] Reviewer false negatives
- [ ] Standards drift
- [ ] Human review bottleneck
- [ ] Excessive process overhead

Describe if yes:

- Description 1
- Description 2

---

## 13. Key insights

The most important takeaways:

- Insight 1
- Insight 2
- Insight 3

---

## 14. Next experiments

Ideas for future runs:

- Experiment 1
- Experiment 2
- Experiment 3

---

## Notes

Optional reflections, risks, or follow-up ideas.
