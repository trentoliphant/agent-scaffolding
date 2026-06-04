# Proposed Intake Workflow

## Purpose

Define a revised client intake workflow that reflects the accepted research
findings from this example.

## Input Findings

- early triage and full intake should be separated
- a small shared intake vocabulary is needed
- the first contact path must work with incomplete information

## Actors

- intake coordinator
- triage reviewer
- service owner

## Workflow Stages

### 1. Received

A request enters through form, email, or phone.
The goal at this stage is only to capture enough information to begin triage.

### 2. Triage

A triage reviewer determines whether the request is urgent, routine, or
insufficiently defined.

Possible next actions:

- urgent: send directly to fast response handling
- routine: request full intake completion if needed
- insufficiently defined: request missing information before assignment

### 3. Intake Complete

The request now contains the minimum information needed for normal assignment.

### 4. Assigned

The request is routed to the service owner or team responsible for handling it.

## Workflow Rules

- urgent handling should not wait for every routine intake field
- normal assignment should not happen before minimum intake information exists
- the same stage names should be used across all channels

## Tradeoffs

- separating triage from full intake adds one explicit stage, but it makes
  urgency handling and missing-information loops easier to understand
- allowing early triage with incomplete information improves responsiveness,
  but requires clearer follow-up ownership

## Open Questions

- what minimum data is required to move from triage to intake complete
- whether phone requests need a dedicated capture script
- whether urgent handling requires a different verifier or approval rule
