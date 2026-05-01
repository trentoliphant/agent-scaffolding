# 0015 Standard Remains Narratively Versioned Until Release Pressure Is Real

## Context

The rewrite reached a point where the repository now has:

- a coherent current builder path
- a baseline implementation shape
- a curated example set
- explicit boundary rules for reference and incubating material
- a one-repo boundary decision

That made it reasonable to ask what release or versioning shape the open
standard should use.

At the same time, the repository still shows several signals that it is not
yet operating like a packaged API or a mature multi-release standard:

- there are no existing release tags
- the main outputs are documents, examples, templates, and decisions
- the repository still uses `Current` materials and active frontier documents
  as its primary coordination mechanism
- examples, references, and incubating sources remain co-located with the
  standard and baseline path

The repository therefore needs a boundary between useful stability signals and
premature release machinery.

## Decision

Keep the open standard narratively versioned for now.

Do not adopt formal release tags or a stronger semantic versioning model yet.

For the current stage, use these stability signals instead:

- `Current` material classification
- durable decision records in `history/decisions/`
- state documents naming the active frontier
- repository history when exact change tracing is required

Revisit explicit release tags only when real pressure appears, such as:

1. external builders need a citeable stable snapshot of the standard or
   baseline path
2. changelog-style communication of meaningful standard changes becomes
   necessary
3. the standard and baseline have become stable enough that a named pre-1.0
   snapshot would help more than it would mislead
4. migration guidance between distinct repository states becomes a repeated
   need
5. examples, templates, and guides need to be frozen against a named standard
   snapshot for adoption or evaluation

When those pressures become real, the most likely next step is not full
multi-track versioning.
It is lightweight explicit pre-1.0 repo-level release snapshots.

## Consequences

Positive consequences:

- the repository avoids versioning overhead before builders clearly need it
- the standard does not imply compatibility guarantees it is not yet ready to
  make
- contributors can keep improving the current path without maintaining a
  formal release process too early
- builders retain one clear current source of truth

Boundary consequences:

- builders who need a citeable stable snapshot do not yet get a named release
- the repository must continue to keep status labels, decision records, and
  active-state documents clear
- the first explicit release will need a deliberate cut later rather than
  emerging automatically

Tradeoff:

- stability is communicated narratively rather than through tags or version
  numbers

This tradeoff is acceptable because the repository's present needs are better
served by clarity of current materials than by premature release formalism.
