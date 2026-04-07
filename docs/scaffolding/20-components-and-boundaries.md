# Components And Boundaries

This document defines the primary components of the scaffold and the boundaries between them.

## Principles

Principles are durable constraints and interpretive rules.

Use principles when a statement should influence many parts of the system over time.

Principles are not:

- temporary status
- one-off implementation advice
- project-specific operating details

## Roles

Roles are responsibility-bearing positions within the system.

A role answers the question: who is responsible for a kind of work or judgment?

Roles are not:

- individual tasks
- quality criteria
- orchestration policies

## Tasks

Tasks are units of work.

A task answers the question: what work is being performed right now?

Tasks are not:

- durable responsibilities
- review lenses
- historical rationale

## Review Types

Review types are recurring lenses used to evaluate work.

A review type answers the question: what kind of judgment is being applied?

Examples might include:

- correctness review
- boundary compliance review
- documentation review
- usability review

Review types are not automatically roles. A role may perform a review, but the review lens itself should remain separately defined when it can be reused.

## Orchestration

Orchestration coordinates work across components.

It answers questions such as:

- which role should handle this task?
- what should happen first?
- when should review be applied?
- when should escalation occur?

Orchestration is not the same thing as a task or a role. It is the coordination logic around them.

## Workflow Standards

Workflow standards define project-level conventions for how work moves through a repository.

They answer questions such as:

- how commits should be structured
- what branch or review conventions apply
- how project documents should be updated
- what repository hygiene expectations exist

Workflow standards are not:

- system architecture
- task definitions
- current state
- durable decisions about why the system exists in its current form

Workflow standards often interact with orchestration, but they are not the same thing. Orchestration coordinates work; workflow standards define repository-level conventions that shape how that work is recorded and reviewed.

## Session State

Session state captures the current working focus, open questions, and active context needed to continue work coherently.

It is temporary or near-term by nature.

Session state is not:

- a durable principle
- a completed decision
- the full history of the system

## History And Decisions

History and decisions record why the system evolved the way it did.

This layer preserves durable reasoning that later contributors should be able to recover without reconstructing it from chat history.

History and decisions are not:

- current status notes
- implementation tasks
- general principles unless a principle was formally adopted from a decision

## Common Boundary Tests

Use these tests when placement is unclear:

- If it should remain true across many projects or revisions, it is probably a principle
- If it assigns responsibility, it is probably a role
- If it describes work to be done, it is probably a task
- If it describes a reusable evaluation lens, it is probably a review type
- If it coordinates sequence, routing, or escalation, it is probably orchestration
- If it defines commit, branch, review-flow, or document-update conventions for a project, it is probably a workflow standard
- If it describes what matters right now, it is probably session state
- If it explains why a structural choice was made, it belongs in history or decisions
