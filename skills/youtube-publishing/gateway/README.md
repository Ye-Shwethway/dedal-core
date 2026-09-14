# DEDAL YouTube Gateway

Production-minded Cloudflare control plane with a separate VPS byte-transfer runner.
Video bodies go from the runner directly to YouTube and never through the Worker.

## Deployed resources

- Worker: `dedal-youtube-gateway`
- Domain: `https://youtube.drthorne.uk`
- D1: `dedal-youtube-gateway-prod` (binding `DB`)
- API: `v1`

No KV, R2, Queue, Durable Object, Access application, Pages project, or Tunnel was
added for this slice.

## Security contract

- Pre-register alias + exact `channel_id` before OAuth.
- OAuth uses 30-minute preview-safe connect tickets, one-use state, browser-bound HttpOnly cookie,
  PKCE S256, and ten-minute expiration.
- Callback calls `channels.list(mine=true)`; mismatch stores no credential.
- Refresh tokens and resumable session URIs are AES-256-GCM ciphertext in dedicated
  D1 vault tables. The encryption key is a Worker Secret.
- Runner uses a separate bearer secret and receives no Google token.
- Every mutation rechecks the authenticated channel.
- Jobs are idempotent and private-first. Broader visibility/scheduling needs explicit
  per-job intent. Success requires remote ID/channel/title/privacy read-back.

D1 encryption is the smallest zero-subscription dynamic-token design. Compromise of
both D1 ciphertext and the Worker KEK exposes tokens; key loss makes them
unrecoverable. Rotation requires re-encryption or reauthorization. Use an external
KMS later only if the threat model justifies it.

## Manual secrets

In **Cloudflare Dashboard → Workers & Pages → dedal-youtube-gateway → Settings →
Variables and Secrets**, add each as type **Secret**:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `TOKEN_ENCRYPTION_KEY_B64` — exactly 32 random bytes, base64/base64url encoded
- `ADMIN_API_TOKEN` — independent random bearer token
- `RUNNER_API_TOKEN` — a different independent random bearer token

Do not put values in chat, GitHub, D1, screenshots, or shell history. Local generation:

```bash
openssl rand -base64 32
openssl rand -hex 32
openssl rand -hex 32
```

## First real channel

1. `GET /health` must report `configured: true`.
2. Copy the exact intended channel ID from YouTube Studio; never infer from email.
3. Pre-register it:

```bash
curl https://youtube.drthorne.uk/v1/channels \
  -H "Authorization: Bearer $ADMIN_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"alias":"archive","channel_id":"UC_REPLACE_WITH_EXACT_ID"}'
```

4. Mint a 30-minute URL:

```bash
curl -X POST https://youtube.drthorne.uk/v1/channels/archive/connect-ticket \
  -H "Authorization: Bearer $ADMIN_API_TOKEN"
```

5. Open returned `connect_url`, choose the intended YouTube identity, and consent.
6. `GET /v1/channels/archive` must show the exact ID, connected, and enabled.
7. Separately test a wrong expected ID: callback must return 409 and store no token.
8. Create one private job and run the VPS runner.
9. Accept only `verified` plus matching remote read-back.

## API

Admin bearer: `POST /v1/channels`, `GET /v1/channels`,
`GET /v1/channels/:alias`, `POST /v1/channels/:alias/connect-ticket`,
`POST /v1/upload-jobs`, `GET /v1/upload-jobs/:id`.

Browser: `GET /oauth/connect/:alias?ticket=...`,
`GET /oauth/google/callback`.

Runner bearer: `POST /v1/upload-jobs/:id/claim`,
`POST /v1/upload-jobs/:id/progress`, `POST /v1/upload-jobs/:id/complete`.
Runner calls claim with `{"inspect_only":true}` before resolving the source.

Example job:

```json
{
  "idempotency_key": "archive:sha256:...",
  "profile_alias": "archive",
  "source_type": "local_file",
  "source_locator": "/srv/videos/example.mp4",
  "source_fingerprint": "sha256:...",
  "title": "Example",
  "made_for_kids": false,
  "requested_privacy": "private"
}
```

Public/unlisted needs `explicit_visibility_intent: true`. `publish_at` also needs
`explicit_publication_intent: true` and private upload status.

## VPS runner

Requires Python 3.10+ and standard library only. Store the scoped runner token in the
service environment, then:

```bash
export DEDAL_YOUTUBE_RUNNER_TOKEN='set-privately'
python3 runner/dedal_youtube_uploader.py --job-id JOB_UUID
```

Direct URLs download resumably to the runner state directory. Local paths are read
in place. A `google_drive` source uses the Drive file ID as its locator and resolves
through the existing VPS media gateway's authenticated `rclone backend copyid`
route; no YouTube credential is placed on that host. The runner computes SHA-256
before claiming the job, and the gateway atomically locks that fingerprint before
creating a resumable session. It then queries YouTube's confirmed offset, uploads
8 MiB chunks, reports progress, and asks the gateway for remote verification.
It never auto-restarts an expired/ambiguous session because a lost final response
could otherwise silently duplicate a video.

Thumbnail, playlist, video-update, analytics, and replacement-session endpoints are
deferred until the private-upload slice is proven.
