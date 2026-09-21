---
name: youtube-publishing
description: Prepare, upload, organize, schedule, brand, caption, and learn from YouTube publishing workflows across multiple Creator-owned channels using the dedicated DEDAL YouTube MCP/Gateway or another verified execution surface.
status: active
---

# YouTube Publishing

Own the channel-operations layer after a media artifact is ready for distribution. The production Gateway, isolated uploader runner, and dedicated MCP control surface have passed representative live gates. Media-replacement operations use managed-state and fail-closed rules where vendor read/update semantics are incomplete.

## Use when

- uploading an approved video or Short to a Creator-owned YouTube channel;
- selecting the correct channel among multiple authorized channel profiles;
- preparing or changing title, description, tags, category, thumbnail, captions, playlist membership/image, privacy, scheduling, or supported channel branding;
- performing bounded YouTube Data/Analytics API operations;
- reading and replying to viewer comments, or performing authorized comment moderation;
- reviewing channel/video analytics and actual YouTube search terms to improve later publishing choices;
- diagnosing a failed YouTube mutation through bounded vendor diagnostics.

## Ownership boundary

YouTube Publishing owns target-channel resolution, YouTube metadata writes, upload lifecycle, privacy/scheduling, playlist and thumbnail operations, captions, supported channel branding, viewer-comment engagement/moderation, managed media state, and bounded YouTube Data/Analytics/Reporting transport used by higher-level workflows. YouTube SEO owns discovery research, surface-specific packaging hypotheses, analytics diagnosis, experiments, and discovery-learning synthesis.

It does **not** replace:
- Video Production for edit quality, codecs, burned-in captions, or the final media master;
- Writing/Editorial for substantial copywriting;
- Research for external factual claims or current platform-policy verification;
- Visual Direction for custom thumbnail/banner image generation or editing;
- Security Engineering for credential-store architecture or threat modeling;
- the YouTube API, MCP, Gateway, browser, runner, or other execution surface.

## Default workflow

1. **Resolve exact ownership.** Select an explicit verified profile and reassert the authenticated YouTube channel before mutation.
2. **Prefer the dedicated typed tool.** Use the narrow MCP/Gateway operation that expresses the intended YouTube action. Use a generic API bridge only for a missing read surface or bounded diagnostics, never as the normal mutation path when a dedicated tool exists.
3. **Capture current state.** Read back the target when the API exposes it. For destructive replacement, preserve a recoverable DEDAL-managed baseline before deleting or overwriting.
4. **Require explicit intent.** Consequential writes require `explicit_action_intent`; deletes/unsets require `explicit_destructive_intent`; public/unlisted/scheduled publication keeps its dedicated visibility/publication intent gate.
5. **Mutate once, boundedly.** During diagnosis, make one bounded mutation attempt, inspect stage-aware audit evidence, patch minimally, then retry at most once when the evidence supports it.
6. **Verify remote truth.** Read back the mutated resource whenever the provider exposes readable state. An accepted request alone is not success.
7. **Recover safely.** For replace-style media, restore the prior DEDAL-managed source if the replacement insert/apply fails and rollback is possible.
8. **Checkpoint durable lessons.** Record vendor quirks, managed-state requirements, and unresolved readback gaps without committing secrets/private tokens.


## Upload orchestration

The normal upload surface is `youtube_upload_submit`. It creates an idempotent private-first job and returns immediately; a persistent isolated runner on Creator-controlled infrastructure discovers queued work through an authenticated outbound poll and executes it automatically. Routine uploads must not require a per-job GitHub Actions dispatch. GitHub Actions is reserved for runner deployment, validation, diagnostics, and manual recovery.

Treat upload evidence as a state machine rather than a single success bit: request accepted -> queued -> source prepared -> uploading -> verifying -> ready_private/verified_remote. Preserve the original job/idempotency key across recovery; do not create a replacement job merely because orchestration or verification is delayed. `youtube_upload_create` remains a compatibility/low-level alias.

Verification is bounded and eventual-consistency-aware. Retry authoritative video read-back briefly before declaring a remote mismatch. Playlist insertion is idempotent; after a successful insert, a temporarily empty playlist read-back is recorded as `inserted_pending_readback` rather than converting a successful video upload into a failed upload. Reconcile through authoritative read-back before any retry.

## Thumbnail execution pipeline

Publishing receives an approved thumbnail asset/brief from the composed SEO + Visual Direction workflow; it does not invent the visual strategy at mutation time. The execution path is:

`approved asset -> DEDAL-controlled ephemeral staging -> Gateway-fetch preflight -> dedicated thumbnail mutation -> stage-aware diagnostics -> authoritative read-back -> staging cleanup -> package-event record`

Prefer Creator-controlled staging. The current native path is a dedicated Cloudflare Worker backed by Workers KV, exposed to the MCP only through authenticated Gateway stage/unstage routes. R2 may replace KV later without changing the contract. Credit-metered third-party upload hosts remain fallback-only. Third-party "upload to URL" services are fallback-only, not a Core dependency. A URL is valid only when the Gateway can actually fetch and validate it; browser accessibility alone is insufficient. See `references/thumbnail-media-staging.md`.


## Managed replacement rules

- Native vendor `update` semantics are not assumed reliable merely because an endpoint exists.
- Playlist hero-image replacement is `read existing -> require managed baseline -> delete -> insert -> read back -> persist managed state`; if insert fails, attempt rollback from the previous managed source.
- An existing unmanaged playlist image must fail closed rather than be destroyed to satisfy a replacement request.
- Banner restoration requires a recoverable/full-resolution source. A display-oriented `bannerExternalUrl` is not a sufficient rollback artifact.
- When an API supports mutation but cannot reliably reveal prior state, treat that state as unmanaged and fail closed unless the Creator explicitly authorizes destructive handling.
- Watermark unset/replacement is therefore not considered fully live-gated until DEDAL has managed-state evidence or explicit authority over an unmanaged watermark.

## Mutation evidence pattern

For hard mutation failures use:

`dedicated MCP call -> bounded Gateway route -> stage-aware D1 mutation audit -> exact vendor error extraction -> minimal patch -> one bounded retry -> read-back verification -> checkpoint`

Audits may retain action/outcome, resource identifiers, stage, bounded vendor status/reason/message/location metadata, and resumable sub-stage diagnostics. They must not retain OAuth tokens, bearer secrets, cookies, raw credential material, or unbounded sensitive payloads.

## Live-gated operation families

Representative live evidence now covers:
- exact-channel ownership and fail-closed mismatch protection;
- resumable private upload with interruption/resume and no duplicate video;
- playlist membership;
- thumbnail upload;
- caption insert/list/download/update/delete with original state restored;
- playlist-image first insert and managed replacement with readback;
- valid channel-banner upload/apply/readback and restoration from a full-resolution source.

Watermark set/unset tools are exposed but the lifecycle remains **not fully live-gated** because YouTube does not provide a reliable current-watermark read/list baseline.


## Viewer-comment engagement triage

Classify the interaction before replying or moderating. Use the smallest sufficient action and preserve the channel voice without turning ordinary disagreement into conflict.

- **Positive / friendly / playful:** a concise friendly acknowledgement or agreement may be posted autonomously when the channel voice and context are clear. Do not over-explain a lightweight comment.
- **Neutral factual question:** answer autonomously only when the factual basis is sufficiently verified and the response does not require personal, medical, legal, or other sensitive speculation. Route material external-fact verification through Research when needed.
- **Sensitive / controversial / adversarial:** use a neutral factual tone, acknowledge reasonable uncertainty, avoid defensive advocacy, and distinguish documented statements from inference. If the reply could materially escalate, endorse a contested claim, speculate about a person, or create meaningful reputational/legal/policy risk, obtain Creator approval before posting.
- **Abuse / spam / moderation:** disagreement alone is not abuse. Deletion, rejection, author bans, or other destructive moderation are separate consequential actions and require explicit authority.

For public figures, do not infer health, drug use, private conduct, or other sensitive facts from appearance or rumor. It is acceptable to report a documented public statement with attribution and limits. When a reply or edit is written through the API, read it back when the provider exposes the resulting comment state. See `references/comment-engagement.md`.

## Discoverability / SEO boundary

Use YouTube SEO for query/entity research, Search/Browse/Suggested strategy, packaging hypotheses, analytics diagnosis, experiments, and channel-learning synthesis. YouTube Publishing remains the execution/transport owner when approved metadata or channel state is actually read or changed. Do not bypass Publishing ownership, intent, mutation, or read-back gates merely because an SEO workflow produced a recommendation.

## Safety and truth gates

- Credentials, client secrets, refresh tokens, cookies, channel-private analytics, and private video metadata do not belong in this public repository.
- Upload success is not publication success. Read back exact video/channel/privacy state.
- API quotas, scopes, upload restrictions, scheduling semantics, media requirements, and analytics fields are live platform facts; re-verify when material.
- A generic API passthrough never expands authority beyond the dedicated surface.
- If prior state cannot be read or recovered, fail closed rather than guessing.

### Copyright/enforcement outcome handling

Publishing does not decide legal clearance and does not ask Video Production to disguise copyrighted material from Content ID. For third-party media, distinguish actual platform outcomes: `claim`, `block`, `takedown/strike`, and separate reused-content/monetization-policy issues. A claim that leaves the video available is not equivalent to a strike; a non-monetized channel is still subject to enforcement.

After upload, capture the actual available enforcement state when surfaced by YouTube and return it to the private operational learning loop. Treat blocks, takedowns/strikes, or repeated aggressive enforcement as stronger future risk evidence than claim-only history. Do not automatically dispute claims or takedowns; any dispute is a separate consequential action requiring explicit Creator intent and an appropriate factual/legal basis.

## Progressive references

- `references/direct-api-and-auth.md`
- `references/mutation-hardening-and-recovery.md`
- `references/thumbnail-media-staging.md`
- `references/reach-reporting.md`
- `references/comment-engagement.md`
- `channel-profiles.example.json`
- `scripts/youtube_channel_ops.py`
- `gateway/README.md`
- `references/cloudflare-gateway-architecture.md`
- `CURRENT_CHECKPOINT.md`
- `mcp/README.md`
## Reach-report consumption

For scheduled Reach reports, follow `references/reach-reporting.md`. The validated `channel_reach_basic_a1` schema exposes `video_thumbnail_impressions` and `video_thumbnail_impressions_ctr` keyed by `date`, `channel_id`, and `video_id`. Download payloads only through the bounded Reporting bridge.

Any user-facing report MUST enrich video IDs with live-resolved video titles whenever available: show the video title as the primary label, retain the video ID for traceability, and write `title unavailable` if lookup fails. Never make the Creator identify a row from an opaque video ID when the title can be resolved. CTR `0` is not equivalent to zero video views. Respect Reporting lag and measurement-window availability states; later historical files may backfill a matching window but must not be presented as if they were available earlier.

## Video rating interaction

YouTube exposes account-level video rating operations even though comment-like writes are not available through the Data API. Until dedicated production-safe aliases are live, route rating requests through the allowlisted Data API bridge only:

- read: `videos.getRating` with the requested video id;
- write: `videos.rate` with exactly `like`, `dislike`, or `none`;
- require explicit user intent before any rating write;
- treat `none` as clearing the connected identity's current like/dislike;
- do not apply the owned-video mutation gate, because rating is an authenticated viewer/account interaction rather than video metadata ownership mutation.

Do not claim comment-like support; YouTube does not expose a comment-like write method.

## Post-publish Drive archive lifecycle

For Creator workflows that use Google Drive staging, publishing owns the archive transition after remote verification:

`Edited Videos -> verified YouTube upload/publication state -> Uploaded YT Videos`

- Treat `Edited Videos` as the pre-publication/ready master queue and `Uploaded YT Videos` as the archive of masters whose intended YouTube state has been verified.
- Never archive on request acceptance alone. First read back enough YouTube state to establish the intended video identity, channel, and visibility/publication outcome.
- After successful verification, move the exact Drive master from `Edited Videos` to `Uploaded YT Videos` using a true parent change when supported.
- If upload verification fails, a duplicate is suspected, a block/claim/takedown state requires review, or publication is otherwise unresolved, leave the master in `Edited Videos` and surface the blocker.
- Read back Drive placement after the move. The destination must contain the exact file and the source folder must no longer retain it when the intended operation is a true move.
- Folder/file IDs are private operational state and must not be committed to public Core.

### Rolling Drive retention

Treat both `Edited Videos` and `Uploaded YT Videos` as rolling working storage, not permanent archives. Default retention is the newest **3 usable videos per folder**. When a newly verified video would make a folder exceed that limit, evaluate the oldest eligible item and delete it only after the relevant state is resolved and read back.

- `Uploaded YT Videos`: keep the newest 3 verified published masters. An older master becomes cleanup-eligible only after the intended YouTube upload/publication state is verified and there is no active block, claim, takedown/strike review, re-upload need, or other recovery requirement.
- `Edited Videos`: keep the newest 3 active/recent outputs. For multiple revisions of the same video, prefer the latest approved/current master and allow superseded drafts to become cleanup-eligible earlier than unrelated current work.
- Retention count alone never overrides an unresolved publishing or recovery state. Pending uploads, failed verification, duplicate investigation, enforcement review, or any explicit Creator hold must be preserved even when the nominal limit is exceeded.
- Run retention cleanup after a successful publish/archive transition or other bounded folder-maintenance event; do not rely on manual periodic cleanup as the only control.
- Destructive Drive cleanup requires exact file/folder resolution before deletion and post-delete read-back. Never infer the target from a fuzzy title match when multiple candidates exist.

The default rolling window is **3**. A smaller or larger window requires explicit Creator intent for that workflow; do not silently change the durable default.
