---
name: youtube-publishing
description: Prepare, upload, organize, schedule, and learn from YouTube publishing workflows across multiple Creator-owned channels using direct APIs or another verified execution surface.
status: candidate
---

# YouTube Publishing

Own the channel-operations layer after a media artifact is ready for distribution. This candidate skill is intentionally not active in the Master Index until a real Creator-owned upload validates the workflow.

## Use when

- uploading an approved video or Short to a Creator-owned YouTube channel;
- selecting the correct channel among multiple authorized channel profiles;
- preparing title, description, tags, category, thumbnail, playlist, privacy, or publish timing;
- performing direct YouTube Data API operations;
- reviewing channel/video analytics and actual YouTube search terms to improve later publishing choices;
- researching discoverability without requiring a paid SEO service.

## Ownership boundary

YouTube Publishing owns target-channel resolution, YouTube metadata, upload lifecycle, privacy/scheduling, playlist/thumbnail operations, channel-specific defaults, post-publish analytics, and YouTube discoverability feedback.

It does **not** replace:
- Video Production for edit quality, codecs, captions burned into media, or the final media master;
- Writing/Editorial for prose quality when substantial copywriting is needed;
- Research for external factual claims or current platform-policy verification;
- Visual Direction for custom thumbnail image generation/editing;
- Security Engineering for credential-store architecture or threat modeling;
- the YouTube API, browser, plugin, local client, gateway, or other execution surface.

## Default workflow

1. **Receive a verified media handoff.** Confirm exact file identity, duration/format where material, and whether this is a master or delivery copy.
2. **Resolve the target channel.** Never infer a channel from the current ChatGPT/Gmail identity. Resolve an explicit profile and verify the authenticated YouTube channel ID before mutation.
3. **Prepare a publish manifest.** Include title, description, optional tags/category/playlist/thumbnail, made-for-kids status, privacy, and optional publish time.
4. **Apply the private-first gate.** Unless the Creator explicitly requests otherwise and the execution surface is eligible, new direct-API uploads default to `private`.
5. **Upload resumably when supported.** Preserve the returned video ID and enough local state to recover or verify after interruption.
6. **Verify remote truth.** Read back the uploaded resource and verify channel, title, privacy, processing state where available, and requested metadata before calling the operation successful.
7. **Apply secondary operations.** Set thumbnail, playlist membership, captions, or scheduling only after video identity is verified.
8. **Promote visibility deliberately.** Public/unlisted visibility or future publication is an external mutation. Require explicit Creator intent for the specific video/channel unless a later approved policy grants bounded standing authority.
9. **Learn from outcomes.** When useful, inspect YouTube Analytics traffic sources/search terms and compare them with the pre-publish hypothesis. Treat proprietary third-party SEO scores as optional supplements, not truth.

## Multi-channel rules

- A profile must bind a human-readable alias to a verified `channel_id`; account email alone is not sufficient identity.
- Keep OAuth tokens isolated per profile. Never reuse a token merely because two channels have similar names or niches.
- A single Google account may expose multiple YouTube identities/Brand Accounts; verify the returned channel ID after authorization.
- Before every upload, display or log the resolved profile alias + channel ID + requested privacy.
- If the authenticated channel ID does not equal the configured channel ID, fail closed before upload.

## Discoverability / SEO rules

DEDAL can perform useful YouTube optimization without vidIQ or another paid service by combining:
- current YouTube search-result patterns and related queries when available;
- Google Trends or other current public trend evidence when appropriate;
- the channel's own YouTube Analytics traffic-source/search-term data;
- title/description semantic clarity and audience intent;
- observed performance from prior videos in the same channel/niche.

Do not invent universal search-volume numbers. Any DEDAL competition/opportunity score must be labeled as a heuristic and explain the evidence behind it.

## Safety and truth gates

- Credentials, client secrets, refresh tokens, channel-private analytics, and private video metadata do not belong in this public repository.
- Do not claim an upload succeeded from an HTTP request alone; verify the returned video ID and remote resource state.
- Do not claim a video is public because it was uploaded successfully.
- Direct API projects created after 2020-07-28 may be restricted to private uploads until YouTube API compliance review; verify current policy before relying on public publication.
- OAuth OOB/manual-copy flows are deprecated. The reference client uses the supported desktop loopback flow; mobile-native auth requires an appropriate supported identity flow.
- API quotas, scopes, upload restrictions, scheduling semantics, and analytics fields are live platform facts; re-verify when material.

## Candidate promotion gate

Promote this skill to the active registry only after representative Creator work demonstrates at least:

1. authorization against one real Creator-owned channel;
2. channel-ID mismatch protection;
3. one resumable private upload with read-back verification;
4. at least one secondary operation (thumbnail or playlist) when relevant;
5. interruption/error behavior that does not silently duplicate or publish the wrong file;
6. a documented path for multiple channel profiles.

## Progressive references

- `references/direct-api-and-auth.md`
- `channel-profiles.example.json`
- `scripts/youtube_channel_ops.py`
- `gateway/README.md`
- `references/cloudflare-gateway-architecture.md`
- `CURRENT_CHECKPOINT.md`
