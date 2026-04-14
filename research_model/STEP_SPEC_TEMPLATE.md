# Step [X.Y] — [Step Title]

## Purpose

[One sentence describing what this step exists to discover or assess.]

---

## Artifact to produce

[The specific document or documents this step produces. Include the
expected file path and a one-sentence description of what it contains.]

| Artifact | Path | Description |
|----------|------|-------------|
| | | |

---

## Questions to address

[The specific research questions this step must answer or explicitly
record as still-open. A step is not complete until each listed question
is either answered with evidence or carried forward as an open question
with an investigation approach noted.]

- [ ] [Question 1]
- [ ] [Question 2]
- [ ] [Question 3]

---

## Inputs

[The documents, artifacts, or information this step depends on.
Note the required confidence level — some investigation steps can
begin with Draft inputs, others need Reviewed.]

| Input | Source | Required confidence |
|-------|--------|---------------------|
| | | |

---

## Methodology

[How this step should be conducted. This is not a script — it is
guidance on the approach. Include:]

### Investigation approach

[Describe the method: direct inspection, tool testing, literature
review, expert consultation, comparative analysis, etc.]

### Tools and commands

[List specific tools, commands, or techniques that should be used.
Be explicit enough that the agent can execute without guessing.]

### Evidence to collect

[What raw evidence should be captured and stored under
`research/evidence/`. Be specific about what to save.]

---

## Constraints

[Any constraints specific to this step — scope limits, things to
avoid, rabbit holes to resist, things that must not be concluded
here because they belong to a later step.]

-
-

---

## Completeness criteria

This step is complete when:

- [ ] The specified artifact exists with a confidence marker
- [ ] All questions in "Questions to address" are either answered
  with cited evidence or explicitly carried as open questions
  with investigation approaches noted
- [ ] All claims have a stated evidence basis
- [ ] Gaps and limitations are identified
- [ ] Evidence files are stored and referenced
- [ ] Dependencies on other artifacts are identified in the artifact
- [ ] No out-of-scope investigation was performed
- [ ] PROGRESS.md is updated to Done with a one-line notes summary
- [ ] HISTORY.md is updated if any meaningful discovery was made

---

## Open questions at step creation

[Questions that were known before this step started. These may or
may not be resolved during this step — record them here so they
are visible from the start.]

| Question | Blocking? | Investigation approach |
|----------|-----------|----------------------|
| | | |

---

## Expected findings profile

[Optional but useful: what kind of findings does this step expect
to produce? This helps calibrate whether the step is on track.]

- Likely to confirm: [things expected to be straightforward]
- Likely to discover: [areas where new information is expected]
- Likely to raise questions about: [areas of expected uncertainty]

This section is guidance, not a constraint. Surprising findings
are valuable — do not suppress results that don't match expectations.

---

## Rabbit hole risks

[Known tangents that might appear during this step. Name them
explicitly so the agent can recognize and resist them.]

- [Tangent 1 — why it's tempting and why it should be deferred]
- [Tangent 2]

If an unlisted tangent appears, follow the investigation rabbit-hole
rule in RESEARCH_STANDARDS.md.

---

## Human review required?

[ ] No — AI self-review is sufficient for this step
[ ] Yes — human review required before promoting artifact confidence

If yes, reason:

---

## Notes

[Any additional context, background, or guidance useful for executing
this step. This is not scope — it is context.]
