# Thumbnail Media Staging and Publishing

## Goal

Provide a repeatable thumbnail execution path without depending on credit-metered third-party "upload to URL" services.

## Preferred architecture

`approved local asset -> DEDAL-owned staging upload -> short-lived HTTPS fetch URL -> Gateway media preflight -> dedicated youtube_thumbnail_set -> YouTube read-back -> staging cleanup`

The staging implementation may use Creator-controlled Cloudflare R2/Workers or another owned storage surface. The contract matters more than the vendor: bounded upload authority, short-lived fetchability, explicit content type, cleanup, and no public credential exposure.

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

- `media`: external/staged media could not be fetched or validated;
- `upload`: bytes reached the YouTube thumbnail endpoint but the vendor rejected/failed the request;
- `readback`: request may have committed but final remote state is not yet proven;
- `connector`: outer aggregation/transport failed before authoritative mutation evidence was obtained.

For outcome-unknown cases, read back before retrying.

## Security and lifecycle

- Keep staged objects private-by-default except for the bounded fetch mechanism required by the Gateway.
- Prefer short TTLs or explicit cleanup after success/final failure.
- Do not store OAuth tokens, API secrets, or channel-private metadata in object names or query strings.
- If rollback needs the old image, persist a managed baseline intentionally; otherwise staging is ephemeral.
- External credit-metered media hosts are optional fallbacks, never required infrastructure.
