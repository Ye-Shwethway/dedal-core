# Multi-Session Delivery

Use when a software effort is too large to fit safely in one working context.

## Separate the jobs

Do not blur these stages:

`decide -> record -> slice -> implement -> review -> checkpoint`

For small work, collapse unnecessary stages. For multi-session work, durable boundaries reduce drift.

## Record only when persistence earns its cost

A spec is useful when decisions must survive context loss or coordinate multiple slices. It should capture decisions already made, constraints, accepted behavior, testing seams, and meaningful out-of-scope choices. Do not invent missing decisions merely to fill a template.

## Slice vertically

Break large work into coherent user/behavior slices that can be implemented and verified independently. Avoid tickets that are merely horizontal layers such as 'all models', then 'all APIs', then 'all UI' when no slice demonstrates working behavior.

Each slice should name dependencies/blockers and its own acceptance/verification evidence.

## Implementation discipline

One working context should normally own one coherent slice. Read the durable plan and live repository state first; do not casually redesign accepted upstream decisions during implementation. Escalate only when implementation evidence proves the plan is inconsistent or unsafe.

## Handoff discipline

A handoff should be compact and point to authoritative artifacts rather than duplicate them. Include:
- current branch/commit and work status;
- next objective and blockers;
- relevant spec/issue/ADR/checkpoint paths;
- verification already performed and what remains;
- suggested DEDAL skills/references for the next session;
- no secrets or unnecessary private data.

DEDAL continuity docs, repository issues/specs, commits, or project-specific systems may serve as the durable surface; no single tracker is mandatory.
