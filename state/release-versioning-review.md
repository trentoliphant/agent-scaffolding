# Release And Versioning Review

This note records a focused review of what release or versioning shape the
open standard currently needs.

It is a working review note, not a durable decision by itself.

## Review Goal

Decide whether the repository should:

- remain narratively versioned for now
- adopt lightweight explicit release tags soon
- adopt a more formal semantic or multi-track versioning model now

## Current Signals

The repository currently shows:

- no existing git tags
- no package-style artifacts or APIs that require compatibility promises
- one active rewrite branch with in-progress standard, guide, template, and
  example alignment
- a builder path that depends primarily on `Current` materials rather than on
  named releases
- curated examples, reference material, and incubating extraction sources
  co-located with the standard

The repository also already has non-versioning tools for clarity:

- a status guide
- durable decision records
- state documents naming the active frontier
- explicit boundary rules between standard, baseline, examples, references,
  and incubating material

## Options Reviewed

### Option 1. Narrative versioning for now

Description:

- no formal release tags yet
- treat the current standard surface and decision history as the source of
  truth
- revisit explicit release tags only when real builder or governance pressure
  appears

Strengths:

- lowest governance overhead
- avoids pretending the standard is more stable than it is
- fits a repository whose main outputs are documents, examples, and templates
- keeps builders focused on the current path rather than on choosing among
  formal releases too early

Risks:

- builders cannot point to a named stable snapshot yet
- later migration into explicit releases will require a deliberate first cut

### Option 2. Lightweight pre-1.0 release tags soon

Description:

- adopt explicit repo-level tags such as `v0.1`, `v0.2`
- treat each tag as a named snapshot of the current standard surface

Strengths:

- gives builders a citeable snapshot
- could help future change logs and migration notes

Risks:

- adds ceremony before the repository has shown strong need for it
- may imply stability guarantees that the current rewrite does not yet intend
- forces decisions about what exactly is included in a release before the
  boundaries need that precision

### Option 3. Formal semantic or multi-track versioning now

Description:

- version the standard, baseline, templates, or examples as separate tracks
- use stronger compatibility language up front

Strengths:

- could support more complex downstream adoption later

Risks:

- over-formal for the current repository stage
- introduces compatibility and scope questions that the repo does not yet need
- increases the chance that versioning machinery becomes more prominent than
  builder usability

## Evaluation

Option 3 is clearly too heavy for the current stage.

Option 2 is plausible later, but it still looks early.

The repository does not yet show strong evidence that builders need explicit
release tags more urgently than they need a single clear current path.
The current rewrite is also still settling the relationship between standard,
baseline, examples, references, and incubating materials.

That makes premature explicit versioning more likely to create false precision
than to solve an urgent adoption problem.

## Recommendation

Choose Option 1 for now.

Keep the standard narratively versioned through:

- the `Current` material classification
- durable decision records
- state documents naming the active frontier
- repository history when exact change tracing is needed

Do not adopt formal release tags yet.

Instead, define the triggers that would justify the first explicit release.

## Suggested Release Triggers

Revisit this conclusion if one or more of these becomes true:

1. external builders need a citeable stable snapshot of the standard or
   baseline path
2. the repository needs changelog-style communication of meaningful standard
   changes
3. the standard and baseline have become stable enough that a named pre-1.0
   snapshot would help more than it would mislead
4. migration guidance between distinct repository states becomes a repeated
   need
5. examples, templates, and guides need to be frozen against a named standard
   snapshot for adoption or evaluation

## Recommended Immediate Action

Promote this recommendation into a decision record:

- keep the standard narratively versioned for now
- avoid formal release tags until release pressure becomes real
- name the triggers that should cause the repository to adopt explicit
  pre-1.0 release snapshots later
