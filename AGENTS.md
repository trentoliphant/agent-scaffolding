# AGENTS.md

## Purpose

This repository is the working source of truth for a scaffolding system for AI-assisted work.

Agents working here should help the repository serve two audiences at once:

- builders applying the scaffold in real projects
- contributors refining the scaffold itself

Builders are the primary audience for the scaffold. Contributors are the audience for the repository's evolution.

The repository should become clearer and more usable over time, not more abstract for its own sake.

## Repo Structure

Keep a clear separation between layers:

- `docs/scaffolding/` defines the system
- `docs/guide/` explains how to apply the system
- `docs/examples/` shows concrete applications
- `history/decisions/` records durable rationale

Do not collapse system definition and system application into the same document unless there is a strong reason to do so.

## Working Rules

- Prefer incremental refinement over wholesale replacement
- Preserve established terminology unless a change clearly improves clarity
- Keep distinctions explicit when concepts are easy to conflate
- Promote durable insights into repository files rather than leaving them in chat
- Prefer precise local edits over broad restructuring
- Surface unresolved design tension rather than hiding it

## Placement Rules

When adding or revising content, place it in the appropriate layer:

- system definition belongs in `docs/scaffolding/`
- usage guidance belongs in `docs/guide/`
- concrete applications belong in `docs/examples/`
- historical rationale belongs in `history/decisions/`

If a concept seems to fit multiple layers, state the ambiguity explicitly and preserve the distinction until it is resolved.

## Expected Agent Behavior

When working in this repository, the agent should:

1. Read relevant context files before making major edits
2. Update existing files in place when possible
3. Keep system definition, application guidance, and examples separate
4. Preserve alignment across related documents
5. Call out inconsistencies when they are discovered
6. Distinguish between proposing, implementing, and documenting a change
7. Avoid silently changing established meaning
8. Consider both conceptual clarity and builder usability in every change

## Editing Rules

- Make the smallest change that correctly advances the work
- Do not reformat large sections unless it improves clarity
- Do not rename files or concepts casually
- Do not remove historical rationale without explicit reason
- When restructuring, update dependent documents and record the rationale

## Review Checks

Before finishing work, check both audiences:

For builders:

- Is there a clear starting point?
- Is the guidance actionable?
- Is there at least one concrete example?

For contributors:

- Are distinctions precise?
- Are related documents still aligned?
- Is new complexity justified?

## Default Assumption

If a conversation produces durable structure, guidance, or rationale, update the repository so that insight is preserved outside transient chat history.
