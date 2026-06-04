# Material Status Review

This note records a focused review of whether the repository's current
`Current`, `Transitional`, `Reference/Migration`, `Legacy`, and `Incubating`
classifications still match the actual shape of the repository.

It is a working review note, not a durable decision by itself.

## Review Goal

Decide whether any major reclassification is needed before the repository
continues deeper repository-boundary or contribution-model work.

## Materials Reviewed

- `docs/guide/repository-status.md`
- `README.md`
- `docs/reference/README.md`
- `docs/guide/starter-kit-adoption.md`
- `CONTRIBUTING.md`
- repository top-level directories
- `history/decisions/0006-0013`
- the current promoted example set
- the root `design_model/` and `research_model/` directories

## Summary Judgment

The current status model still broadly holds.

No major reclassification is needed right now.

The main issue is precision, not direction:

- some documents describe a directory as current when only a named subset is
  current
- the status guide has not fully caught up to newer review notes and
  decisions
- the repository still needs a clearer statement that co-location does not
  imply equal builder-path status

## Specific Judgments

### Current

These still belong in the current surface:

- `docs/scaffolding/`
- the current builder-guide path in `docs/guide/`
- the promoted example directories:
  - `docs/examples/minimal/`
  - `docs/examples/software-project/`
  - `docs/examples/research-to-design/`
  - `docs/examples/regulated-approval/`
  - `docs/examples/expertise-tiered-review/`
- the baseline template layer in `templates/`, except explicitly deferred
  coding-focused items
- repository entry and governance documents such as `README.md`, `AGENTS.md`,
  and `CONTRIBUTING.md`
- active state and planning documents plus the working review notes directly
  referenced by `state/current.md`
- rewrite-era decisions in `history/decisions/0006-0013`

### Transitional

The transitional classification remains narrow.

The clearest current transitional item is still:

- `templates/core/coding_standards.template.md`

It remains useful, but it is intentionally deferred from the smallest
domain-neutral baseline.

### Reference/Migration

These still fit the reference or migration role:

- `docs/reference/`
- `docs/reference/starter_kit/`
- `docs/examples/structured-project-starter/`
- `docs/guide/starter-kit-adoption.md`

They are relevant and useful, but they are not the default builder path.

### Legacy

These still read correctly as legacy:

- `history/decisions/0003-0005`
- `state/starter-kit-integration-plan.md`
- `docs/reference/starter_kit/v1/`

They preserve earlier repository rationale and material without defining the
current direction.

### Incubating

These still fit the incubating classification:

- `design_model/`
- `research_model/`

They remain extraction sources, not promoted examples or baseline assets.

## Recommendation

Do not perform a large reclassification pass.

Instead:

1. tighten the wording in `docs/guide/repository-status.md`
2. keep the distinction between promoted examples and reference examples
   explicit
3. keep the distinction between active state documents and supporting review
   notes visible
4. leave the one-repo versus multi-repo question open for a later boundary
   decision

## Recommended Next Focus

The next stronger question is no longer whether the current status labels are
wrong.

It is:

1. whether the standard, baseline implementation, examples, references, and
   incubating sources should remain co-located in one repository for now
2. what contributor guidance is still needed so standard changes and domain
   implementation contributions do not blur together
