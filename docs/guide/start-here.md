# Start Here

This guide is for builders who want to use this repository as the basis for a
domain harness built on the open standard.

Do not start by copying every concept at once. Start with the smallest version
that makes responsibilities, verification, traces, and improvement more
explicit in your project.

## Recommended Path

1. Read [../scaffolding/00-overview.md](../scaffolding/00-overview.md) to
   understand the standard and its core modules.
2. Read
   [../scaffolding/50-traces-verification-and-evolution.md](../scaffolding/50-traces-verification-and-evolution.md)
   to understand the parts most likely to shape real execution quality.
3. Read [baseline-implementation.md](baseline-implementation.md) to understand
   how the practical baseline relates to the standard.
4. Use [minimal-adoption.md](minimal-adoption.md) to create a first working
   baseline.
5. Use [customizing.md](customizing.md) to add optional modules such as domain
   rules, expertise tiers, or runtime integration profiles.
6. Review [../examples/minimal/README.md](../examples/minimal/README.md)
   before adding more structure.
7. Use [starter-kit-adoption.md](starter-kit-adoption.md) only when older
   starter-kit-derived patterns are relevant to your adoption or migration.

## Material Status Rule

When choosing what to read next:

- prefer `Current` materials first
- use `Transitional` materials when you need practical examples or baseline
  assets that are still being refined
- use `Reference/Migration` materials only when translating older patterns
- ignore `Legacy` and `Incubating` materials unless you have a specific reason

Use [repository-status.md](repository-status.md) when you need the explicit
classification map.

## The Default Assumption

The default builder path is:

- adopt the standard in a minimal form
- use the baseline as a recommended starting shape rather than a required
  implementation
- add extensions only when your workflow needs them
- treat older reference implementations as learning material, not as the
  default starting point

## What To Aim For First

Your first adoption should make these things clearer:

- what work the harness is responsible for
- which roles exist and who or what fills them
- what must be verified before work is accepted
- what trace from execution is preserved
- where durable harness decisions are recorded

If the scaffold does not improve those five things, it is too abstract or too
heavy for the current stage.

## Start Small

For many projects, the first useful version only needs:

- a short operating contract for how agents work in the repository
- a small standard definition describing roles, tasks, verification, and traces
- one lightweight workflow loop
- a place to record durable decisions

You do not need a complex orchestration system before the work itself becomes
complex enough to require one.
