#!/usr/bin/env python3
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
GATEWAY = ROOT / "skills/youtube-publishing/gateway/src/index.js"
MCP = ROOT / "skills/youtube-publishing/mcp/src/index.js"
MIGRATION = ROOT / "skills/youtube-publishing/gateway/migrations/0004_playlist_image_state.sql"
CONTRACT = ROOT / "evals/youtube-source-sync/contract-v1.json"

gateway = GATEWAY.read_text()
mcp = MCP.read_text()
contract = json.loads(CONTRACT.read_text())

required_gateway = [
    "fetchExternalMedia", "validateExternalHttpsUrl", "googleMultipartUpload",
    "googleResumableMediaUpload", "assertCaptionOwned", "playlistImagesList",
    "managedPlaylistImageReplace", "playlist_image_state",
    "playlist_image_replace_requires_managed_baseline", "playlist.image_rollback",
    "caption.insert", "caption.update", "caption.delete",
    "video.thumbnail_set", "channel.banner_set", "channel.watermark_set",
    "youtubeDataApi", "youtubeReportingApi", "youtubeAnalyticsApi",
    "resumable_init", "resumable_media", "google_location_type",
    "verifyVideoStatusEventually", "accepted_pending_readback",
]
missing = [x for x in required_gateway if x not in gateway]
if missing:
    raise SystemExit(f"gateway parity markers missing: {missing}")

for marker in ["parent_raw", "parent_resource", "metadata.google.internal", "192\\.168", "169\\.254", "too_many_media_redirects"]:
    if marker not in gateway:
        raise SystemExit(f"media/list compatibility marker missing: {marker}")

if not MIGRATION.exists() or "CREATE TABLE IF NOT EXISTS playlist_image_state" not in MIGRATION.read_text():
    raise SystemExit("playlist_image_state migration missing")

# Tool names are intentionally parsed only from the TOOLS registry, not routing strings.
block = mcp[mcp.index("const TOOLS = ["):mcp.index("\n];", mcp.index("const TOOLS = ["))]
tools = re.findall(r'tool\("(youtube_[^"]+)"', block)
if len(tools) != contract["expected_mcp_tool_count"] or len(set(tools)) != len(tools):
    raise SystemExit(f"unexpected MCP tool surface: count={len(tools)} unique={len(set(tools))}")

required_tools = {
    "youtube_thumbnail_set", "youtube_captions_list", "youtube_caption_insert",
    "youtube_caption_update", "youtube_caption_download", "youtube_caption_delete",
    "youtube_playlist_images_list", "youtube_playlist_image_set", "youtube_playlist_image_delete",
    "youtube_channel_banner_set", "youtube_watermark_set", "youtube_watermark_unset",
    "youtube_data_api", "youtube_reporting_api", "youtube_analytics_api",
}
if not required_tools.issubset(tools):
    raise SystemExit(f"missing MCP tools: {sorted(required_tools - set(tools))}")

if 'let body = input.body' not in gateway or 'parts.add("snippet")' not in gateway:
    raise SystemExit("playlist update normalization markers missing")
if 'status.privacyStatus === privacy && !status.publishAt' not in gateway:
    raise SystemExit("video privacy eventual-readback/cancel marker missing")

# Deployed debug conveniences must never enter the public source mirror.
banned_debug = [
    "test-assets/dedal-caption", "test-assets/spices-from-movies",
    "internal:test-asset", "base64ToArrayBuffer(\"/9j/",
]
for marker in banned_debug:
    if marker in gateway or marker in mcp:
        raise SystemExit(f"deployment-only debug artifact leaked into public source: {marker}")

print("youtube source sync contract: PASS")
print(f"MCP tools: {len(tools)}")
print("deployed reference: Gateway 0.7.41 / MCP 0.8.1")
