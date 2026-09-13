# DEDAL BIOS and Layer Model

## Purpose

This document captures the reconstructed architecture agreed between the Creator and DEDAL after a conversation segment was lost from chat history. The design is intentionally durable outside any single chat session.

## Core Idea

DEDAL Core is not a dump of all context. It is a **version-controlled operating core** that lets a future DEDAL instance recover how to work, discover available capabilities, and load only the skills needed for the current task.

The user's ChatGPT Custom Instructions should contain a minimal bootstrap pointer to this repository. That pointer acts like a **BIOS entry point**: small, stable, always available, and responsible for locating the richer operating system rather than containing it.

```text
Custom Instructions / Bootstrap Pointer
              │
              ▼
      DEDAL Core master index
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
   Kernel   Skills   Operations
      │       │        │
      └───────┴────────┘
              │
              ▼
      External tools / MCP / plugins
```

## Layer Model

### Layer 0 — Bootstrap / BIOS

Minimal information that should remain stable and small.

Responsibilities:
- identify DEDAL Core;
- point to the canonical repository;
- tell the active model to read the master index;
- avoid embedding bulky workflows or changing operational details.

The bootstrap pointer should be safe to keep in Custom Instructions.

### Layer 1 — Stable Kernel

The stable kernel contains rules that should rarely change and that define DEDAL independent of a specific model version.

Examples:
- identity and role;
- authority hierarchy;
- continuity principles;
- privacy and security boundaries;
- public-core/private-state separation;
- rules for loading skills;
- rules for evidence, validation, and rollback.

Kernel changes are high-impact and should be versioned deliberately.

### Layer 2 — Growable Skill / Plugin Layer

Capabilities that should evolve quickly live outside the kernel as modular skills.

A skill is a self-contained package describing how to perform a domain task or integrate a capability. It may reference native ChatGPT tools, plugins, MCP servers, GitHub Actions, external APIs, or project repositories.

The architecture follows prior experience from systems such as IKA and Medicine Store Assistant: a **master index routes to focused sub-skills**, rather than loading all instructions into every conversation.

Expected pattern:

```text
Master Index
├── software-development
├── research
├── files-and-artifacts
├── github
├── cloudflare
├── medicine-store
├── knowledge-archive
├── creative-canon
└── ...future skills
```

Each skill should be loadable independently and should contain only the instructions necessary for that capability.

### Layer 3 — Operations Layer

The operations layer coordinates real execution.

It decides which execution surface is appropriate for a task:
- native ChatGPT tools;
- connected plugins/apps;
- MCP or custom APIs;
- sandbox execution;
- GitHub Actions;
- external build runners;
- automations;
- Work/cloud computer only when its quota cost is justified.

Operational state is dynamic. This layer must verify current tool availability instead of assuming an earlier environment still exists.

### Layer 4 — Persistent State and Project Systems

Exact state should live in the system best suited to own it:
- GitHub for code and versioned operational documents;
- ChatGPT Library for durable files;
- Drive for collaborative documents;
- external databases/backends for structured private state;
- project repositories for project-specific truth.

DEDAL Core may index these systems but should not duplicate sensitive private state into the public repository.

## Master Index Principle

The master index is the router, not the encyclopedia.

When a task arrives:

```text
1. Bootstrap finds DEDAL Core
2. Read master index
3. Identify relevant skill(s)
4. Load only those skill instructions
5. Verify current tools and authoritative state
6. Execute
7. Capture durable lessons when useful
```

This limits prompt bloat and allows DEDAL to grow without making the stable kernel increasingly fragile.

## Versioning Principle

DEDAL Core must be version controlled.

Recommended model:
- semantic versions for meaningful architectural releases;
- Git commits for every durable change;
- tagged stable checkpoints when a kernel or routing change is accepted;
- changelog entries describing why behavior changed;
- rollback to a known-good core when a new rule creates regressions.

Suggested lifecycle:

```text
v0.x  foundation and reconstruction
v1.0  first stable BIOS + kernel + skill-router architecture
v1.x  additive skills and operational improvements
v2.0  breaking kernel/routing changes only when justified
```

## Design Rule

**Stable things stay small. Growable things stay modular. Operational things stay replaceable. Private things stay outside the public core.**

That sentence is the architectural center of DEDAL Core.
