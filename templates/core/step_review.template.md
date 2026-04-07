# STEP REVIEW — Step X.Y

## 1. Objective alignment

- [ ] The implementation satisfies the stated Objective
- [ ] The behavior matches the intent of the step, not just the literal code changes

---

## 2. Scope adherence

- [ ] Only items in "In Scope" were implemented
- [ ] Nothing from "Out of Scope" was implemented
- [ ] No future-phase functionality was introduced

---

## 3. Architectural integrity

- [ ] No architectural constraints were violated
- [ ] Component boundaries are respected
- [ ] No hidden coupling was introduced
- [ ] No shortcuts bypass core abstractions

---

## 4. Correctness

- [ ] All acceptance criteria are satisfied
- [ ] Relevant edge cases are handled
- [ ] Behavior is deterministic where required
- [ ] No known incorrect behavior remains within scope

---

## 5. Testing

- [ ] Required tests are implemented
- [ ] Tests reflect intended behavior, not outdated assumptions
- [ ] Tests pass consistently
- [ ] No test relies on undefined or accidental behavior

---

## 6. Regression awareness

- [ ] Existing functionality still works as expected
- [ ] No unrelated behavior was broken
- [ ] Changes are localized to intended components

---

## 7. Fix-forward validation

If earlier work was modified:

- [ ] Changes were necessary to satisfy the current step
- [ ] The original step intent remains intact
- [ ] Changes were not disguised architectural or plan changes
- [ ] Meaningful corrections were recorded in `HISTORY.md`

---

## 8. Escalation check

- [ ] No unresolved plan-level issues remain
- [ ] No unresolved architectural issues remain
- [ ] Any required escalations were handled before completion

---

## 9. Code quality

- [ ] Code is understandable by future contributors and agents
- [ ] No unnecessary complexity was introduced
- [ ] Naming is consistent with the system model and coding standards
- [ ] No obvious dead code or placeholders remain

---

## 10. Documentation alignment

- [ ] `step_X.Y_spec.md` reflects what was actually implemented, if adjusted
- [ ] `PROGRESS.md` is updated correctly
- [ ] `HISTORY.md` is updated if meaningful insights occurred

---

## 11. Completion decision

- [ ] This step can be considered complete
- [ ] No known work remains within the defined scope

---

## Notes

- Observations during review
- Any concerns to revisit later
- Any follow-up actions outside current scope
