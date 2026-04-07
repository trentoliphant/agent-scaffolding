# Customizing The Scaffold

Use this guide when the base scaffold is helpful but your project needs adaptation.

## Preserve The Core Distinctions

Customization should not erase distinctions that are doing useful work.

Try to preserve:

- roles vs tasks
- review types vs roles
- system definition vs project guidance
- session state vs history and decisions

If you merge concepts, do it deliberately and explain why.

## Good Reasons To Customize

Customize when:

- your domain requires a role the base examples do not show
- your project has recurring review needs
- your orchestration needs explicit routing or escalation
- your team needs a different level of detail

## Common Safe Customizations

Common adaptations include:

- renaming example roles to fit a domain
- adding review types such as security, compliance, or usability
- adding a lightweight session-state file for multi-session work
- creating examples that reflect the real workflow of a project

## Changes That Need Extra Care

Be careful when:

- collapsing review into implementation
- turning temporary working notes into durable principles
- using examples as if they define the whole system
- creating new terms for concepts that already exist clearly

## Practical Heuristic

Before customizing, ask:

1. What problem is this change solving?
2. What layer does it belong to?
3. Is the change durable or temporary?
4. Will the change make the system easier to use?
5. Will the change make the system harder to understand later?

If the answer to the last question is yes, add documentation that makes the customization recoverable.
