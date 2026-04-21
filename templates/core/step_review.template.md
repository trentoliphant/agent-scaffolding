# VERIFICATION RECORD — Task Or Step X.Y

## 1. Objective alignment

- [ ] The outcome satisfies the stated Objective
- [ ] The result matches the intent of the task or step, not just a narrow
      literal reading

---

## 2. Scope adherence

- [ ] Only items in "In Scope" were performed
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
- [ ] Outputs or decisions are internally consistent where required
- [ ] No known incorrect or unsupported result remains within scope

---

## 5. Verification Evidence

- [ ] Required checks, tests, or reviews were completed
- [ ] The evidence reflects intended behavior, not outdated assumptions
- [ ] No verification relied on undefined or accidental behavior
- [ ] The verification verdict is explicit

---

## 6. Regression awareness

- [ ] Existing supported behavior still works as expected
- [ ] No unrelated behavior or process was broken
- [ ] Changes are localized to intended components or artifacts

---

## 7. Fix-forward validation

If earlier work was modified:

- [ ] Changes were necessary to satisfy the current task or step
- [ ] The original intent remains intact
- [ ] Changes were not disguised architectural or plan changes
- [ ] Meaningful corrections were recorded in `HISTORY.md`

---

## 8. Escalation check

- [ ] No unresolved plan-level issues remain
- [ ] No unresolved architectural issues remain
- [ ] Any required escalations were handled before completion

---

## 9. Output quality

- [ ] The output is understandable by future contributors and agents
- [ ] No unnecessary complexity was introduced
- [ ] Naming and terminology are consistent with the system model and
      applicable standards
- [ ] No obvious placeholders remain in accepted output

---

## 10. Documentation alignment

- [ ] The spec reflects what was actually performed, if adjusted
- [ ] `PROGRESS.md` is updated correctly
- [ ] Required trace information is recorded
- [ ] `HISTORY.md` is updated if meaningful insights occurred

---

## 11. Completion decision

- [ ] This task or step can be considered complete
- [ ] No known work remains within the defined scope

---

## Verdict And Notes

- Verification verdict
- Observations during verification
- Any concerns to revisit later
- Any follow-up actions outside current scope
