# Thumbnail Media Staging and Publishing

## Goal

Provide a repeatable thumbnail execution path without depending on credit-metered third-party "upload to URL" services.

## Current native architecture

`approved local asset -> youtube_media_stage (small) OR youtube_media_stage_chunk* + youtube_media_stage_finalize (normal/large) -> DEDAL media-staging Worker -> short-lived signed HTTPS URL -> Gateway media preflight -> youtube_thumbnail_set -> YouTube read-back -> youtube_media_unstage/TTL expiry`

The current production implementation uses a dedicated Cloudflare Worker backed by Workers KV. R2 is not a runtime dependency. The public Core stores only the generic Worker source and binding contract; account identifiers, namespace identifiers, service URLs, and secrets remain deployment-private.

### Staging contract

- accepted content types: PNG and JPEG;
- bounded raw payload size;
- TTL defaults to minutes, not days;
- staged keys are random capability identifiers;
- fetch URLs are HMAC-signed and time-bounded;
- responses use `no-store` and `nosniff`;
- staging upload/delete requires an authenticated server-side token;
- successful publication should explicitly clean up when practical; TTL expiry is the fallback cleanup;
- no OAuth/channel secrets are placed in object names, media bytes, or query strings.

## Why KV now

The deployment account did not have R2 enabled when native staging was implemented. Workers KV already provided the needed short-lived bounded object lifecycle for thumbnail-sized media. If R2 is enabled later, storage may be swapped without changing the higher-level staging contract.

## Media preflight

Before mutation, verify from the same network class that will fetch the asset when practical:

- HTTPS only;
- no embedded credentials in the URL;
- bounded redirect chain;
- successful status;
- accepted image content type;
- non-empty bounded payload;
- current YouTube thumbnail dimensions/format/size constraints;
- source remains valid long enough for the mutation/read-back window.

A URL that works in a browser but fails from the Cloudflare Gateway is not a valid staging result.

## Failure stages

Thumbnail mutation diagnostics should distinguish at least:

- `stage`: DEDAL staging upload or cleanup failed;
- `media`: external/staged media could not be fetched or validated;
- `upload`: bytes reached the YouTube thumbnail endpoint but the vendor rejected/failed the request;
- `readback`: request may have committed but final remote state is not yet proven;
- `connector`: outer aggregation/transport failed before authoritative mutation evidence was obtained.

For outcome-unknown cases, read back before retrying.

## Operational rule

Use native DEDAL staging first. Credit-metered third-party upload hosts are fallback-only and should require an explicit reason, not silently become a dependency.


## MCP transport-safe chunking

The custom MCP/aggregation transport can reject large inline Base64 requests before they reach the Gateway. Assets that do not fit the single-call path must be split into bounded Base64 chunks (raw decoded chunk <= 16 KiB), uploaded with `youtube_media_stage_chunk`, finalized with `youtube_media_stage_finalize`, then published from the returned signed URL. Abandoned chunk sessions expire automatically. This keeps third-party upload hosts out of the required path.


## Stable MCP surface

Production keeps the existing 54-action MCP surface. Chunking is transported through the existing `youtube_media_stage` action using a Base64-encoded DEDAL control envelope, so no MCP re-sync or separate chunk tools are required. The Gateway recognizes only the versioned envelope marker and routes it to the owned staging Worker; ordinary image Base64 continues through the original single-call path. Recommended raw chunk size is 6 KiB to stay comfortably below connector body limits.

Chunk acknowledgements are wrapped to satisfy the stable `youtube_media_stage` output contract (`pending: true`, empty `source_url`) while carrying `upload_id` as an additional field. Only the finalize response is a publishable stage result.
