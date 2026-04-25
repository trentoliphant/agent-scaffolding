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
6. Read
   [execution-system-integration.md](execution-system-integration.md)
   when you need to map the harness onto a real runtime without making that
   runtime part of the standard core.
7. Read
   [domain-implementation-extensions.md](domain-implementation-extensions.md)
   when your project needs domain-specific roles, verification, or overlays
   without redefining the shared standard.
8. Review
   [../examples/research-to-design/README.md](../examples/research-to-design/README.md)
   when you want to study the first promoted domain-extension pattern and a
   non-software research-to-design handoff.
9. Review [../examples/minimal/README.md](../examples/minimal/README.md)
   before adding more structure.
10. Review
   [../examples/software-project/README.md](../examples/software-project/README.md)
   when you want a coding-focused scaling pattern.
11. Review
   [../examples/regulated-approval/README.md](../examples/regulated-approval/README.md)
   when your domain needs visible approvals, compliance review, or escalation
   by risk.
12. Review
   [../examples/expertise-tiered-review/README.md](../examples/expertise-tiered-review/README.md)
   when the same role needs different autonomy or review thresholds by
   expertise.
13. Use [starter-kit-adoption.md](starter-kit-adoption.md) only when older
   starter-kit-derived patterns are relevant to your adoption or migration.

## Current Example Set

The current curated example set is:

- one minimal baseline example
- one coding-focused scaling pattern
- one document-first research-to-design pattern
- one regulated approval pattern
- one expertise-tiered review pattern

Additional examples should fill a builder need that this set does not already
address.

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
- a small local harness definition describing roles, tasks, verification, and
  traces
- one lightweight workflow loop
- a place to record durable decisions

You do not need a complex orchestration system before the work itself becomes
complex enough to require one.
