#!/usr/bin/env python3
"""Check asset-bound review/approval/release state; external refs need owner evidence."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
from urllib.parse import urlparse, parse_qs

ACTIONS = {'render_review', 'deliver_review', 'private_upload', 'thumbnail', 'publish', 'close'}


def require(value, message):
    if not value:
        raise ValueError(message)


def ref(record, field, message):
    require(isinstance(record, dict) and isinstance(record.get(field), str)
            and bool(record[field].strip()), message)


def probe(path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                             'format=duration:stream=codec_type,width,height', '-of', 'json', str(path)],
                            capture_output=True, text=True, check=True, timeout=30)
    data = json.loads(result.stdout)
    video = next(x for x in data['streams'] if x.get('codec_type') == 'video')
    return {'duration': float(data['format']['duration']), 'width': video['width'], 'height': video['height']}


def validate(state, action, task_id, probe_media=probe):
    require(action in ACTIONS, 'unknown media action')
    require(isinstance(state, dict) and state.get('schema_version') == 1
            and state.get('task_id') == task_id, 'media task identity')
    asset = state.get('asset', {})
    path = Path(asset.get('path', ''))
    require(path.is_absolute() and path.is_file(), 'final media unavailable')
    raw = path.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    require(asset.get('sha256') == sha and asset.get('size_bytes') == len(raw), 'final media hash/size mismatch')
    actual = probe_media(path)
    duration = asset.get('duration')
    require(type(duration) in (int, float) and math.isfinite(duration) and duration > 0
            and abs(duration - actual['duration']) <= .05
            and asset.get('width') == actual['width'] and asset.get('height') == actual['height'],
            'final media probe mismatch; draft metadata cannot close')
    ref(asset, 'qc_ref', 'rendered QC evidence missing')
    if action == 'render_review':
        return {'action': action, 'asset_sha256': sha}
    if action not in {'deliver_review', 'render_review'} and state.get('review_required') is False:
        ref(state, 'review_not_required_ref', 'explicit already-approved source/handoff exemption missing')
    else:
        validate_review(state, sha, len(raw))
    if action == 'deliver_review':
        return {'action': action, 'asset_sha256': sha}
    approval = state.get('media_approval', {})
    require(approval.get('asset_sha256') == sha, 'media approval belongs to another master')
    ref(approval, 'creator_ref', 'actual Creator media approval missing')
    package = state.get('package', {})
    require(package.get('asset_sha256') == sha, 'launch package belongs to another master')
    ref(package, 'locked_ref', 'locked launch package missing')
    ref(state.get('target', {}), 'channel_id', 'target channel missing')
    ref(state.get('target', {}), 'verified_ref', 'target ownership readback missing')
    ref(state, 'publishing_authority_ref', 'publication authority missing')
    ref(state, 'single_flight_ref', 'existing result/idempotency check missing')
    if action == 'private_upload':
        return {'action': action, 'asset_sha256': sha, 'cover_pending_allowed': True}
    return validate_release(state, action, sha)


def validate_review(state, sha, size):
    review = state.get('review', {})
    require(review.get('asset_sha256') == sha and review.get('size_bytes') == size, 'review master identity mismatch')
    for field in ('file_id', 'parent_id', 'verified_ref', 'delivered_ref'):
        ref(review, field, 'review upload/readback/link delivery missing: ' + field)
    url = urlparse(review.get('view_url', ''))
    require(url.scheme == 'https' and bool(url.netloc), 'accessible review link missing')
    if url.hostname == 'drive.google.com':
        parts=url.path.strip('/').split('/')
        file_id=parts[2] if len(parts)>=3 and parts[:2]==['file','d'] else parse_qs(url.query).get('id',[None])[0]
        require(file_id == review['file_id'], 'Drive view link belongs to another file')


def validate_release(state, action, sha):
    options = state.get('cover_options', [])
    require(isinstance(options, list) and options, 'cover options missing')
    ids = set()
    for option in options:
        require(isinstance(option, dict) and isinstance(option.get('id'), str)
                and option['id'] not in ids and option.get('asset_sha256') == sha, 'cover option identity')
        ids.add(option['id'])
        ref(option, 'presented_ref', 'cover options not presented to Creator')
        image = Path(option.get('path', ''))
        require(image.is_absolute() and image.is_file()
                and hashlib.sha256(image.read_bytes()).hexdigest() == option.get('sha256'), 'cover pixels unavailable/changed')
    choice = state.get('cover_approval', {})
    require(choice.get('asset_sha256') == sha and choice.get('mode') in ('chosen', 'delegated'), 'cover approval pending')
    ref(choice, 'creator_ref', 'actual Creator cover selection/delegation missing')
    selected = next((o for o in options if o['id'] == choice.get('option_id')), None)
    require(selected is not None, 'selected cover is not a presented option')
    upload = state.get('upload', {})
    require(upload.get('asset_sha256') == sha and upload.get('upload_status') == 'processed'
            and upload.get('processing_status') == 'succeeded', 'private upload not ready')
    ref(upload, 'video_id', 'owned upload identity missing')
    ref(upload, 'verified_ref', 'upload/processing readback missing')
    if action == 'thumbnail':
        return {'action': action, 'asset_sha256': sha, 'cover_sha256': selected['sha256']}
    thumbnail = state.get('thumbnail', {})
    require(thumbnail.get('video_id') == upload['video_id'] and thumbnail.get('cover_sha256') == selected['sha256'],
            'applied cover differs from selected cover')
    ref(thumbnail, 'verified_ref', 'thumbnail readback missing')
    if action == 'publish':
        return {'action': action, 'asset_sha256': sha, 'cover_sha256': selected['sha256']}
    publication = state.get('publication', {})
    require(publication.get('video_id') == upload['video_id'] and publication.get('visibility') == 'public', 'public result mismatch')
    ref(publication, 'verified_ref', 'final public readback missing')
    ref(state, 'archive_verified_ref', 'master archive readback missing')
    ref(state, 'checkpoint_ref', 'continuity checkpoint missing')
    return {'action': action, 'asset_sha256': sha, 'cover_sha256': selected['sha256']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--state', type=Path, required=True)
    parser.add_argument('--action', choices=sorted(ACTIONS), required=True)
    parser.add_argument('--task-id', required=True)
    args = parser.parse_args()
    try:
        result = validate(json.loads(args.state.read_text()), args.action, args.task_id)
        print(json.dumps({'status': 'pass', **result, 'boundary': 'local properties checked; external references require actual owner/Creator evidence; no host interception'}))
    except (ValueError, OSError, KeyError, TypeError, StopIteration, subprocess.SubprocessError) as exc:
        parser.exit(1, 'MEDIA WORKFLOW: FAIL ' + str(exc) + '\n')
