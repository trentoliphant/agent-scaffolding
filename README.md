# Agent Scaffolding

## Overview

Agent Scaffolding is a repository for designing and evolving a structured approach to AI-assisted work.

This is not a collection of prompts or templates.  
It is a system for defining how agents operate, how work is structured, and how context is preserved across sessions.

The goal is to move from ad-hoc interactions toward a repeatable, inspectable, and extensible framework.

---

## What This Is

This repository defines a layered scaffolding system that may include:

- **Principles** — foundational ideas and constraints
- **Roles** — responsibility-bearing agent positions
- **Tasks** — units of work
- **Review Types** — cross-cutting evaluation criteria
- **Orchestration** — coordination and control flow
- **Session State** — current working context
- **History / Decisions** — distilled evolution of the system

The system is designed to:

- Preserve continuity across sessions
- Enable iterative refinement
- Maintain clarity between conceptual layers
- Support both human and agent understanding

---

## What This Is Not

- Not a prompt library
- Not a code framework (though it may support one)
- Not a static methodology

This repository is intended to evolve as understanding improves.

---

## Why This Exists

Typical AI workflows are:

- Stateless
- Opaque
- Difficult to reproduce
- Hard to scale beyond a single session

This project explores a different model:

> Treat context as a designed system, not an accident of conversation.

---

## Structure

A typical structure may look like:
```text
├── docs/
scaffolding/
│   ├── 00-overview.md
│   ├── 10-principles.md
│   ├── 20-roles.md
│   ├── 30-review-types.md
│   ├── 40-task-patterns.md
│   ├── 50-session-state.md
├── history/
├── decisions.md
├── AGENTS.md
├── .codex/config.toml
```


- `AGENTS.md` defines how agents should behave
- `scaffolding/` contains the current system design
- `history/` captures important decisions
- `.codex/` configures local agent execution

---

## How to Use This Repo

### With Codex (recommended)

1. Open Codex in this repository
2. Ask it to read the scaffolding documents
3. Request targeted updates
4. Review changes via diff
5. Commit

Example prompts:

- "Summarize the current scaffolding model"
- "Refine the distinction between roles and review types"
- "Add orchestration layer considerations"
- "Update session-state based on current focus"

---

### With ChatGPT

Use ChatGPT for:

- Exploration
- Concept development
- Language refinement

Then promote durable insights into the repository.

---

## Working Philosophy

- Structure before expansion
- Iteration over replacement
- Explicit over implicit
- Human-readable over model-optimized
- Durable context over transient conversation

---

## Current Status

This project is actively evolving.

Expect:
- changing structure
- refined terminology
- incomplete sections

The goal is not early stability, but increasing clarity.

---

## Contributing

At this stage, contributions are primarily conceptual:

- clarifying distinctions
- identifying missing layers
- improving structure
- refining language

---

## Future Direction

Potential future extensions include:

- structured session state (JSON)
- automated context injection
- orchestration engines
- integration with local agent systems
- reusable scaffolding templates

---

## License

See LICENSE file for details.
