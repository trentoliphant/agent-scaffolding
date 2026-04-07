# Reference Implementations

This section identifies real working systems that matter to the development of the scaffold.

These are not the scaffold definition itself, and they are not only downstream examples. They are working reference implementations that can also serve as extraction sources for scaffold patterns.

## Purpose

Use this section to capture sources that are relevant because they are:

- usable packages in their own right
- evidence of how the scaffold works in practice
- sources from which reusable scaffold patterns may be extracted

## Relationship To Other Layers

Keep these distinctions explicit:

- `docs/scaffolding/` defines the generalized scaffold
- `docs/guide/` explains how to apply the scaffold
- `docs/examples/` shows illustrative applications within this repository
- `docs/reference/` points to real working systems that both inform and embody parts of the scaffold

Reference implementations may influence scaffold refinement, but their instance-level documents should not be copied into scaffold definitions without generalization.

## Current Reference Source

### `starter_kit`

Location:

- `/Volumes/Home/Users/trentoliphant/Development/starter_kit`

Current interpretation:

- `starter_kit` is a usable starter package
- `starter_kit` is a working reference implementation
- `starter_kit` is one source from which scaffold patterns have been extracted

This means it should not be treated as only:

- a downstream example
- the scaffold itself

## Usage Rule

When using a reference implementation to refine the scaffold:

1. identify the reusable pattern
2. decide whether it belongs in scaffold definition, guide material, examples, or templates
3. preserve the distinction between generalized concepts and instance-level documents

## Current Note

This section is intentionally lightweight.

At this stage, a simple named place for reference implementations is enough. It makes the relationship visible without creating a heavy new subsystem.
