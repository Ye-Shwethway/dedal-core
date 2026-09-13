---
name: automations
description: Design and manage reminders, recurring jobs, scheduled summaries, and condition/event watches with explicit trigger, cadence, action, and notification semantics.
---

# Automations

Use automations when work must happen later, repeatedly, or only when a future condition/event occurs.

## Design

Define:
- trigger: time, recurrence, event, or condition;
- cadence: no more frequent than the available platform supports;
- action: one clear iteration of work;
- notification rule: especially for condition watches, notify only when the condition is met;
- source/tool dependencies.

## Rules

- Use exact scheduling only for explicit clock times/cadences; use flexible timing for broad dayparts.
- Use condition watches for "tell me when X happens" rather than sending repeated no-change messages.
- For supported app events, prefer event triggers over wasteful polling.
- Do not pretend normal chat can run a background daemon; use the actual automation surface.
- Keep prompts self-contained enough to execute later with minimal ambiguity.

## Maintenance

When an automation becomes obsolete, noisy, duplicative, or replaced by a better event trigger, update or disable it rather than accumulating stale jobs.
