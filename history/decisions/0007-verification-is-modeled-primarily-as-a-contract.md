# 0007 Verification Is Modeled Primarily As A Contract

## Context

The rewrite has already established verification as a first-class part of the
open standard.

However, one modeling ambiguity remained open:

- should verification be treated mainly as a role
- should it be treated mainly as a reusable contract
- should older `review type` language remain a peer concept in the standard

Without a clear answer, different documents could drift toward different
interpretations and make the standard harder to inspect or extend.

## Decision

In the open standard, verification is modeled primarily as a reusable
contract.

That contract defines:

- the subject being judged
- the criteria being applied
- the possible verdicts
- the consequence of each verdict

The standard keeps that contract distinct from:

- verifier roles, which define who may apply the judgment
- orchestration, which defines when verification happens and what changes next

Older `review type` language is treated as legacy or local implementation
language.

When a `review type` defines explicit criteria and verdict flow, it maps to a
verification contract.
When it only names a workflow step, it belongs in orchestration or local
implementation guidance.

## Consequences

Positive consequences:

- the standard has a clearer reusable unit for verification across domains
- the same verification logic can be carried by different human or machine
  roles without redefining the standard
- older materials can still be interpreted without preserving ambiguity in the
  core model

Boundary consequences:

- roles remain responsible for authority and assignment, not for silently
  carrying the full verification logic
- orchestration remains responsible for timing and routing, not for defining
  the verification criteria themselves
- implementations may still use local review language, but the underlying model
  should remain recoverable

Tradeoff:

- some older material will need translation from broader `review` language into
  the more explicit contract-role-orchestration split

This tradeoff is acceptable because it improves inspectability, portability,
and consistency across the standard.
