# Repository Boundary Review

This note records a focused review of whether the standard, baseline
implementation, examples, references, and incubating extraction sources should
remain co-located in this repository for the current phase of work.

It is a working review note, not a durable decision by itself.

## Review Goal

Choose the most useful repository boundary for the next phase of the rewrite.

The question is not whether a split might ever happen.

The question is whether the current repository should, for now, keep together:

- the open standard
- the baseline implementation assets
- the curated teaching-oriented examples
- selected reference and migration material
- incubating extraction sources

## Criteria

The options were judged against:

- builder usability
- clarity of source of truth
- contributor safety
- maintenance overhead
- ability to host references and incubating material without confusion
- compatibility with open, proprietary, and third-party implementations

## Options Reviewed

### Option 1. Keep one repository and strengthen boundaries inside it

Description:

- keep the current co-location model
- use status labels, contributor guidance, and a curated example policy to
  prevent drift
- treat external or proprietary domain implementations as valid without making
  this repository their required home

Strengths:

- keeps the builder path in one place
- preserves the relationship between standard, baseline, examples,
  references, and extraction sources
- avoids coordination and versioning overhead across multiple repositories
- makes it easier for contributors to compare source material against the
  current standard directly

Risks:

- contributors may still blur current, reference, and incubating material
- the repository can become noisy if boundaries are not maintained actively

### Option 2. Keep one repository for now, but define explicit split triggers

Description:

- same near-term structure as Option 1
- explicitly name what evidence would justify a later split

Strengths:

- keeps the builder path simple now
- avoids pretending the current shape is permanent
- gives contributors a clearer threshold for revisiting the boundary later

Risks:

- still requires disciplined curation in the current repository

### Option 3. Split now into separate repositories

Description:

- move the standard and baseline path into one repository
- move examples, references, or incubating materials into separate
  repositories or packages

Strengths:

- could reduce accidental source-of-truth confusion
- could give different materials separate release cadence

Risks:

- makes the builder path harder to scan
- adds coordination overhead immediately
- weakens the visibility of how examples and references relate back to the
  current standard
- creates extra governance work before the repository has real pressure that
  requires it

## Evaluation

Option 3 is not justified yet.

The repository already has a workable way to keep boundaries visible:

- a layered document structure
- a status guide
- a curated example rule
- explicit reference and incubating classifications
- a decision that domain implementations do not need to live here to count as
  valid uses of the standard

That means the main risks of co-location are governance risks, not structural
impossibilities.

Those governance risks are better handled right now through:

- clearer contributor guidance
- durable boundary decisions
- a small promoted example surface

than through an immediate repository split.

## Recommendation

Choose Option 2.

Keep the current co-location model for now, and record explicit split triggers
for later review.

This preserves the clearest builder path while leaving room to split if real
usage pressure appears.

## Suggested Split Triggers

Revisit the boundary if one or more of these becomes true:

1. the promoted example layer wants to grow beyond a small curated teaching
   set
2. reference or incubating materials begin to dominate contributor work or
   navigation
3. standard changes and domain-implementation changes repeatedly interfere
   with each other in review
4. the standard and baseline need a release cadence that diverges from
   examples or reference material
5. maintaining source-of-truth clarity requires heavier status machinery than
   a single repository can comfortably support

## Recommended Immediate Action

Promote this recommendation into a decision record:

- keep the standard, baseline, curated examples, selected references, and
  incubating extraction sources co-located for now
- state that this repository is not the required home for all domain
  implementations
- name the triggers that would justify reopening the split question
