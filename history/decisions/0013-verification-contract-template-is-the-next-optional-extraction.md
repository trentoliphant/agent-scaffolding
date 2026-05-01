# 0013 Verification Contract Template Is The Next Optional Extraction

## Context

The repository completed a curated promoted example set covering minimal,
coding-focused, research-to-design, regulated-approval, and expertise-tiered
patterns.

That created a post-curation question: whether the examples now revealed one
reusable artifact gap that builders should not have to reconstruct from prose.

The strongest repeated gap was not another full domain example and not a
heavier task template.
It was a compact way to define one verification contract as a reusable local
artifact.

The repository already had:

- standard-level definition of verification contracts
- repeated example use of explicit verification contracts
- `step_review.template.md` as a record for applying verification after work

What it did not have was a focused baseline asset for defining one contract in
advance, including:

- the subject being judged
- the criteria
- the allowed verifier
- the verdicts
- the consequence of each verdict

Without that asset, builders had to reconstruct the contract shape from guide
text or example prose.

## Decision

Add an optional `verification_contract.template.md` to the baseline template
set.

Treat it as:

- a baseline implementation asset, not a standard-core requirement
- an optional template used when a project benefits from defining reusable
  verification contracts explicitly
- the first promoted reusable extraction from the completed example set

Do not treat this template as a reason to make every project define separate
verification-contract files.
It should remain optional and compact.

Do not widen the baseline further unless repeated builder need shows another
real cross-example gap.

## Consequences

Positive consequences:

- builders get a copyable contract shape without having to infer it from prose
- the distinction between defining a contract and applying a contract becomes
  more explicit
- domain implementations can express repeated verification logic cleanly
  without expanding the standard core

Boundary consequences:

- `step_review.template.md` remains the verification record after work is
  performed
- the standard core still defines only the minimum verification contract
  requirements
- domain-specific verification language still belongs in implementations and
  examples, not in the standard itself

Tradeoff:

- the baseline template set becomes slightly larger

This tradeoff is acceptable because the new template fills a repeated
cross-example builder need while staying optional and domain-neutral.
