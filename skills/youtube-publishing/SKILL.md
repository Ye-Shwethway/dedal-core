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
- reviewing channel/video analytics and actual YouTube search terms to improve later publishing choices;
- diagnosing a failed YouTube mutation through bounded vendor diagnostics.

## Ownership boundary

YouTube Publishing owns target-channel resolution, YouTube metadata writes, upload lifecycle, privacy/scheduling, playlist and thumbnail operations, captions, supported channel branding, managed media state, and bounded YouTube Data/Analytics/Reporting transport used by higher-level workflows. YouTube SEO owns discovery research, surface-specific packaging hypotheses, analytics diagnosis, experiments, and discovery-learning synthesis.

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

## Discoverability / SEO boundary

Use YouTube SEO for query/entity research, Search/Browse/Suggested strategy, packaging hypotheses, analytics diagnosis, experiments, and channel-learning synthesis. YouTube Publishing remains the execution/transport owner when approved metadata or channel state is actually read or changed. Do not bypass Publishing ownership, intent, mutation, or read-back gates merely because an SEO workflow produced a recommendation.

## Safety and truth gates

- Credentials, client secrets, refresh tokens, cookies, channel-private analytics, and private video metadata do not belong in this public repository.
- Upload success is not publication success. Read back exact video/channel/privacy state.
- API quotas, scopes, upload restrictions, scheduling semantics, media requirements, and analytics fields are live platform facts; re-verify when material.
- A generic API passthrough never expands authority beyond the dedicated surface.
- If prior state cannot be read or recovered, fail closed rather than guessing.

## Progressive references

- `references/direct-api-and-auth.md`
- `references/mutation-hardening-and-recovery.md`
- `channel-profiles.example.json`
- `scripts/youtube_channel_ops.py`
- `gateway/README.md`
- `references/cloudflare-gateway-architecture.md`
- `CURRENT_CHECKPOINT.md`
- `mcp/README.md`
