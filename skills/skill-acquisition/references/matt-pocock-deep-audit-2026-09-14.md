# Matt Pocock Skills — DEDAL Deep Audit

Date: 2026-09-14
Source: `mattpocock/skills`
Inspected source commit/tree: `3cca18b368ae95cdbdebbff572ccafa662551015`
License: MIT

## Why this corpus matters

This repository is useful less as a collection of copyable prompts than as a worked example of a composable skill system: narrow triggers, shared vocabulary, progressive disclosure, explicit phase boundaries, durable project context, and workflows that hand work from decision-making to implementation and review.

DEDAL policy remains: **reuse ideas; do not inherit trust blindly.** No upstream scripts or runtime-specific orchestration were installed or executed during this audit.

## Classification

### Adapt as standalone DEDAL skill

- `grilling` / `grill-me` -> `decision-design`
  - Keep: dependency-aware decision tree, ask only currently-unblocked questions, assistant retrieves facts while the Creator owns decisions, explicit shared-understanding gate.
  - Change: no assumption of a particular Skill tool/subagent runtime; do not force exhaustive questioning on small tasks; respect DEDAL's bias toward acting when enough is known.

### Merge into Software Development references

- `diagnosing-bugs` -> `debugging-loop.md`
  - Keep: build a red-capable feedback loop first, reproduce/minimize, ranked falsifiable hypotheses, targeted instrumentation, regression lock, cleanup.
  - Change: reproduction-first is strong guidance, not a reason to refuse all progress when the environment cannot reproduce; use least-destructive evidence gathering and state uncertainty.

- `tdd` -> `testing-and-seams.md`
  - Keep: behavior through public seams, independent expected values, vertical slices, red-before-green when TDD is chosen.
  - Change: TDD is not mandatory for every task; do not require user confirmation of every seam when repository conventions already establish it.

- `code-review` -> `review-two-axis.md`
  - Keep: pin a fixed comparison point; review Standards and Spec/Intent separately so one cannot mask the other; exact diff first.
  - Change: independent workers are optional; two conceptual passes are required, not parallel subagents.

- `codebase-design`, `domain-modeling`, architecture-improvement patterns -> `architecture-and-domain.md`
  - Keep: deep modules, small interfaces, seams, leverage/locality, domain vocabulary, ADR conflict visibility, lazy documentation when a real decision crystallizes.
  - Change: terminology is guidance rather than a universal ban on words like API/service; project-local vocabulary wins.

- `to-spec`, `to-tickets`, `implement`, `handoff` -> `multi-session-delivery.md`
  - Keep: decisions before build, durable spec only when work outlives a session, vertical-slice tickets, one coherent slice per implementation context, compact handoff that references rather than duplicates existing truth.
  - Change: tracker use is optional; repository continuity docs/issues/specs may all be valid persistence surfaces.

### Merge as general principles, not new skills

- `ask-matt` router -> reinforces DEDAL `MASTER_INDEX` smallest-matching-skill routing.
- setup/config patterns -> reinforce reading project-local context and ADRs before generic rules.
- explicit user-only invocation on disruptive workflows -> reinforces avoiding surprise high-ceremony behavior.

### Reject / do not inherit

- assumptions that a particular Skill tool, Claude plugin, native subagent primitive, or issue-tracker configuration exists;
- mandatory parallel workers where the runtime does not expose them;
- process gates that would turn trivial changes into ceremony;
- copying upstream prose wholesale when a smaller DEDAL-native contract preserves the idea;
- treating upstream popularity as correctness.

## High-value design lessons

1. **Skill composition beats giant prompts.** Narrow skills can hand off durable artifacts and share vocabulary without loading everything at once.
2. **A workflow needs explicit phase boundaries.** Deciding, recording, slicing, implementing, and reviewing are different cognitive jobs.
3. **Feedback-loop quality dominates debugging quality.** A fast red-capable signal sharply reduces speculative diagnosis.
4. **Review needs independent axes.** Conformance to standards and conformance to intended behavior are different questions.
5. **Project vocabulary is operational state.** Context/glossary and ADRs reduce semantic drift across sessions.
6. **Continuity artifacts should reference truth, not duplicate it.** Handoffs should point to commits/specs/issues/ADRs where possible.
7. **User-invoked heavy workflows are healthy.** High-ceremony or disruptive flows should not trigger from weak relevance.

## DEDAL integration decision

Promote the adapted patterns into DEDAL Core v0.6.0 as focused references under `software-development`, plus one generic `decision-design` skill. Preserve this audit as provenance and re-check upstream only when materially revising these adaptations.
