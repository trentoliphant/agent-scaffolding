# CODING STANDARDS

> Status: Transitional
> Alignment: Partially aligned with the open-standard rewrite
> Intended role: optional implementation-specific template for coding projects
> Use it for: baseline coding implementations, not as standard core

## Purpose

This document defines coding and implementation standards for the project.

It governs how code should be written, organized, tested, and maintained.
It does not define system architecture, project sequencing, or workflow
governance.

Architecture is defined in `SYSTEM_MODEL.md`.
Process and execution rules are defined in the project's operating model or equivalent orchestration/workflow document.

---

## Core principles

- Prefer clarity over cleverness
- Prefer explicitness over implicit behavior
- Prefer simple, composable solutions over premature abstraction
- Keep code aligned with the system model
- Minimize hidden coupling and side effects
- Write code that is understandable by future contributors and agents

---

## Scope

This document applies to:

- Source code
- Tests
- Supporting implementation files
- Language-specific coding patterns

This document does not define:

- System architecture
- Project plan or sequencing
- Git / branching / commit conventions
- Human or agent workflow rules

---

## Global standards

### Required

- Follow established project patterns unless explicitly changing them
- Keep responsibilities clear and localized
- Public interfaces must be explicit and understandable
- Code must be testable
- New behavior must include appropriate tests
- Avoid hidden side effects
- Avoid duplicating business logic across components

### Preferred

- Small, focused modules and functions
- Descriptive names over short clever names
- Straight-line code where practical
- Explicit data flow
- Reuse through composition before inheritance or heavy abstraction

### Avoid

- Clever but opaque code
- Unnecessary abstractions
- Hidden mutation of shared state
- Duplicated logic across files or components
- Large multi-purpose functions without clear boundaries

---

## File and module organization

### Required

- Files should have a clear primary purpose
- Modules should align with project component boundaries
- Tests should live near or clearly map to the code they validate
- New files should follow the existing repository structure

### Preferred

- One coherent concept per file or module
- Related helpers grouped logically
- Public and internal interfaces clearly distinguishable

### Avoid

- Files that mix unrelated concerns
- Utility files that accumulate unrelated helpers
- New top-level directories without explicit need

---

## Naming conventions

### Required

- Names must reflect actual responsibility
- Public names must be descriptive
- Avoid misleading or overly broad names

### Preferred

- Domain language aligned with `SYSTEM_MODEL.md`
- Verb-oriented names for actions/functions
- Noun-oriented names for entities/structures

### Avoid

- Generic names like `helper`, `stuff`, `misc`, `manager` unless truly accurate
- Names that imply architecture not actually present
- Abbreviations that reduce clarity

---

## Functions and methods

### Required

- Functions and methods should have a clear purpose
- Inputs and outputs should be understandable
- Public functions should avoid surprising side effects
- Complex behavior should be broken into understandable units

### Preferred

- Small focused functions
- Explicit return values
- Argument lists that remain understandable without external context

### Avoid

- Functions that do too many unrelated things
- Long chains of hidden mutation
- Overloaded behavior that depends on subtle flags unless clearly justified

---

## State and side effects

### Required

- State changes should be explicit
- Side effects should be visible at meaningful boundaries
- Shared mutable state must be handled carefully

### Preferred

- Pass required state explicitly
- Keep mutation near the point of use
- Isolate impure operations from pure logic when practical

### Avoid

- Hidden global state
- Side effects buried inside utility functions
- Implicit dependencies on ambient context unless intentional and documented

---

## Error handling

### Required

- Errors must be handled intentionally
- Error behavior should match the importance of the failure
- Public-facing failures should be understandable
- Silent failure is not allowed unless explicitly justified

### Preferred

- Fail fast on invalid internal assumptions
- Use specific exceptions / error types where appropriate
- Preserve useful debugging context

### Avoid

- Broad catch-all handling without good reason
- Swallowing errors silently
- Returning ambiguous values instead of signaling failure clearly

---

## Comments and documentation

### Required

- Public interfaces should be documented where needed
- Comments must explain why, not restate obvious code
- Non-obvious constraints or tradeoffs should be captured

### Preferred

- Concise docstrings or comments
- Documentation of assumptions at important boundaries
- Notes for behavior that may otherwise appear surprising

### Avoid

- Commenting every obvious line
- Stale comments
- Large comment blocks that replace better code structure

---

## Testing standards

### Required

- New behavior must be tested
- Tests must validate intended behavior
- Tests must not rely on accidental or undefined behavior
- Failing edge cases discovered during implementation should be captured where appropriate

### Preferred

- Tests that read as behavior specifications
- Clear separation of setup, action, and assertion
- Tests focused on one meaningful behavior at a time
- Use fixtures/helpers to reduce duplication when helpful

### Avoid

- Tests that merely mirror implementation details
- Brittle tests tied to incidental structure
- Overly broad tests that fail for many unrelated reasons
- Updating tests to match broken behavior without validating intent

---

## Refactoring standards

### Required

- Refactoring must preserve intended behavior unless a change is explicit
- Refactoring must stay within step scope unless otherwise approved

### Preferred

- Small, targeted refactors
- Refactors that improve clarity, locality, or maintainability

### Avoid

- Opportunistic refactors unrelated to the current step
- Mixing major refactors with behavior changes without clear reason

---

## Dependency standards

### Required

- Add dependencies deliberately
- New dependencies must have a clear justification
- Prefer existing project tools and patterns when sufficient

### Preferred

- Standard library / built-in tools where reasonable
- Small, well-understood dependencies

### Avoid

- Adding dependencies for trivial convenience
- Overlapping dependencies with similar purpose
- Hiding architectural complexity behind packages without understanding tradeoffs

---

## Language-specific standards

Add only the sections relevant to the project.

---

## Python standards

### Required

- Type hints on public function and method signatures
- Clear module structure
- Tests written with the project’s chosen test framework
- Imports organized consistently
- Exceptions handled intentionally

### Preferred

- `pathlib` over raw path string manipulation
- Dataclasses or equivalent structured types for simple data containers
- Small, explicit functions
- Explicit return values
- Use enums/constants instead of magic strings where appropriate

### Avoid

- Bare `except`
- Hidden mutation across long functions
- Excessive dynamic behavior when simpler explicit code would work
- Unclear mixing of IO, transformation, and orchestration logic

---

## TypeScript / JavaScript standards

### Required

- Explicit types at important boundaries
- Avoid `any` unless explicitly justified
- Async behavior handled intentionally
- Public APIs clearly typed

### Preferred

- Small, composable functions/components
- Clear separation of data, logic, and presentation
- Use shared types/interfaces for stable contracts

### Avoid

- Unchecked implicit coercion
- Large files mixing many concerns
- Silent promise failures
- Type assertions used to bypass actual uncertainty

---

## SQL standards

### Required

- Queries must be understandable and maintainable
- Schema changes must be explicit
- Table and column names must be consistent
- Business-critical logic should not be hidden in ad hoc queries

### Preferred

- Clear formatting and aliasing
- Consistent naming patterns for IDs, timestamps, and foreign keys
- Separation between schema definition, migration, and query logic

### Avoid

- Opaque one-line queries
- Inconsistent naming
- Duplicating business logic across many queries
- Mixing temporary experimentation into production query files

---

## Shell / scripting standards

### Required

- Scripts must be readable and safe
- Side effects must be intentional
- Destructive operations must be obvious

### Preferred

- Small focused scripts
- Clear variable names
- Defensive checks around important operations

### Avoid

- Dense one-liners in important scripts
- Hidden destructive behavior
- Scripts that assume environment state without validation

---

## Project-specific additions

Add project-specific implementation conventions here.

Examples:
- logging style
- configuration access patterns
- serialization patterns
- file layout rules
- API design conventions

---

## Exception handling for standards

These standards are the default.

If a step or project requires deviation:

- keep the deviation intentional
- keep it local if possible
- document the reason when the deviation is meaningful

---

## Review expectations

Code review — whether by agent or human — should evaluate:

- clarity
- scope adherence
- consistency with this document
- consistency with `SYSTEM_MODEL.md`
- test realism
- maintainability

---

## What this document is not

This document does not define:

- Architecture
- Planning or sequencing
- Step execution process
- Commit / branch / git workflow conventions
- Human approval rules
