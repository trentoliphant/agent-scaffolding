# DESIGN STANDARDS

> Status: Incubating
> Alignment: Not yet aligned with the current open-standard rewrite
> Intended role: earlier design-domain adapter material
> Use it for: reference or future integration work, not as current standard core

## Purpose

This document defines standards for design artifacts, design steps, and
design decisions in a structured design project.

It governs how design work is written, organized, validated, and maintained.
Operating model, workflow practices, and execution governance are defined
elsewhere.

---

## Core principles

- Decisions must be explicit and traceable
- Tradeoffs must be stated, not implied
- Open questions are first-class artifacts
- Provisional designs are preferable to premature closure
- Invariants are load-bearing and must be treated as such
- Scope boundaries prevent design sprawl
- Later phases depend on earlier phases being stable

---

## Design artifact standards

### What a design artifact is

A design artifact is a document produced by a design step. It captures
decisions, models, constraints, or workflows at a level of detail sufficient
for the next phase of work to proceed without ambiguity.

A design artifact is not:
- Implementation code or pseudocode (unless explicitly in scope)
- A planning document (that is PLAN.md)
- A progress record (that is PROGRESS.md)
- A meeting note or scratch pad

### Required properties of every design artifact

- Has a clear stated purpose
- Identifies what decisions it resolves
- Identifies open questions it defers
- States dependencies on other design artifacts
- Has a stability marker (see below)
- Is understandable without oral explanation

### Stability markers

Every design artifact carries one of three stability markers:

**Provisional** — the artifact captures current thinking but is expected
to change as later design work reveals new constraints or conflicts.
Downstream artifacts should not treat provisional decisions as settled.

**Stable** — the artifact has been reviewed, conflicts resolved, and
downstream work may depend on it. Changes require explicit escalation.

**Locked** — the artifact is complete for the current design phase and
will not change without a major scope or constraint revision. Changes
require human approval.

Mark stability explicitly at the top of each artifact. Default is
Provisional until explicitly promoted.

---

## How to write a domain entity definition

A domain entity definition must include:

- **Name** — the canonical name used consistently across all artifacts
- **Purpose** — one sentence describing what this entity represents
- **Responsibilities** — what this entity owns and tracks
- **Key attributes** — the properties that define it (not an exhaustive
  schema, but the properties that matter for design decisions)
- **Invariants** — rules that must always hold for this entity
- **Relationships** — how it relates to other entities, with cardinality
- **Constraints** — what this entity explicitly does not own or do

Do not include implementation details (column types, indexes, ORM
annotations) in a domain entity definition. Those belong in a later
technical artifact.

### Example structure

```
### Account

Purpose: Represents a financial account owned by or associated with an Entity.

Responsibilities:
- Tracks balance and transaction history for one currency and account type
- Maintains the ledger of all entries affecting this account

Key attributes:
- Account type (asset, liability, equity, income, expense)
- Currency
- Owner entity
- Opening date
- Current balance (derived)

Invariants:
- Balance is always derivable from transaction history
- Account type never changes after creation
- Accounts are never deleted; they are closed

Relationships:
- Belongs to one Entity
- Has many Transactions
- May have one parent Account (for sub-account hierarchies)

Constraints:
- Does not own tax basis calculations (those belong to Position)
- Does not enforce double-entry rules directly (that is the Transaction invariant)
```

---

## How to write an invariant

An invariant is a rule that must always hold. It is not a preference,
a default, or a guideline. Invariants are the hardest constraints in the
system.

Every invariant must:
- Be stated as an unconditional assertion
- Name the entity or boundary it applies to
- State the consequence of violation (data corruption, legal exposure,
  audit failure, etc.)
- Be traceable to a source (business rule, legal requirement, accounting
  principle, explicit design decision)

### Invariant format

```
**Invariant:** [entity or boundary] — [assertion]
**Source:** [business rule / legal / accounting principle / design decision]
**Consequence of violation:** [what breaks or becomes invalid]
```

### Example

```
**Invariant:** Transaction — a posted transaction is immutable
**Source:** Audit trail requirement; cash basis accounting principle
**Consequence of violation:** Historical balances become untrustworthy;
audit trail is invalid
```

Invariants are not negotiable during implementation. If an implementation
need appears to require violating an invariant, that is a class 4
architectural issue — stop and escalate.

---

## How to write a workflow definition

A workflow definition describes a process in terms of states, transitions,
actors, and rules.

Every workflow definition must include:

- **Name** — canonical name used consistently
- **Purpose** — what user or system need this workflow serves
- **Actors** — who or what initiates or participates
- **States** — the discrete states an artifact moves through
- **Transitions** — what triggers movement between states, and any
  guards or conditions
- **Invariants** — rules that must hold across the workflow
- **Open questions** — unresolved decisions that affect this workflow

Do not include UI details or implementation details in a workflow
definition. Those belong in later artifacts.

---

## How to document a decision

When a design decision is made — especially one that forecloses
alternatives — record it explicitly.

Every decision record must include:

- **Decision** — what was decided, stated clearly
- **Context** — why this decision was needed
- **Alternatives considered** — what else was evaluated
- **Rationale** — why this option was chosen
- **Tradeoffs** — what is accepted or given up
- **Consequences** — what this decision constrains downstream
- **Status** — Provisional / Stable / Locked

Decisions that foreclose future sophistication must explicitly state
what they foreclose and under what conditions the decision should be
revisited.

---

## How to handle open questions

An open question is a design decision that has not yet been resolved.
Open questions are first-class artifacts — they must be tracked, not
buried.

Every open question must include:

- **Question** — what needs to be decided
- **Why it matters** — what downstream work it blocks or affects
- **Options identified** — what the candidate answers are, if known
- **Resolution criteria** — what information or event would allow
  this to be resolved
- **Owner** — who is responsible for resolving it (human or deferred
  to a specific future step)

Open questions do not block a step from completing unless they are
explicitly marked as blocking. A step may complete with open questions
carried forward, provided those questions are recorded and their
downstream impact is noted.

---

## Design step completeness criteria

A design step is complete when:

- The specified artifact exists and has a stability marker
- All decisions required by the step are documented
- All open questions discovered during the step are recorded
- Dependencies on other design artifacts are identified
- No out-of-scope design work was performed
- PROGRESS.md and HISTORY.md are updated per the completion gate

A design step is not complete because:
- The artifact looks finished
- The artifact is long
- No open questions remain (open questions are expected and normal)

---

## Provisional vs stable promotion rules

Promote an artifact from Provisional to Stable when:

- The artifact has been reviewed against dependent artifacts
- No conflicts with other stable artifacts exist
- Open questions within the artifact do not affect its core decisions
- The artifact is being depended upon by the next phase

Promote from Stable to Locked only when:

- The phase that produced it is complete
- Implementation or later design phases are depending on it
- Human review has confirmed correctness

Do not promote stability markers automatically. Promotion is an explicit
act recorded in HISTORY.md.

---

## Scope discipline for design steps

- Do not design future-phase features within a current-phase step
- Do not make implementation decisions in design artifacts unless
  explicitly in scope
- Do not resolve open questions by making undocumented assumptions
- Do not treat a design decision as made unless it is recorded

If scope creep is tempting, classify it as an issue per
OPERATING_MODEL.md before acting.

---

## Cross-artifact consistency rules

Design artifacts must be consistent with each other. Inconsistency
is a design issue, not a documentation issue.

When an inconsistency is discovered:

- Identify which artifact is authoritative for the conflicting decision
- Update the non-authoritative artifact to align
- Record the resolution in HISTORY.md
- If authority is unclear, escalate to human review

The authority order for design artifacts mirrors the document hierarchy:
constraints and invariants take precedence over entity definitions, which
take precedence over workflow definitions, which take precedence over
boundary definitions.

---

## What design standards do not govern

- Git workflow (WORKFLOW_STANDARDS.md)
- Operating model and issue classification (OPERATING_MODEL.md)
- Project scope and phase sequencing (PLAN.md and PROJECT_CHARTER.md)
- Technical implementation standards (a separate adapter document
  when implementation begins)

---

## Deviation rules

These standards define the default for design-phase work.

If a step requires deviation:

- Make the deviation explicit in the step spec
- Keep it narrow in scope
- Record the reason in HISTORY.md if meaningful
- Do not silently drift from the standard
