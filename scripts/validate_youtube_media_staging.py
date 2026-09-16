#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
worker = (ROOT / "skills/youtube-publishing/media-staging/worker.mjs").read_text(encoding="utf-8")
gateway = (ROOT / "skills/youtube-publishing/gateway/src/index.js").read_text(encoding="utf-8")
mcp = (ROOT / "skills/youtube-publishing/mcp/src/index.js").read_text(encoding="utf-8")
missing = []
for marker in ["expirationTtl", "SIGNING_SECRET", "ADMIN_TOKEN", "getWithMetadata", "no-store", "image/png", "image/jpeg", "MAX_CHUNK_BYTES", "chunkKey", "/v1/stage/chunk", "/v1/stage/finalize"]:
    if marker not in worker: missing.append("worker:" + marker)
for marker in ['path === "/v1/media/stage"', "mediaUnstageMatch", "MEDIA_STAGING_URL", "MEDIA_STAGING_TOKEN"]:
    if marker not in gateway: missing.append("gateway:" + marker)
for marker in ["youtube_media_stage", "youtube_media_unstage"]:
    if marker not in mcp: missing.append("mcp:" + marker)
if missing: raise SystemExit("missing native media staging markers: " + ", ".join(missing))
for forbidden in ["workers.dev", "MEDIA_STAGING_TOKEN=", "SIGNING_SECRET=", "ADMIN_TOKEN="]:
    if forbidden in worker or forbidden in gateway or forbidden in mcp: raise SystemExit("deployment-private identifier leaked into public source")
print("youtube media staging contract: PASS")
