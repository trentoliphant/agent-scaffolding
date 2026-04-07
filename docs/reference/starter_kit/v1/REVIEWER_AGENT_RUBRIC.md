# Reviewer Agent Rubric

A step may PASS only if:

- Objective satisfied
- In-scope work only
- Out-of-scope work not implemented
- Acceptance criteria satisfied
- Architectural constraints preserved
- Tests are adequate and passing
- No hidden regressions
- No escalation required

A step must REVISE if:

- Local implementation is incomplete or incorrect
- Tests are weak, stale, or misaligned
- Minor scope drift occurred
- Edge cases are missing
- Local fixes are needed without changing plan or architecture

A step must ESCALATE if:

- Architecture may need to change
- Plan sequencing may be wrong
- Dependency level is wrong
- A workaround bypasses an abstraction
- Tests hide conceptual failure
- The issue cannot be judged locally
