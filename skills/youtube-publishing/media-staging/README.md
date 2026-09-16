# DEDAL Media Staging Worker

Short-lived DEDAL-owned image staging for YouTube publishing operations.

## Bindings
- `MEDIA`: Workers KV namespace.
- `ADMIN_TOKEN`: secret text used only by authenticated service callers.
- `SIGNING_SECRET`: secret text used to HMAC-sign public fetch URLs.

No account IDs, namespace IDs, service URLs, or secret values belong in public Core.

## Routes
- `GET /health` — service/version check.
- `POST /v1/stage` — authenticated PNG/JPEG staging with bounded TTL.
- `GET|HEAD /m/:stage_id?exp=...&sig=...` — time-bounded signed fetch.
- `DELETE /v1/stage/:stage_id` — authenticated cleanup.

Objects are deliberately ephemeral: stage -> YouTube mutation -> authoritative read-back -> delete; TTL expiry is fallback cleanup.
