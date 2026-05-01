# Reference Retention Review

This note records a focused review of which current reference and migration
materials still provide enough builder or contributor value to remain in this
repository long term.

It is a working review note, not a durable decision by itself.

## Review Goal

Decide whether the current reference and migration set should:

- remain in this repository largely as-is
- be reduced to a smaller subset
- be moved out of the repository sooner

## Materials Reviewed

- `docs/reference/README.md`
- `docs/reference/starter_kit/`
- `docs/reference/starter_kit/v1/`
- `docs/guide/starter-kit-adoption.md`
- `docs/examples/structured-project-starter/README.md`
- current references from `README.md`, `CONTRIBUTING.md`, and
  `docs/guide/start-here.md`

## Current Signals

The current reference and migration layer is still narrow:

- one local reference source: `docs/reference/starter_kit/`
- one migration guide: `docs/guide/starter-kit-adoption.md`
- one reduced teaching-oriented derived example:
  `docs/examples/structured-project-starter/`
- one legacy historical subtree nested inside the reference source:
  `docs/reference/starter_kit/v1/`

The entire `docs/reference/` footprint is also small.

The local `starter_kit` copy remains important because the external source
path named in older notes is not a dependable repository-local dependency.

## Options Reviewed

### Option 1. Keep the current reference and migration set in-repo for now

Strengths:

- preserves the actual source material that informed the current baseline and
  template extractions
- keeps migration help available for older document-structured workflows
- keeps the reduced example and the full reference source visible together
- avoids turning current docs into implicit replacements for source-preserving
  reference material

Risks:

- retains some older material that is no longer central to the current builder
  path

### Option 2. Reduce the retained set now

Possible reduction:

- keep only the migration guide and reduced example
- remove or externalize the full local `starter_kit` reference copy

Strengths:

- further reduces repository noise

Risks:

- removes the main in-repo extraction source
- weakens contributor ability to trace where imported templates and older
  patterns came from
- makes the repository depend more on external context that may not be
  available

### Option 3. Externalize most reference material now

Strengths:

- makes the current builder path visually cleaner

Risks:

- breaks the current one-repo teaching and extraction story
- makes migration guidance less inspectable
- adds coordination overhead without strong pressure

## Evaluation

Option 1 is the strongest current fit.

The reference layer is small, intentionally classified, and still actively
used in the repository's explanations of:

- migration from older starter-kit-derived workflows
- where some baseline templates came from
- how fuller document-structured implementations differ from the minimal
  standard path

The weakest part of the retained set is `docs/reference/starter_kit/v1/`, but
it is already isolated as `Legacy`, small, and not causing meaningful builder
path confusion by itself.

That makes immediate pruning less valuable than keeping the reference story
intact.

## Recommendation

Keep the current reference and migration set in this repository for now.

That means retaining:

- `docs/reference/README.md`
- the local `docs/reference/starter_kit/` copy
- `docs/guide/starter-kit-adoption.md`
- `docs/examples/structured-project-starter/README.md`
- the nested `docs/reference/starter_kit/v1/` subtree as a legacy part of the
  retained reference source

Do not add more reference or migration material casually.

Add or retain reference material only when it satisfies at least one of these:

1. it is a real extraction source for current or likely standard work
2. it materially helps builders migrate older workflows
3. it preserves context that current templates, guides, or examples would be
   harder to understand without

## Revisit Triggers

Revisit this conclusion if one or more of these becomes true:

1. the reference layer grows beyond a small, inspectable supporting set
2. the retained source material stops informing actual extraction or migration
   work
3. builder navigation confusion starts coming from reference-layer presence
   rather than from wording or status labeling
4. maintaining local copies becomes meaningfully more expensive than their
   teaching or extraction value

## Recommended Immediate Action

Promote this recommendation into a decision record:

- keep the current reference and migration set in-repo for now
- treat the local `starter_kit` copy as the authoritative in-repo reference
  source
- keep `v1` only as a nested legacy part of that retained source, not as a
  separately promoted artifact
