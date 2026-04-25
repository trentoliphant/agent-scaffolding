# 0011 Design And Research Models Remain Extraction Sources

## Context

The repository contains `design_model/` and `research_model/` directories from
an earlier phase of work.

They contain useful domain-specific patterns, terminology, templates, and
quality standards.
However, they were created before the current open-standard framing and before
the repository adopted a small curated example set.

The repository now has a promoted example set that covers:

- a minimal baseline shape
- a coding-focused scaling pattern
- a research-to-design handoff
- a regulated approval overlay
- an expertise-tiered review pattern

That makes it important to decide how `design_model/` and `research_model/`
should relate to the current builder path.

## Decision

Treat `design_model/` and `research_model/` as incubating extraction sources,
not as near-term promoted examples or top-level builder-path materials.

Their purpose is to provide candidate ideas for selective extraction into:

- guides
- templates
- decision records
- future example refinements

Promote material from those directories only when it fills a builder need that
the current curated example set does not already address.

Do not promote the directories wholesale as current domain implementations or
as a parallel example track.

When evaluating those directories, prefer extracting reusable pieces such as:

- template structure
- verification language
- trace expectations
- evidence discipline
- plan mutation rules
- domain-specific quality standards that reveal a cross-domain gap

If a piece remains too domain-specific or too structurally heavy to transfer
cleanly, leave it in the incubating layer.

## Consequences

Positive consequences:

- the builder path stays smaller and more coherent
- contributors have a clearer rule for how to use older domain-adapter
  material
- useful ideas can still be promoted without treating the old adapters as
  current source of truth
- the distinction between curated examples and fuller domain implementations
  stays visible

Tradeoffs:

- some potentially useful domain material will remain indirect for longer
- contributors must do extraction work instead of simply reclassifying the old
  directories as current

Those tradeoffs are acceptable because the repository should promote only the
smallest reusable artifacts that improve the current standard and builder path.
