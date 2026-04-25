# Domain Implementation Extensions

This guide explains how to extend the standard for a specific domain without
turning one domain implementation into the definition of the standard itself.

Use it when the core standard and baseline path are useful, but your project
needs domain-specific roles, verification, language, controls, or artifacts.

## Goal

The goal of a domain implementation is not to replace the standard.

The goal is to instantiate the standard for a real domain while keeping the
boundary between:

- reusable standard structure
- baseline implementation guidance
- domain-specific extensions

Good extension guidance should help a builder answer:

- which parts of the harness are domain-specific
- which parts still map back to the shared standard
- what belongs in domain modules instead of the standard core
- what should be promoted back into the standard only after repeated reuse

## What A Domain Implementation May Add

A domain implementation may add:

- domain-specific role names or role variants
- domain-specific task types or work item categories
- domain verification contracts
- domain terminology and evidence requirements
- compliance, privacy, audit, or approval overlays
- domain artifacts, templates, or operating conventions
- execution-system mappings tailored to the domain's actual environment

These additions are expected.
The important thing is to make the relationship to the core standard visible.

## What Should Stay Shared

Even when the implementation becomes highly specialized, keep these things
recoverable:

- which part defines roles
- which part defines tasks
- which part defines verification contracts
- which part defines orchestration
- which part defines trace expectations
- which part defines session state
- which part defines durable decisions

The domain may specialize all of them.
It should not blur them beyond recognition.

## Extension Mapping Questions

Before adding a domain module, ask:

1. What problem exists in this domain that the baseline does not express?
2. Is the missing concept domain-specific, or does it appear reusable across
   many domains?
3. Is this change a new role, a new verification contract, a workflow rule, a
   trace requirement, or a domain artifact?
4. Does the extension change portable meaning, or only local implementation?
5. Where should future readers look to understand the extension?

If those questions do not have clear answers, the extension probably needs a
cleaner boundary.

## Common Domain Extension Categories

The most common extension categories are:

### Domain Roles

Examples:

- triage nurse
- contract approver
- fraud analyst
- sales manager

These should still be defined as roles with responsibilities, not as loose
labels for whoever happens to act in a given runtime.

### Domain Verification Contracts

Examples:

- medical evidence sufficiency
- legal policy compliance
- pricing approval
- security review

These belong in domain verification modules when they define:

- what is being judged
- what criteria apply
- what verdicts are possible
- what next action each verdict triggers

### Domain Trace Fields

Examples:

- cited regulation
- customer segment
- case severity
- risk score
- model confidence explanation

These are appropriate when the baseline trace is too thin for the domain's
actual diagnosis, review, or audit needs.

### Domain Overlays

Examples:

- regulatory controls
- privacy handling rules
- dual-approval requirements
- escalation ladders for high-risk work

These often affect orchestration, verification, and expertise thresholds at
the same time.
Keep the boundary between those concerns recoverable even when they interact.

### Research-Heavy Investigation Extensions

Examples:

- evidence discipline for factual claims
- explicit open-question tracking
- exploratory plan mutation rules

These are appropriate when a domain implementation spends real time
investigating, comparing, or assessing before it can recommend, design, or
implement.
They should remain visible as domain extensions rather than being hidden in
informal working habits.

## Safe Extension Pattern

A safe default pattern is:

1. Start from the baseline implementation shape.
2. Add only the domain modules the work actually needs.
3. Name each extension category explicitly.
4. Record how each extension maps back to the standard modules.
5. Promote a domain pattern back into the standard only after repeated
   cross-domain reuse is visible.

That pattern keeps the domain implementation practical without making it
silently redefine the standard.

## Where Extensions Should Live

Use these placement rules:

- reusable standard concepts belong in `docs/scaffolding/`
- practical builder guidance belongs in `docs/guide/`
- domain-specific examples belong in `docs/examples/`
- domain-specific project documents belong in the implementation itself
- durable rationale for structural extension choices belongs in
  `history/decisions/` or the implementation's local equivalent

If a domain concept seems to fit multiple layers, document the ambiguity rather
than collapsing the layers casually.

## Promotion Rule

Do not promote a domain extension into the standard core just because it is
important in one domain.

Promote it only when it improves:

- inspectability across many domains
- interoperability between implementations
- the ability to evolve the scaffold safely

If the benefit is local to one domain, keep it as a domain extension.

## Example Mapping

A healthcare implementation might add:

- roles: clinician reviewer, case coordinator
- verification contracts: evidence sufficiency, policy compliance
- trace fields: patient context class, evidence source, risk level
- overlays: privacy restrictions, escalation for high-risk cases

Those additions still map back to the same shared structure:

- roles remain roles
- verification remains verification
- trace remains trace
- escalation remains orchestration
- durable rationale remains history and decisions

The domain changes the content, not the category system.

## Common Extension Mistakes

Watch for these mistakes:

- treating one domain's terminology as if it were the general standard
- hiding verification criteria inside role descriptions
- burying domain-specific escalation rules inside runtime behavior
- promoting domain artifacts into the baseline before other builders need them
- using domain pressure as a reason to collapse state, trace, and decisions
- assuming a regulated domain's controls should automatically apply everywhere
- treating exploratory work as if it should follow a fixed plan even when new
  findings legitimately redirect it
- mixing raw evidence, interpretation, and recommendation so tightly that later
  readers cannot tell which claims are directly supported

## Practical Heuristic

If you removed the domain-specific nouns from the harness, ask:

1. Would the underlying structure still make sense?
2. Would the extension's relationship to roles, tasks, verification, and trace
   still be visible?
3. Would a reader know what is standard, baseline, and domain-specific?

If the answer is no, the domain implementation is carrying too much hidden
structure.

## Research-Heavy Domains

Some domains need a more explicit extension layer for investigative work before
they can support design, implementation, or stakeholder decisions.

When that is true, the most useful additions are often:

- evidence discipline: keep raw evidence, observations, and interpretation
  distinguishable enough that later readers can inspect the basis of important
  claims
- open-question tracking: treat unresolved questions as first-class outputs
  rather than burying them in narrative prose
- exploratory plan mutation: record when the investigation plan changes
  because findings exposed a better next question, a dead end, or a narrower
  scope

Those additions are still domain extensions.
They do not change the shared scaffold categories.

Map them back like this:

- evidence discipline extends verification and trace expectations
- open-question tracking extends trace and active state
- exploratory plan mutation extends orchestration and planning guidance

Use these additions when:

- claims need visible basis and caveats
- findings routinely produce new questions
- the work cannot be planned completely in advance without pretending to know
  more than is actually known

Do not promote a full research-document system into the baseline by default.
Add only the specific investigative structure the domain actually needs.

## Current Promoted Examples

Use the current example set to study different extension patterns:

- [../examples/research-to-design/README.md](../examples/research-to-design/README.md)
  for a document-first research-to-design handoff
- [../examples/software-project/README.md](../examples/software-project/README.md)
  for coding-focused scaling with task, review, and workflow assets
- [../examples/regulated-approval/README.md](../examples/regulated-approval/README.md)
  for regulated or approval-heavy overlays
- [../examples/expertise-tiered-review/README.md](../examples/expertise-tiered-review/README.md)
  for expertise profiles and multi-tier review

Study them as a curated set of non-overlapping patterns.
They are meant to show different extension pressures, not to prescribe one
universal implementation shape.

## When To Add Another Guide Or Module

Add more domain-specific guidance only when:

- repeated work in the domain exposes the same missing pattern
- builders need reusable domain templates or examples
- compliance or risk requires explicit handling beyond the baseline
- multiple implementations in the same domain would benefit from a shared
  extension layer

Start with implementation guidance or examples first.
Promote only what proves durable and reusable.
