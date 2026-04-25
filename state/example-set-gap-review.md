# Example Set Gap Review

This note records a side-by-side review of the current promoted example set to
identify whether the examples imply one missing reusable artifact in
`docs/guide/` or `templates/`.

It is a working review note, not a durable decision by itself.

## Examples Reviewed

- `docs/examples/minimal/README.md`
- `docs/examples/software-project/README.md`
- `docs/examples/research-to-design/README.md`
- `docs/examples/regulated-approval/README.md`
- `docs/examples/expertise-tiered-review/README.md`

## Review Goal

Find one repeated optional artifact shape that:

- appears across multiple examples
- is not already given a focused reusable form
- would help builders copy a pattern without reconstructing it from prose

## Summary Judgment

The strongest candidate gap is a reusable verification-contract definition
artifact.

This is not the same thing as the current `step_review` template.

The current repository already has:

- standard-level explanation of what a verification contract is
- example after example using multiple explicit verification contracts
- a verification record template for judging a completed task or step

What it does not yet have is a focused reusable way to define one verification
contract as a local artifact.

## Why This Gap Stands Out

Verification contracts appear repeatedly across the example set:

- `minimal`: correctness and boundary compliance
- `software-project`: correctness, architecture alignment, documentation
  completeness, regression awareness, release readiness
- `research-to-design`: evidence sufficiency, synthesis coherence, workflow
  clarity, decision traceability
- `regulated-approval`: content correctness, evidence sufficiency, compliance
  alignment, approval authorization
- `expertise-tiered-review`: content correctness, scope fit, escalation
  compliance, trace sufficiency

That repetition suggests a reusable pattern, not just example-specific prose.

## Why Existing Templates Do Not Fully Cover It

`templates/core/step_review.template.md` captures a verification record after
work has been performed.

It does not define a reusable contract artifact that answers questions such as:

- what is being judged
- what criteria apply
- what verdicts are possible
- who may apply the judgment
- what next action follows each verdict

Builders can infer those fields from the guides and examples, but they still
have to reconstruct the artifact shape themselves.

## Why Other Candidates Look Weaker

### Approval matrix

This appears strongly in only one promoted example.
It looks better treated as a domain-specific extension artifact unless reuse
pressure appears in more examples.

### Expertise profile or authority matrix

This is a strong pattern, but it currently appears as a clearly domain-specific
implementation shape rather than a cross-example gap.

### Investigative-step appendix

This was already evaluated separately and judged not yet justified.

### Research or design artifact templates

These are still too domain-shaped and better handled through examples and
guide text for now.

## Recommendation

The next extraction worth considering is:

- an optional verification-contract template or focused guide artifact that
  helps builders define one reusable contract cleanly

The most likely good fit is a template-level extraction, because builders may
want to copy and adapt a contract definition directly.

## Suggested Scope If Extracted

Keep it optional and compact.

A useful verification-contract template would likely cover:

- contract name
- subject being judged
- criteria
- verifier role or verifier function
- possible verdicts
- consequence or next action for each verdict
- evidence expected
- escalation rule if the contract cannot be resolved normally

It should stay domain-neutral and map cleanly to the existing standard
language.

## Recommended Immediate Action

If the repository chooses one next extraction, the best candidate is an
optional verification-contract template.

If the repository is not ready to add another template yet, the fallback is to
add a very short focused guide note first and wait for more adoption pressure.
