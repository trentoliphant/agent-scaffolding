# Principles

These principles apply across the scaffold.

They are not steps in a workflow. They are durable constraints and preferences that shape how the scaffold should be interpreted and evolved.

## 1. Separate Layers

Do not collapse distinct layers into one another when the distinction matters.

Important distinctions include:

- system definition vs system application
- roles vs tasks
- execution vs review
- current state vs historical reasoning
- orchestration vs implementation details
- facts vs interpretations vs asserted outputs

## 2. Iteration Over Replacement

The scaffold is expected to evolve.

Prefer revising and extending existing structure over repeatedly replacing it. Replacement is justified when the existing structure no longer preserves meaning clearly.

## 3. Structure Before Expansion

When a new idea appears, first determine what kind of thing it is.

Ask:

- Is it a principle?
- Is it a role?
- Is it a task pattern?
- Is it a review type?
- Is it orchestration logic?
- Is it session state?
- Is it historical rationale?

Expansion without placement produces confusion quickly.

## 4. Human Legibility Matters

The scaffold must remain understandable to a thoughtful human reader.

Prefer:

- explicit definitions
- stable terminology
- short explanatory sections
- cross-references where needed
- documents with a clear purpose

## 5. Durable Context Over Transient Chat

Important context should not remain trapped in conversation history.

If a distinction, constraint, or decision repeatedly matters, promote it into the repository in the correct layer.

## 6. Review Is Cross-Cutting

Review is not automatically a role.

Review can apply to planning, architecture, implementation, documentation, orchestration, or outputs. When there is ambiguity between a role and a review type, preserve that ambiguity until it can be resolved cleanly.

## 7. Usability Is Required

A scaffold that is conceptually elegant but difficult to apply is incomplete.

The system should make it possible to:

- start small
- adopt incrementally
- understand component interactions in practice
- learn from examples, not only definitions

## 8. Clarity Over Unnecessary Abstraction

Abstraction is only useful when it improves understanding, reuse, or consistency.

If a change adds layers, terms, or categories without making the system clearer or more usable, it should be reconsidered.
