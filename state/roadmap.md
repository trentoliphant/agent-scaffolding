# Roadmap

This document lists likely next improvements for the repository.

It is a planning aid, not a durable definition of the scaffold. Items here may change as the repository evolves.

## Near Term

1. Reframe the repository around the open-standard direction and align entry
   point documents to that purpose
2. Define the core modules of the standard and which are optional extensions
3. Add explicit standard treatment for traces, verification contracts, and the
   self-evolution loop
4. Clarify how roles, expertise levels, and decision rights work across mixed
   human and machine systems
5. Decide how to distinguish the open standard, the baseline implementation,
   and domain-specific implementations
6. Review current starter-kit-derived materials and classify them as canonical,
   transitional, or reference-only

## Medium Term

1. Publish a baseline implementation path that demonstrates the standard
   without tying it to one domain or runtime
2. Add integration guidance for common execution systems while preserving model
   and engine agnosticism
3. Define how domain implementations should extend the standard and contribute
   improvements back safely
4. Decide whether the standard and domain implementations should live in one
   repository or multiple repositories
5. Create a contribution model that welcomes domain experts without weakening
   the standard's coherence

## Watch Items

These are not immediate commitments, but they should remain visible:

1. Avoid over-formalizing the standard before real usage pressures justify it
2. Avoid turning one company's proprietary domain patterns into the open
   standard by default
3. Keep contributor-facing refinement from overwhelming builder-facing usability
4. Keep the trace and evolution requirements lightweight enough to be adoptable
5. Preserve the distinction between inspectable governance and specific model
   behavior claims

## Completion Rule

When a roadmap item becomes the active frontier of work, reflect that in `state/current.md`.

When a roadmap item turns into a durable structural choice, record that in `history/decisions/`.
