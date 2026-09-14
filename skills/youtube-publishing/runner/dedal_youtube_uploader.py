#!/usr/bin/env python3
"""VPS runner: source bytes go directly to YouTube; no Google token is stored here."""
from __future__ import annotations
import argparse, hashlib, json, mimetypes, os, re, subprocess, sys
import urllib.error, urllib.request
from pathlib import Path

GATEWAY="https://youtube.drthorne.uk"
CHUNK=8*1024*1024

class RunnerError(RuntimeError): pass

def api(base, token, method, path, payload):
    req=urllib.request.Request(
        base.rstrip("/")+path,
        data=json.dumps(payload).encode(),
        method=method,
        headers={"Authorization":f"Bearer {token}","Content-Type":"application/json",
                 "User-Agent":"dedal-youtube-uploader/0.1.0"})
    try:
        with urllib.request.urlopen(req,timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        detail=exc.read(4096).decode("utf-8","replace")
        raise RunnerError(f"Gateway HTTP {exc.code}: {detail}") from exc

def download(url, target):
    target.parent.mkdir(parents=True,exist_ok=True)
    offset=target.stat().st_size if target.exists() else 0
    headers={"User-Agent":"dedal-youtube-uploader/0.1.0"}
    if offset: headers["Range"]=f"bytes={offset}-"
    try:
        response=urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=120)
    except urllib.error.HTTPError as exc:
        if exc.code==416 and target.exists(): return target
        raise RunnerError(f"Source download HTTP {exc.code}") from exc
    status=getattr(response,"status",200)
    mode="ab" if offset and status==206 else "wb"
    with response,target.open(mode) as output:
        while True:
            block=response.read(1024*1024)
            if not block: break
            output.write(block)
    if not target.is_file() or target.stat().st_size==0:
        raise RunnerError("Downloaded source is empty")
    return target

def resolve(job,state_dir):
    source=job["source"]
    if source["type"]=="google_drive":
        file_id=source["locator"]
        if not re.fullmatch(r"[A-Za-z0-9_-]{10,100}",file_id):
            raise RunnerError("Invalid Google Drive file ID")
        bridge_repo=os.getenv("DEDAL_YOUTUBE_DRIVE_BRIDGE_REPO")
        if not bridge_repo:
            raise RunnerError("DEDAL_YOUTUBE_DRIVE_BRIDGE_REPO is not set")
        target=Path(bridge_repo).resolve()/"downloads"/"dedal-youtube"/"drive"/file_id
        target.mkdir(parents=True,exist_ok=True)
        files=[p for p in target.iterdir() if p.is_file()]
        if not files:
            container_target=f"/app/downloads/dedal-youtube/drive/{file_id}/"
            result=subprocess.run(
                ["docker","exec","mirror-bot","rclone","backend","copyid",
                 "gdrive:",file_id,container_target],
                stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=1800)
            if result.returncode:
                raise RunnerError(f"Drive source fetch failed (exit {result.returncode})")
            files=[p for p in target.iterdir() if p.is_file()]
        if len(files)!=1:
            raise RunnerError(f"Drive source resolution expected one file, found {len(files)}")
        return files[0].resolve()
    if source["type"]=="local_file":
        path=Path(source["locator"]).expanduser().resolve()
        if not path.is_file(): raise RunnerError(f"Local source not found: {path}")
        return path
    if source["type"]=="direct_url":
        return download(source["locator"],state_dir/f"{job['id']}.source")
    raise RunnerError(f"Unsupported source type: {source['type']}")

def fingerprint(path):
    digest=hashlib.sha256()
    with path.open("rb") as stream:
        while True:
            block=stream.read(1024*1024)
            if not block: break
            digest.update(block)
    return "sha256:"+digest.hexdigest()

def verify_fingerprint(job,actual):
    expected=job.get("source_fingerprint")
    if not expected: return
    expected=expected if expected.startswith("sha256:") else "sha256:"+expected
    if not hashlib.compare_digest(expected.lower(),actual.lower()):
        raise RunnerError(f"Source fingerprint mismatch: expected={expected} actual={actual}")

def confirmed_offset(session,total):
    req=urllib.request.Request(session,data=b"",method="PUT",
        headers={"Content-Length":"0","Content-Range":f"bytes */{total}"})
    try:
        with urllib.request.urlopen(req,timeout=60) as response:
            result=json.load(response)
            return total,result.get("id")
    except urllib.error.HTTPError as exc:
        if exc.code==308:
            match=re.search(r"bytes=0-(\d+)",exc.headers.get("Range") or "")
            return (int(match.group(1))+1 if match else 0),None
        if exc.code in (404,410):
            raise RunnerError("Session expired/ambiguous; auto-restart is disabled to prevent duplicates") from exc
        raise RunnerError(f"Session query HTTP {exc.code}") from exc

def progress(base,token,job_id,count):
    api(base,token,"POST",f"/v1/upload-jobs/{job_id}/progress",
        {"bytes_uploaded":count})

def upload(path,session,mime,total,base,token,job_id):
    offset,done=confirmed_offset(session,total)
    if done: return done
    with path.open("rb") as stream:
        stream.seek(offset)
        while offset<total:
            block=stream.read(min(CHUNK,total-offset))
            if not block: raise RunnerError("Source ended before declared length")
            end=offset+len(block)-1
            req=urllib.request.Request(session,data=block,method="PUT",headers={
                "Content-Type":mime,"Content-Length":str(len(block)),
                "Content-Range":f"bytes {offset}-{end}/{total}"})
            try:
                with urllib.request.urlopen(req,timeout=300) as response:
                    result=json.load(response)
                    if not result.get("id"): raise RunnerError("Final response has no video ID")
                    progress(base,token,job_id,total)
                    return result["id"]
            except urllib.error.HTTPError as exc:
                if exc.code==308:
                    match=re.search(r"bytes=0-(\d+)",exc.headers.get("Range") or "")
                    offset=int(match.group(1))+1 if match else end+1
                    stream.seek(offset); progress(base,token,job_id,offset)
                    print(f"Uploaded {offset}/{total} bytes",flush=True); continue
                if exc.code in (404,410):
                    raise RunnerError("Upload session expired; reconcile before replacement") from exc
                detail=exc.read(4096).decode("utf-8","replace")
                raise RunnerError(f"YouTube HTTP {exc.code}: {detail}") from exc
    raise RunnerError("Upload returned no video ID")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--job-id",required=True)
    p.add_argument("--gateway",default=os.getenv("DEDAL_YOUTUBE_GATEWAY",GATEWAY))
    p.add_argument("--state-dir",default=os.getenv("DEDAL_YOUTUBE_STATE_DIR",
        "/var/lib/dedal-youtube-uploader"))
    args=p.parse_args()
    token=os.getenv("DEDAL_YOUTUBE_RUNNER_TOKEN")
    if not token: raise RunnerError("DEDAL_YOUTUBE_RUNNER_TOKEN is not set")
    inspected=api(args.gateway,token,"POST",
        f"/v1/upload-jobs/{args.job_id}/claim",{"inspect_only":True})["job"]
    source=resolve(inspected,Path(args.state_dir))
    actual=fingerprint(source); verify_fingerprint(inspected,actual)
    total=source.stat().st_size
    mime=mimetypes.guess_type(source.name)[0] or "application/octet-stream"
    claim=api(args.gateway,token,"POST",f"/v1/upload-jobs/{args.job_id}/claim",
        {"content_length":total,"content_type":mime,"source_fingerprint":actual})
    video_id=upload(source,claim["upload"]["session_url"],mime,total,
        args.gateway,token,args.job_id)
    verified=api(args.gateway,token,"POST",
        f"/v1/upload-jobs/{args.job_id}/complete",{"youtube_video_id":video_id})
    if verified["job"]["status"]!="verified":
        raise RunnerError("Gateway did not verify remote state")
    print(json.dumps(verified,indent=2))
    return 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except RunnerError as exc:
        print(f"ERROR: {exc}",file=sys.stderr); raise SystemExit(1)
