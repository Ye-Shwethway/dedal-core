#!/usr/bin/env python3
"""Persistent outbound-polling DEDAL YouTube runner.

The daemon never stores Google OAuth credentials. It polls the bounded Gateway with the
runner token, discovers one actionable upload job, and delegates the actual resumable
upload to dedal-youtube-uploader. GitHub Actions remains deployment/recovery only.
"""
from __future__ import annotations
import fcntl
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

GATEWAY = os.getenv("DEDAL_YOUTUBE_GATEWAY", "https://youtube.drthorne.uk").rstrip("/")
TOKEN = os.getenv("DEDAL_YOUTUBE_RUNNER_TOKEN", "")
UPLOADER = os.getenv("DEDAL_YOUTUBE_UPLOADER_BIN", "/usr/local/bin/dedal-youtube-uploader")
POLL_SECONDS = max(2, int(os.getenv("DEDAL_YOUTUBE_RUNNER_POLL_SECONDS", "5")))
ERROR_BACKOFF_SECONDS = max(POLL_SECONDS, int(os.getenv("DEDAL_YOUTUBE_RUNNER_ERROR_BACKOFF_SECONDS", "15")))
LOCK_PATH = Path(os.getenv("DEDAL_YOUTUBE_RUNNER_LOCK", "/run/dedal-youtube-runner.lock"))
USER_AGENT = "dedal-youtube-runner-daemon/0.1.0"

def next_job():
    req = urllib.request.Request(
        GATEWAY + "/v1/upload-jobs/next",
        method="GET",
        headers={"Authorization": f"Bearer {TOKEN}", "User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)

def log(event, **details):
    safe = {"event": event, **details}
    print(json.dumps(safe, sort_keys=True), flush=True)

def main():
    if not TOKEN:
        raise RuntimeError("DEDAL_YOUTUBE_RUNNER_TOKEN is not set")
    if not Path(UPLOADER).is_file():
        raise RuntimeError(f"Uploader not found: {UPLOADER}")
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOCK_PATH.open("w") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError("another DEDAL YouTube runner daemon is already active") from exc
        log("runner_daemon_started", poll_seconds=POLL_SECONDS)
        while True:
            try:
                payload = next_job()
                job = payload.get("job")
                if not job:
                    time.sleep(int(payload.get("poll_after_seconds") or POLL_SECONDS))
                    continue
                job_id = str(job.get("id") or "")
                if not job_id:
                    log("queue_response_missing_job_id")
                    time.sleep(ERROR_BACKOFF_SECONDS)
                    continue
                log("upload_job_discovered", job_id=job_id, phase=job.get("phase"), status=job.get("status"))
                result = subprocess.run([UPLOADER, "--job-id", job_id], check=False)
                if result.returncode:
                    log("upload_job_runner_failed", job_id=job_id, exit_code=result.returncode)
                    time.sleep(ERROR_BACKOFF_SECONDS)
                else:
                    log("upload_job_runner_completed", job_id=job_id)
            except (urllib.error.URLError, urllib.error.HTTPError) as exc:
                log("queue_poll_failed", error=type(exc).__name__)
                time.sleep(ERROR_BACKOFF_SECONDS)
            except Exception as exc:
                log("runner_loop_error", error=type(exc).__name__)
                time.sleep(ERROR_BACKOFF_SECONDS)

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(0)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
