# Human Review Rubric

APPROVE if:

- The step clearly satisfies its intended purpose
- Reviewer agent reasoning is sound
- Tests reflect real, meaningful behavior
- No hidden architectural or plan issues exist
- The system can safely build on this step

REQUEST_CHANGES if:

- Minor correctness issues exist
- Tests are weak or misleading
- Reviewer agent missed local issues
- Behavior is incomplete or unclear

ESCALATE if:

- Architecture may be wrong or incomplete
- Plan sequencing is questionable
- A dependency should have required human-level stability
- The step changes system meaning
- The issue cannot be resolved locally
