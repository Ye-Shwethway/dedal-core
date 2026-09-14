#!/usr/bin/env python3
"""Reference YouTube channel-operations client for DEDAL.

This is a local execution surface, not a credential store. Keep client secrets,
OAuth tokens, private manifests, and channel-private data outside the public repo.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
from pathlib import Path
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
MANAGE_SCOPE = "https://www.googleapis.com/auth/youtube"


def expand(path: str) -> Path:
    return Path(os.path.expanduser(path)).resolve()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json_private(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    try:
        path.chmod(0o600)
    except OSError:
        pass


def load_profile(config_path: Path, alias: str) -> dict[str, Any]:
    cfg = load_json(config_path)
    profiles = cfg.get("profiles", {})
    if alias not in profiles:
        raise SystemExit(f"Unknown profile: {alias}")
    profile = profiles[alias]
    required = ["channel_id", "client_secrets_file", "token_file"]
    missing = [key for key in required if not profile.get(key)]
    if missing:
        raise SystemExit(f"Profile {alias} missing fields: {', '.join(missing)}")
    profile = dict(profile)
    profile["alias"] = alias
    return profile


def scopes_for(profile: dict[str, Any]) -> list[str]:
    features = set(profile.get("features", ["upload"]))
    scopes = [UPLOAD_SCOPE]
    if "playlist" in features or "manage" in features:
        scopes.append(MANAGE_SCOPE)
    return scopes


def credentials_for(profile: dict[str, Any], force_auth: bool = False) -> Credentials:
    token_path = expand(profile["token_file"])
    scopes = scopes_for(profile)
    creds: Credentials | None = None

    if token_path.exists() and not force_auth:
        creds = Credentials.from_authorized_user_file(str(token_path), scopes=scopes)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    if not creds or not creds.valid or force_auth:
        client_path = expand(profile["client_secrets_file"])
        if not client_path.exists():
            raise SystemExit(f"OAuth client secrets not found: {client_path}")
        flow = InstalledAppFlow.from_client_secrets_file(str(client_path), scopes=scopes)
        creds = flow.run_local_server(host="127.0.0.1", port=0, open_browser=True)

    save_json_private(token_path, json.loads(creds.to_json()))
    return creds


def youtube_service(profile: dict[str, Any], force_auth: bool = False):
    creds = credentials_for(profile, force_auth=force_auth)
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def authenticated_channel(youtube) -> dict[str, Any]:
    response = youtube.channels().list(part="id,snippet", mine=True).execute()
    items = response.get("items", [])
    if len(items) != 1:
        raise SystemExit(f"Expected exactly one authenticated channel identity, got {len(items)}")
    return items[0]


def verify_channel(youtube, profile: dict[str, Any]) -> dict[str, Any]:
    channel = authenticated_channel(youtube)
    actual = channel.get("id")
    expected = profile["channel_id"]
    title = channel.get("snippet", {}).get("title", "")
    print(f"Resolved profile={profile['alias']} channel_id={actual} title={title!r}")
    if actual != expected:
        raise SystemExit(
            "FAIL-CLOSED: authenticated channel does not match profile. "
            f"expected={expected} actual={actual}"
        )
    return channel


def build_upload_body(profile: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    defaults = profile.get("defaults", {})
    title = manifest.get("title")
    if not title:
        raise SystemExit("Manifest requires a non-empty title")

    privacy = manifest.get("privacy", defaults.get("privacy", "private"))
    if privacy not in {"private", "unlisted", "public"}:
        raise SystemExit(f"Unsupported privacy value: {privacy}")

    snippet: dict[str, Any] = {
        "title": title,
        "description": manifest.get("description", ""),
        "categoryId": str(manifest.get("category_id", defaults.get("category_id", "22"))),
    }
    if manifest.get("tags"):
        snippet["tags"] = list(manifest["tags"])

    status: dict[str, Any] = {
        "privacyStatus": privacy,
        "selfDeclaredMadeForKids": bool(
            manifest.get("made_for_kids", defaults.get("made_for_kids", False))
        ),
    }
    if manifest.get("publish_at"):
        if privacy != "private":
            raise SystemExit("publish_at requires privacy=private for YouTube scheduling")
        status["publishAt"] = manifest["publish_at"]

    return {"snippet": snippet, "status": status}


def upload_video(youtube, profile: dict[str, Any], video_path: Path, manifest: dict[str, Any]) -> str:
    if not video_path.is_file():
        raise SystemExit(f"Video file not found: {video_path}")

    body = build_upload_body(profile, manifest)
    requested_privacy = body["status"]["privacyStatus"]
    print(
        f"Upload target profile={profile['alias']} channel_id={profile['channel_id']} "
        f"privacy={requested_privacy} file={video_path.name}"
    )

    mime, _ = mimetypes.guess_type(str(video_path))
    media = MediaFileUpload(
        str(video_path),
        mimetype=mime or "application/octet-stream",
        chunksize=8 * 1024 * 1024,
        resumable=True,
    )
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    while response is None:
        progress, response = request.next_chunk()
        if progress:
            print(f"Upload progress: {progress.progress() * 100:.1f}%")

    video_id = response.get("id")
    if not video_id:
        raise SystemExit("Upload returned no video ID")

    verify = youtube.videos().list(
        part="id,snippet,status,processingDetails", id=video_id
    ).execute()
    items = verify.get("items", [])
    if len(items) != 1:
        raise SystemExit(f"Upload returned video_id={video_id} but read-back verification failed")

    remote = items[0]
    remote_privacy = remote.get("status", {}).get("privacyStatus")
    remote_title = remote.get("snippet", {}).get("title")
    if remote_privacy != requested_privacy or remote_title != body["snippet"]["title"]:
        raise SystemExit(
            "Read-back mismatch after upload: "
            f"privacy={remote_privacy!r} title={remote_title!r}"
        )

    print(f"Verified upload video_id={video_id} privacy={remote_privacy} title={remote_title!r}")
    return video_id


def set_thumbnail(youtube, video_id: str, image_path: Path) -> None:
    if not image_path.is_file():
        raise SystemExit(f"Thumbnail not found: {image_path}")
    media = MediaFileUpload(str(image_path), resumable=False)
    youtube.thumbnails().set(videoId=video_id, media_body=media).execute()
    print(f"Thumbnail set for video_id={video_id}")


def add_to_playlist(youtube, video_id: str, playlist_id: str) -> None:
    body = {
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {"kind": "youtube#video", "videoId": video_id},
        }
    }
    youtube.playlistItems().insert(part="snippet", body=body).execute()
    print(f"Added video_id={video_id} to playlist_id={playlist_id}")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="DEDAL reference YouTube channel-operations client")
    p.add_argument("--config", default="~/.config/dedal/youtube/channels.json")
    p.add_argument("--profile", required=True)
    p.add_argument("--force-auth", action="store_true")
    sub = p.add_subparsers(dest="command", required=True)

    sub.add_parser("whoami")
    sub.add_parser("auth")

    up = sub.add_parser("upload")
    up.add_argument("--video", required=True)
    up.add_argument("--manifest", required=True)
    up.add_argument("--thumbnail")
    up.add_argument("--playlist-id")

    thumb = sub.add_parser("thumbnail")
    thumb.add_argument("--video-id", required=True)
    thumb.add_argument("--image", required=True)

    pl = sub.add_parser("playlist-add")
    pl.add_argument("--video-id", required=True)
    pl.add_argument("--playlist-id", required=True)
    return p


def main() -> int:
    args = parser().parse_args()
    profile = load_profile(expand(args.config), args.profile)
    youtube = youtube_service(profile, force_auth=args.force_auth or args.command == "auth")
    verify_channel(youtube, profile)

    if args.command in {"auth", "whoami"}:
        return 0

    if args.command == "upload":
        manifest = load_json(expand(args.manifest))
        video_id = upload_video(youtube, profile, expand(args.video), manifest)
        if args.thumbnail:
            set_thumbnail(youtube, video_id, expand(args.thumbnail))
        if args.playlist_id:
            add_to_playlist(youtube, video_id, args.playlist_id)
        return 0

    if args.command == "thumbnail":
        set_thumbnail(youtube, args.video_id, expand(args.image))
        return 0

    if args.command == "playlist-add":
        add_to_playlist(youtube, args.video_id, args.playlist_id)
        return 0

    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        raise SystemExit(130)
