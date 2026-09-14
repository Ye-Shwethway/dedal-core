# Direct YouTube API and Auth Reference

## Current platform facts verified 2026-09-15

Official YouTube/Google documentation currently establishes:

- `videos.insert` supports media upload with a maximum file size of 256 GB and accepts `video/*` or `application/octet-stream`.
- The current granular quota model gives `videos.insert` its own upload bucket; the documented default is 100 upload calls/day. `search.list` also has its own default 100 calls/day, while other Data API methods share a documented default 10,000 units/day.
- API projects created after 2020-07-28 that have not completed YouTube API compliance review are restricted to private viewing mode for uploads performed through `videos.insert`.
- YouTube Analytics can report `YT_SEARCH` traffic with `insightTrafficSourceDetail`, exposing search terms that actually generated traffic for authorized channel content.
- OAuth out-of-band/manual copy-paste authorization is deprecated. Desktop installed applications should use a loopback listener such as `127.0.0.1`; Google does not recommend that loopback pattern for Android/iOS native client types.

Re-verify these facts before relying on them in long-lived automation.

## Architecture

Use three layers:

1. **Public Core contract** — routing, guards, schemas, and example configuration only.
2. **Private channel profile state** — profile aliases, channel IDs, defaults, token paths, and optional local preferences.
3. **Credential/token store** — OAuth client secret and refresh/access tokens outside the repository.

A ChatGPT login, Gmail identity, Google OAuth identity, and YouTube channel identity are separate concepts. Never assume they are the same.

## Channel identity contract

Each profile should have:

- `alias`: stable Creator-facing name;
- `channel_id`: expected YouTube channel ID;
- `token_file`: private per-profile OAuth token path;
- `client_secrets_file`: private OAuth client configuration path;
- defaults such as privacy, category, playlist, and audience flag.

After OAuth, call `channels.list(mine=true, part=id,snippet)` and compare the returned channel ID with the configured `channel_id`. Refuse mutation on mismatch.

If one Google account controls multiple channel identities/Brand Accounts, authorize the desired identity and bind the resulting verified channel ID to a distinct profile.

## Scope strategy

Request only the scopes required by the selected features.

Suggested modes:

- upload-only: `https://www.googleapis.com/auth/youtube.upload`
- channel-manage/playlist: `https://www.googleapis.com/auth/youtube`
- analytics read: `https://www.googleapis.com/auth/yt-analytics.readonly`

If a profile later requires broader scopes, re-authorize deliberately rather than silently expanding authority.

## Upload transaction

Preferred transaction:

1. validate local file and publish manifest;
2. authorize the selected profile;
3. verify authenticated channel ID;
4. construct `snippet` + `status` body;
5. call resumable `videos.insert`;
6. retain returned `video_id`;
7. read back `videos.list(part=snippet,status,processingDetails,id=...)`;
8. verify identity and requested privacy/metadata;
9. apply thumbnail/playlist/caption secondary actions;
10. verify those mutations separately.

Do not retry blindly after an ambiguous network failure. First query remote state using any retained video ID or transaction evidence to avoid duplicate uploads.

## Visibility policy

Candidate default: `private`.

Treat `unlisted`, `public`, and future `publishAt` scheduling as separate visibility mutations. A successful private upload does not imply authority to publish it.

Also distinguish platform eligibility from user intent: an unverified API project may be technically prevented from making a direct upload public even when the Creator wants public visibility.

## Analytics and self-built SEO

Useful evidence can be assembled without a paid SEO service:

- current search result titles/descriptions and topical patterns;
- Google Trends comparisons when available;
- own-channel historical performance;
- YouTube Analytics traffic-source reports;
- actual `YT_SEARCH` terms from `insightTrafficSourceDetail`;
- watch time/views by search term and by video;
- topic/title experiments across later uploads.

A DEDAL heuristic may estimate opportunity using factors such as topical fit, result saturation, recency, title-pattern redundancy, channel authority mismatch, and observed own-channel search performance. It must not be presented as YouTube's official search volume or a proprietary vidIQ score.

## Mobile note

The included Python reference client is desktop-first because Google's supported installed-app loopback flow is documented for macOS/Linux/Windows desktop apps. Termux runs on Android, so do not represent desktop loopback auth there as a formally supported Android-native flow.

A future mobile-first execution bridge can use a compliant web-server OAuth callback or a native Android identity surface, while preserving the same profile/channel-ID guard contract.
