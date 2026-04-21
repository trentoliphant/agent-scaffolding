# Customizing The Standard

Use this guide when the base standard is helpful but your project needs local
adaptation.

The standard is meant to be modular. Customization is expected. The key is to
extend it without collapsing distinctions that preserve clarity, portability,
and reviewability.

## Preserve The Core Distinctions

Customization should not erase distinctions that are doing useful work.

Try to preserve:

- standard definition vs implementation guidance
- roles vs tasks
- execution vs verification
- session state vs traces vs history and decisions
- core modules vs optional extensions

If you merge concepts, do it deliberately and explain why.

## Good Reasons To Customize

Customize when:

- your domain needs roles the baseline examples do not show
- your project needs domain-specific verification criteria
- your workflow needs explicit routing, escalation, or approval rules
- your implementation needs expertise tiers with different autonomy levels
- your runtime needs explicit integration guidance
- your project needs compliance, privacy, or audit overlays

## Common Safe Customizations

Common adaptations include:

- renaming example roles to fit a domain
- assigning a role to a human, a machine, or a mixed loop
- adding verification contracts such as security, compliance, or usability
- defining autonomy profiles such as junior, regular, and senior
- adding a lightweight session-state file for multi-session work
- adding trace fields that matter in a specific runtime or domain
- starting from the templates and trimming them down for local needs

## Changes That Need Extra Care

Be careful when:

- collapsing verification into execution
- hiding trace requirements inside role descriptions
- turning temporary working notes into durable principles
- treating one domain module as if it defines the whole standard
- creating new terms for concepts that are already clear
- baking one runtime or model provider into the standard core

## Practical Heuristic

Before customizing, ask:

1. What problem is this change solving?
2. Is this a core concept, an extension, or an implementation detail?
3. Is the change durable or temporary?
4. Will the change make the harness easier to use?
5. Will the change make the harness harder to transfer or inspect later?

If the answer to the last question is yes, add documentation that makes the
customization recoverable.

## Common Extension Categories

The most common extension categories are:

- autonomy or expertise profiles
- domain verification modules
- runtime integration profiles
- workflow standards for a specific repository or organization
- regulated-domain overlays

These are valuable, but they should plug into the standard rather than redefine
the standard silently.
