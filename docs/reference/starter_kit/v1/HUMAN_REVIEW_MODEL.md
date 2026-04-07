# HUMAN REVIEW MODEL

## Purpose

The human reviewer validates whether a step is safe to promote from
Machine Complete to Done.

The human does not re-implement or fully re-review the step. The human
confirms:

- intent is satisfied
- behavior is correct in practice
- the reviewer agent’s judgment is sound
- no incorrect assumptions are being promoted as truth

---

## Primary responsibilities

The human reviewer must evaluate:

- Whether the step actually achieves its intended purpose
- Whether the reviewer agent’s decision and reasoning are sound
- Whether tests validate meaningful behavior
- Whether any incorrect assumptions are being accepted
- Whether escalation should have occurred but did not

---

## Non-responsibilities

The human reviewer does not:

- Perform full code review line-by-line (unless necessary)
- Re-run the entire STEP_REVIEW checklist
- Optimize or expand the implementation
- Redesign architecture during review (unless escalation is required)

---

## Required review context

Before reviewing, read:

1. STEP_SPEC
2. Reviewer agent output
3. Relevant code changes (skim or targeted)
4. Tests (especially for intent validation)
5. Relevant HISTORY entries if referenced

---

## Human review procedure

### 1. Intent check

Ask:

- Does this actually solve the intended problem?
- Would a user or system behave correctly with this change?

---

### 2. Reviewer validation

Ask:

- Does the reviewer agent’s reasoning make sense?
- Did it miss anything obvious or important?
- Is the decision (PASS / REVISE / ESCALATE) justified?

---

### 3. Reality check

Ask:

- Do the tests reflect real behavior, or just internal consistency?
- Are there assumptions that could be wrong in practice?
- Is anything “technically correct but practically misleading”?

---

### 4. Boundary check

Ask:

- Did this step accidentally change architecture or system meaning?
- Should something here have been escalated?

---

### 5. Risk check

Ask:

- If this is wrong, how costly is it to fix later?
- Is the system now depending on something that isn’t fully validated?

---

## Decision outcomes

The human must return one of:

### APPROVE

- Step is correct and safe
- May be marked as Done
- Safe for downstream human-level dependencies

---

### REQUEST_CHANGES

- Step is close but needs adjustment
- Return to owner with specific guidance

---

### ESCALATE

- Issue requires:
  - PLAN.md update, or
  - SYSTEM_MODEL.md update

- Do not accept step as Done until resolved

---

## Decision criteria

### APPROVE only if:

- Intent is clearly satisfied
- Reviewer agent reasoning is sound
- Tests validate meaningful behavior
- No hidden architectural or plan issues exist
- No significant risk is being silently accepted

---

### REQUEST_CHANGES if:

- Minor correctness issues exist
- Tests are insufficient or misleading
- Reviewer agent missed something local
- Behavior is unclear or incomplete

---

### ESCALATE if:

- Architecture may be incorrect or incomplete
- Plan sequencing appears wrong
- A dependency should have been human-level
- The step changes system meaning
- The issue cannot be resolved locally

---

## Review priorities

When uncertain, prioritize:

1. Correct system behavior
2. Architectural integrity
3. Correct interpretation of intent
4. Test realism
5. Code quality

---

## Review output format

### Human Review Result
- Decision: APPROVE | REQUEST_CHANGES | ESCALATE

### Summary
- 2-4 sentence summary

### Key observations

- Observation 1
- Observation 2

### Required actions

- Action 1
- Action 2

### Escalations

- None
or
- PLAN.md requires update because ...
- SYSTEM_MODEL.md requires update because ...

### Confidence

- High / Medium / Low

### Notes (optional)
- Any additional thoughts
