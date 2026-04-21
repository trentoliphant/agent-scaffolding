# Principles

These principles apply across the standard.

They are not workflow steps. They are durable constraints and interpretive
rules that shape how the standard should be understood, extended, and revised.

## 1. Separate Layers

Do not collapse distinct layers into one another when the distinction matters.

Important distinctions include:

- standard definition vs implementation guidance
- open standard vs baseline implementation vs domain implementation
- roles vs tasks
- execution vs verification
- session state vs traces vs historical rationale
- observed outcomes vs interpretations vs adopted changes

## 2. Modularity Before Completeness

The standard should define composable modules rather than one monolithic
process.

Add a concept to the core only when it is reusable across domains and improves:

- inspectability
- interoperability
- safety
- scaffold evolution

## 3. Model And Runtime Agnosticism

The standard should not depend on one model family or one execution engine.

It may describe integration points and common expectations, but those
integration details should not become the core definition.

## 4. Human And Machine Composability

Roles should be defined by responsibility and boundaries, not by whether a
human or machine performs them.

The same structural role may be filled by:

- a human
- a machine
- a human-supervised machine
- a machine-assisted human

The standard should make those substitutions explicit and inspectable.

## 5. Verification Must Stay Explicit

Verification is not just "good execution."

The scaffold should keep explicit:

- what is being verified
- what criteria apply
- what verdicts are possible
- where the verdict is recorded

This remains true even when the executor and verifier are both machines.

## 6. Traceability Is Required

The scaffold should preserve enough evidence from execution to support:

- review
- debugging
- auditability
- later scaffold improvement

A harness that cannot be inspected after the fact cannot improve reliably.

## 7. Learn From Use

The scaffold should include a structured path for learning from repeated use.

That means preserving:

- assumptions a task relied on
- whether those assumptions held
- what failed or degraded
- what part of the harness may need revision

## 8. Human Legibility Matters

The standard must remain understandable to a thoughtful human reader.

Prefer:

- explicit definitions
- stable terminology
- short explanatory sections
- clear module boundaries
- documents with a single purpose

## 9. Usability Is Required

A standard that is conceptually elegant but difficult to adopt is incomplete.

The standard should make it possible to:

- start with a minimal baseline
- add modules only when needed
- understand how the modules work together
- extend the harness without redefining the whole system

## 10. Improvement Should Be Reviewable

Changes to the scaffold should not appear as silent drift.

If usage suggests the harness should evolve, the proposed change should be:

- visible
- reviewable
- attributable
- placed in the correct layer
