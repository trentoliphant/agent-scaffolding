# Post-Verification Example Set Review

This note records a second-pass review of the promoted example set after the
optional `verification_contract` template was added.

It is a working review note, not a durable decision by itself.

## Review Goal

Decide whether the repository now needs any further reusable extension
artifact beyond the optional `verification_contract` template.

## Materials Reviewed

- `docs/examples/minimal/README.md`
- `docs/examples/software-project/README.md`
- `docs/examples/research-to-design/README.md`
- `docs/examples/regulated-approval/README.md`
- `docs/examples/expertise-tiered-review/README.md`
- `docs/guide/domain-implementation-extensions.md`
- `docs/guide/customizing.md`
- `templates/README.md`
- `templates/core/verification_contract.template.md`
- `state/research-model-extraction-review.md`
- `state/investigative-step-template-evaluation.md`

## Summary Judgment

No further reusable extension artifact is clearly justified right now.

The current repository now has:

- a compact reusable artifact for defining one verification contract
- guide-layer treatment of domain extensions, expertise profiles, and
  research-heavy work
- a curated example set that covers the strongest current builder-facing
  extension patterns

That combination appears sufficient for the current builder path.

## Why Another Extraction Is Not Yet Justified

The strongest repeated cross-example gap has already been addressed by the
optional `verification_contract` template.

The remaining patterns look weaker as reusable baseline artifacts:

### Approval matrix

This appears strongly in the regulated-approval example, but not across the
full promoted set.

It still looks like a domain-specific overlay artifact rather than a
cross-domain baseline need.

### Expertise profile or work-type matrix

This is a strong implementation pattern, but it remains tightly tied to
projects that vary authority by profile, risk, or scope.

The current combination of guide text plus the expertise-tiered example is
enough for now.

### Research or investigative step variant

This has already been evaluated separately and is still not justified as a
template addition.

The guide layer now carries the portable ideas that matter most:

- evidence discipline
- open-question tracking
- expected plan mutation in exploratory work

### Domain trace-field appendices

Several examples add domain trace fields, but the field sets differ too much
to justify a shared baseline artifact.

At this stage, the examples are a better teaching surface than a single
template would be.

### Additional decision records

The example set does not currently expose one missing structural decision that
needs to be recorded before the repository can move forward.

## Recommendation

Do not add another template, focused guide artifact, or promoted extension
pattern yet.

Prefer to:

1. keep the current example set and template layer stable
2. mine incubating sources only when a real uncovered builder need appears
3. wait for repeated builder pressure before widening the reusable artifact
   set again

## What Would Change This Judgment

Revisit this conclusion if one of these happens:

1. multiple promoted examples begin using the same approval or authority
   artifact shape
2. builders repeatedly ask for help expressing investigative work inside the
   current template set
3. a real adoption project exposes a repeated gap that cannot be covered
   cleanly by the current guides and examples
4. repository-boundary work reveals a missing contribution or extension
   decision that deserves durable recording

## Recommended Next Focus

The next stronger frontier is no longer template extraction.

It is:

1. clarifying which remaining materials should stay current, transitional,
   reference, or incubating
2. deciding whether the standard, baseline implementation, and domain
   implementations should remain co-located in one repository
3. sharpening contributor guidance for standard changes versus domain
   implementation contributions
