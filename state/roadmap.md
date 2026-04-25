# Roadmap

This document lists likely next improvements for the repository.

It is a planning aid, not a durable definition of the scaffold. Items here may change as the repository evolves.

## Near Term

1. Add integration guidance for common execution systems while preserving
   model and engine agnosticism
2. Define how domain implementations should extend the standard and contribute
   improvements back safely
3. Refresh or reclassify remaining transitional materials that still carry
   older coding-first or starter-kit-derived framing
4. Decide whether the standard, baseline implementation, and domain
   implementations should remain in one repository or later split

## Medium Term

1. Extract templates or sharper guide material from the completed curated
   example set when repeated builder need justifies it
2. Add more promoted extension artifacts only if future builder pressure
   exposes a need not addressed by the current example set
3. Create a contribution model that welcomes domain experts without weakening
   the standard's coherence
4. Evaluate whether older reference and migration materials should remain in
   this repository long term
5. Decide what release or versioning shape the open standard should use

## Watch Items

These are not immediate commitments, but they should remain visible:

1. Avoid over-formalizing the standard before real usage pressures justify it
2. Avoid turning one company's proprietary domain patterns into the open
   standard by default
3. Keep contributor-facing refinement from overwhelming builder-facing usability
4. Keep the trace and evolution requirements lightweight enough to be adoptable
5. Preserve the distinction between inspectable governance and specific model
   behavior claims
6. Keep coding-focused examples useful without letting them redefine the
   domain-neutral baseline
7. Keep the promoted example set small enough to stay teaching-oriented rather
   than becoming a catalog of domain implementations

## Completion Rule

When a roadmap item becomes the active frontier of work, reflect that in `state/current.md`.

When a roadmap item turns into a durable structural choice, record that in `history/decisions/`.
