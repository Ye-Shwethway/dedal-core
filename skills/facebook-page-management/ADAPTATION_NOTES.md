# Adaptation Notes — Facebook Page Management

## Why this skill exists

The Creator explicitly requested a reusable Facebook Page management faculty after representative live Page-management work demonstrated a distinct operational boundary not owned by an existing skill. This is a CREATE decision under Skill Acquisition, not generic marketplace expansion.

## Evidence used

- Current Composio Facebook toolkit documentation reviewed 2026-09-18 for Page-only scope and the exposed Page operations surface.
- Representative live connected-Page tests on 2026-09-18 demonstrated managed-Page discovery, role/task reads, post/feed reads, text-post create/read/update/delete, scheduled text/photo creation, scheduled queue read, rescheduling, photo publishing, native file-upload video scheduling, comments/reactions reads, and Page/post insights.
- The same live tests demonstrated that Messenger tool exposure and `pages_messaging` authorization did not guarantee fresh inbound visibility or a compliant send; stale thread state plus an out-of-window provider error was therefore retained as a fail-closed lesson rather than promoted as a verified messaging capability.

## Adaptation decisions

- Keep the skill execution-surface independent. Composio is evidence and one possible transport, not the faculty itself.
- Scope mutations to Facebook Pages, not personal profiles.
- Separate `exposed`, `authorized`, `read-verified`, `write-verified`, and `degraded` capability states.
- Prefer unpublished/scheduled tests when they can validate a write path without creating public noise.
- Require exact remote read-back for consequential mutations when readable state exists.
- Treat media fetch/upload failures independently from Page authorization failures.
- Keep real Page/account identifiers, private content strategy, analytics, messages, and credentials out of public Core.

## Non-adoptions

- No provider token storage or webhook implementation is imported into Core.
- No automated Messenger-policy bypass, message-tag workaround, or retry loop is adopted.
- No Page-specific content voice, niche, identifiers, or moderation rules are embedded in the public skill.
