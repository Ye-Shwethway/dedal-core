---
name: facebook-page-management
description: Read, publish, schedule, edit, moderate, analyze, and manage authorized Facebook Pages through a verified execution surface while preserving Page identity, explicit mutation intent, read-back verification, and public/private separation.
status: active
---

# Facebook Page Management

Own authenticated Facebook **Page** operations after content, media, or engagement intent is clear. This skill governs Page identity resolution, Page content lifecycle, scheduling, media publishing, engagement/moderation, Page analytics, Messenger operations when live capability is verified, and safe use of a connected Facebook execution surface.

## Use when

- listing or selecting Facebook Pages the authenticated user is authorized to manage;
- reading Page details, posts, photos, videos, comments, reactions, roles/tasks, scheduled content, or insights;
- creating, scheduling, updating, rescheduling, publishing, or deleting Page posts;
- publishing Page photo/video content or managing albums when the execution surface supports it;
- replying to or moderating Page comments;
- reading or replying to Page Messenger conversations when current platform eligibility and conversation freshness are verified;
- diagnosing a Facebook Page mutation through bounded provider evidence.

## Ownership boundary

Facebook Page Management owns authenticated Facebook Page identity, Page content/engagement mutations, Page scheduling, Page analytics transport, and Page messaging operations. It does **not** own:

- personal Facebook profile posting or personal-profile automation;
- substantial copywriting or editorial voice, which belongs to Writing/Editorial;
- image generation/editing, which belongs to Visual Direction;
- video editing/master creation, which belongs to Video Production;
- external factual research or current Meta policy interpretation, which belongs to Research;
- credential-store/security architecture, which belongs to Security Engineering;
- automation cadence/monitoring policy, which belongs to Automations;
- the provider SDK, Graph API, Composio, MCP, browser, or other execution surface itself.

## Core workflow

1. **Resolve the exact Page.** Enumerate or verify the intended managed Page and its current tasks/roles before consequential writes. Never substitute a personal profile ID for a Page ID.
2. **Verify the execution surface.** Confirm the connected Facebook surface is active and exposes the required operation. Tool exposure alone is not proof that a live capability currently works.
3. **Capture current state.** Read the target post/comment/schedule/settings state when available. Preserve exact composite identifiers returned by Facebook for later read/update/delete operations.
4. **Classify the mutation.** Distinguish read-only inspection, reversible/private draft work, public publication, engagement with a real user, access/role changes, and irreversible deletion.
5. **Require explicit intent for consequential writes.** Public publishing, replies/messages to real users, role/task changes, settings changes, reactions, and destructive actions require clear user intent. Do not infer approval from a prior read-only request.
6. **Prefer low-impact validation.** When testing a new write path, prefer unpublished or scheduled content when supported, verify it, then clean it up. Do not create public test content merely to prove tool availability when a private/scheduled path can establish the same capability.
7. **Mutate once, boundedly.** Perform the narrow intended action. On failure, inspect the exact provider/tool error before retrying; do not loop mutations blindly.
8. **Verify remote truth.** Read back the resulting post, queue, Page state, or engagement object whenever the provider exposes readable state. A successful request alone is not proof of the intended remote outcome.
9. **Clean up tests.** Delete or revert test drafts/scheduled objects after verification when cleanup was part of the test plan and the user authorized the test lifecycle.
10. **Record durable quirks without private identifiers.** General platform behavior may enter public Core; Page IDs, account aliases, private content strategy, credentials, audience data, and Creator-specific operating state belong in private state.

## Content lifecycle rules

- Text/link posts: support create, read, update, schedule/reschedule, publish-now where available, and delete through the narrowest verified operation.
- Photo/video posts: validate the media transport independently from Page authorization. A media-fetch failure is not automatically a Page-permission failure.
- Prefer a managed file-upload/staging path when remote public URLs are rejected, unstable, redirect-heavy, expiring, or blocked from Facebook fetchers.
- Multi-photo feed posts, album creation, or other operations that are inherently public must not be used as silent capability tests. Require explicit approval for the visible artifact.
- Scheduling uses provider-accepted future time semantics. Verify the queued object and stored publish time instead of trusting local timestamp arithmetic alone.
- Preserve the full Page-scoped/composite post identifier returned or recovered from Page queues; do not truncate to a media ID when later operations require the post ID.

## Engagement and moderation

- Read comments/reactions before replying, editing, hiding, deleting, liking, or unliking.
- A public comment/reply is an external communication and requires explicit user intent.
- Destructive moderation is irreversible or user-visible; confirm the exact target and avoid bulk actions without bounded selection and evidence.
- Role/task assignment/removal and Page settings changes are high-impact administrative mutations. Re-read current roles/tasks and require explicit intent for the exact change.

## Messenger boundary

Messenger is a conditional Page capability, not a guaranteed consequence of Page access.

Before replying:

1. verify the Page has current messaging authority;
2. read the current conversation through the same execution surface;
3. confirm the latest inbound user message is actually visible and recent enough for the requested messaging mode;
4. derive the recipient from conversation participants/message metadata, never from a guessed username;
5. send only after explicit user intent;
6. read back or otherwise verify delivery state when the surface exposes it.

If the tool returns stale conversation state, an out-of-window policy error, missing fresh inbound messages, or an unclear Page-token/app-subscription state, **fail closed**. Do not bypass platform messaging policy with tags, alternate APIs, or repeated retries. Treat Messenger as unverified for that connection until current inbound visibility and a compliant send are demonstrated.

## Truth and safety gates

- Facebook Personal profiles are outside this skill's mutation scope unless a future execution surface explicitly and lawfully supports them and the skill is re-audited.
- OAuth scopes, Page tasks, API versions, messaging windows, available metrics, media constraints, and product surfaces are live platform facts. Verify them when material.
- Never expose or persist Page/user access tokens, cookies, bearer secrets, raw auth responses, or private audience/message content in public Core.
- Do not treat a Page role/task as proof that every Graph/Messenger endpoint is operational.
- Do not treat a connector's supported-tool catalog as a live gate. Separate `exposed`, `authorized`, `live-read-verified`, and `live-write-verified` capability states.
- If read-back contradicts the mutation response, report the remote state as authoritative and stop before compounding the change.

## Execution-surface preference

Prefer, in order:

1. a dedicated typed Facebook/Page operation with exact schema and active connection;
2. a bounded provider API bridge for missing read-only diagnostics;
3. browser/computer interaction only when API/tool coverage is insufficient and the user has authorized the visible workflow.

Generic API passthrough does not expand authority beyond the connected Page or bypass provider policy.

## Progressive references

- `references/capability-and-verification.md`
- `references/media-scheduling-and-messaging.md`
- `Adaptation_NOTES.md`
