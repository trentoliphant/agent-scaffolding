# AGENTS.md

This file defines the local operating contract for the research-to-design
example.

## Purpose

The purpose of this example is to show how a small harness can support both
investigation and design work without hiding role boundaries, verification, or
durable decisions.

## Working Rules

- Keep roles explicit even when one person or agent fills more than one role
- Keep research findings tied to a stated basis
- Keep design decisions tied to stated tradeoffs and constraints
- Keep open questions visible rather than resolving them silently
- Keep durable structural choices in `history/decisions/`

## Escalation Rules

- Escalate when research findings contradict the current objective
- Escalate when a design choice depends on unresolved research questions
- Escalate when a local convenience would blur the boundary between findings
  and decisions
- Escalate when a proposed workflow change would materially change scope,
  service commitments, or compliance obligations

## Update Rules

- Update `PLAN.md` when the work sequence changes
- Update `PROGRESS.md` when task status or verification state changes
- Update `state/current.md` when the active objective or main open questions
  change
- Update research artifacts when evidence or interpretation changes
- Update design artifacts when decisions, workflow structure, or tradeoffs
  change
- Add a decision record when a structural choice should outlive the current
  task

## Completion Rule

Do not treat work as complete only because a document exists.

Work is complete when:

- the intended artifact exists
- the relevant verification contract has been applied
- open questions are visible
- trace is preserved in `PROGRESS.md` or the artifact itself
- any durable structural lesson has been recorded
