# Session State And History

This document distinguishes current working context from durable historical context.

The distinction matters because systems become difficult to reason about when short-term status and long-term rationale are mixed together.

## Session State

Session state captures what matters for continuing the current line of work.

It may include:

- current objective
- active tasks
- open questions
- blocking issues
- important temporary assumptions

Session state should be easy to update and easy to discard once it is no longer relevant.

## History And Decisions

History and decisions capture context that should remain useful after the current task or session ends.

They may include:

- why a structure was adopted
- why terminology changed
- what tradeoff a contributor accepted
- what interpretation should remain visible later

## Promotion Rule

When a point stops being merely situational and starts affecting future interpretation, it should move out of session state and into a durable document.

Examples:

- a repeated convention becomes a documented principle
- a structural tradeoff becomes a decision record
- a recurring evaluation lens becomes a review type

## Common Failure Modes

Watch for these failure modes:

- decision rationale hidden inside temporary status notes
- current blockers mixed into permanent definitions
- examples treated as if they were general principles
- chat history carrying important context that never reaches the repository

## Practical Implication

A healthy scaffold keeps current work easy to resume without letting temporary details distort the durable definition of the system.
