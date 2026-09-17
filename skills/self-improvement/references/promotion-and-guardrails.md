# Promotion and Guardrails

## Promotion ladder

Choose the narrowest durable sink:

1. No promotion — transient event.
2. Private lesson/checkpoint — Creator/project-specific procedure or incident detail.
3. Domain skill/reference — reusable behavior owned by one specialist domain.
4. Regression contract/test — mechanically checkable invariant or observed failure.
5. Core routing/protocol — cross-domain rule with repeated or high-impact evidence.

Do not promote a local workaround directly into a global rule unless the failure mechanism is genuinely cross-domain.

## Immediate repair versus durable improvement

Immediate repair optimizes time-to-recovery. Durable improvement optimizes recurrence risk. If time pressure requires a live hotfix first, verify it, mark source-sync debt, reconcile canonical source and regression coverage in the same work unit when practical, and otherwise leave an explicit checkpoint item.

## Protected evaluation

Material self-changes require evaluation that the candidate cannot silently weaken. Preserve held-out/regression coverage and reject task-specific benchmaxxing.

## External patterns

OpenClaw-style learning hooks are useful for trigger detection and durable capture, but DEDAL does not copy an autonomous file-writing loop blindly. DEDAL keeps explicit source ownership, public/private separation, independent verification, Creator/platform authority boundaries, promotion gates, and rollback evidence.

Automatic learning means automatic detection and capture, not automatic permission to rewrite every governing rule.
