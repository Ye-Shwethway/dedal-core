---
name: interface-design
description: Design, redesign, audit, and refine user-facing software interfaces with brief-aware visual direction, incumbent-state respect, accessibility, responsiveness, and bounded visual verification. Use for websites, app UI, dashboards, product surfaces, and frontend UX; not backend-only work.
---

# Interface Design

Treat interface work as both product design and engineering. The goal is not a fashionable default; it is a coherent surface that fits the user, product, task, and existing system.

## Start from evidence

Before changing a UI, inspect the brief and the incumbent visual truth: current screens, components, tokens, assets, copy, platform conventions, and constraints. Do not infer greenfield merely because a formal design document is missing.

State a concise **design read** when direction is materially ambiguous or useful: surface type, audience, task, intended character, and major constraints. Ask only when unresolved design direction would materially change the result.

## Choose the surface mode

Use the dominant user job to calibrate design decisions:

- **Persuade** — marketing, landing, pricing: attention, trust, comprehension, action.
- **Operate** — apps, dashboards, settings, tools: scanability, task completion, consistency, states.
- **Read** — docs, articles, help: hierarchy, comprehension, navigation, reading comfort.
- **Experience** — portfolios, galleries, showcases: the content/artifact leads; interface recedes or supports immersion.

A product can contain several modes. Classify the surface, not the company.

## Direction rules

- **The brief wins.** Explicit brand, audience, accessibility, platform, and product constraints outrank generic taste.
- **Refinement preserves; redesign may replace.** A refinement protects incumbent identity and behavior outside scope. A redesign may establish a new visual world while preserving product truth, function, content requirements, and platform affordances.
- **Use real systems honestly.** If an established design system is appropriate, use its actual components/tokens when available rather than imitating it loosely. Do not present aesthetic inspiration as an official system.
- **Avoid template autopilot.** Repeated AI defaults are not banned aesthetics; they are weak defaults. Use them only when the brief actually supports them.
- **Keep one coherent visual language.** Typography, spacing, iconography, color, motion, density, and component behavior should reinforce the same direction.

## Workflow

1. **Inspect** — current UI, product context, technical stack, constraints, reference assets, and user goal.
2. **Frame** — identify the surface mode and design direction; preserve explicit user choices.
3. **Shape** — establish hierarchy, layout, content flow, states, responsiveness, accessibility, and interaction behavior before decorative polish.
4. **Implement** — follow the existing stack and design system unless the task explicitly changes them. Verify dependencies before assuming a library exists.
5. **Review visually** — inspect the rendered result on the relevant device classes when tools permit; include error/empty/loading/focus/hover states when material.
6. **Fix materially** — batch the important defects instead of entering an open-ended polish loop.
7. **Confirm** — one focused re-check is normally enough unless new defects or explicit Creator feedback justify another pass.
8. **Persist** — when a durable design system or product direction emerged, propose recording it in the owning project rather than relying on memory.

## Progressive references

- `references/brief-and-direction.md` — brief inference, surface modes, visual direction, and system choice.
- `references/redesign-and-audit.md` — preservation vs redesign, incumbent truth, audit-first workflow.
- `references/quality-floor.md` — hierarchy, typography, layout, states, accessibility, responsiveness, and anti-template checks.
- `references/visual-verification.md` — bounded visual QA and evidence-backed completion.

## Boundary

This skill governs interface design quality. Use Software Development for implementation lifecycle/debugging/testing and Files/Slides/Image tools for artifact-specific mechanics. Do not override higher-priority platform instructions or invent visual verification that was not actually performed.
