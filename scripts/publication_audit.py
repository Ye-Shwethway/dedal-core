#!/usr/bin/env python3
"""Select byte readback safely from a complete authoritative metadata snapshot.

Adapters supply observations, not authentication. Null revisions never prove
unchanged bytes. A verified source report precedes pointer activation; the final
pointer must separately be read back. There is no remote transaction/lock.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import PurePosixPath, Path

POINTER = 'state/active-release.json'
MANIFEST = 'state/release-manifest.json'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def valid_hash(value):
    return isinstance(value, str) and re.fullmatch('[0-9a-f]{64}', value) is not None


def release(raw):
    data = json.loads(raw)
    if data.get('schema_version') != 1 or data.get('algorithm') != 'sha256' or not re.fullmatch(r'\d+\.\d+\.\d+', str(data.get('core_version', ''))):
        raise ValueError('invalid release identity')
    hashes = data.get('files')
    if not isinstance(hashes, dict) or not hashes or {POINTER, MANIFEST} & set(hashes):
        raise ValueError('invalid release files')
    for p, h in hashes.items():
        path = PurePosixPath(p)
        if not p or path.is_absolute() or '..' in path.parts or str(path) != p or not valid_hash(h):
            raise ValueError('unsafe release path/digest')
    return data


def revision(value):
    # Transport currently supports concrete decimal Library revisions only.
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (str, int)) and re.fullmatch(r'\d+', str(value)):
        return str(int(value))
    return None


def identities(metadata, expected):
    if not isinstance(metadata, dict) or set(metadata) != expected:
        raise ValueError('complete unique canonical inventory required')
    for m in metadata.values():
        if not isinstance(m, dict) or not isinstance(m.get('library_file_id'), str) or not m['library_file_id']:
            raise ValueError('missing canonical identity')
    ids = [m['library_file_id'] for m in metadata.values()]
    if len(set(ids)) != len(ids):
        raise ValueError('duplicate canonical identity')


def plan(prior_raw, candidate_raw, baseline, metadata, mode='incremental', now=None):
    if mode not in {'incremental', 'full'}:
        raise ValueError('unknown audit mode')
    prior, candidate = release(prior_raw), release(candidate_raw)
    old, new = prior['files'], candidate['files']
    if set(old) - set(new):
        raise ValueError('removal requires explicit migration')
    expected = set(new) | {MANIFEST, POINTER}
    identities(metadata, expected)
    now = now or datetime.now(timezone.utc)
    usable = False
    if isinstance(baseline, dict) and baseline.get('schema_version') == 1 and baseline.get('status') == 'verified' and baseline.get('release_sha256') == digest(prior_raw):
        try:
            at = datetime.fromisoformat(baseline['full_audit_at'])
            usable = at.tzinfo is not None and timedelta(0) <= now - at <= timedelta(days=7)
        except (KeyError, TypeError, ValueError):
            pass
    entries = baseline.get('entries', {}) if usable else {}
    if not isinstance(entries, dict) or set(entries) != set(old) | {MANIFEST, POINTER}:
        usable = False
        entries = {}
    structural = any(old.get(p) != h and (p == 'core-manifest.yaml' or p.startswith(('kernel/', 'index/', 'scripts/', 'validators/')) or p.endswith('.schema.json')) for p, h in new.items())
    full = mode == 'full' or structural or not usable
    reads, reused, reasons = [], {}, {}
    wanted = {**new, MANIFEST: digest(candidate_raw)}
    for p, h in wanted.items():
        b, m = entries.get(p, {}), metadata[p]
        if not isinstance(b, dict):
            b = {}
        known = revision(m.get('version_id'))
        can_reuse = (not full and p != MANIFEST and old.get(p) == h
                     and b.get('sha256') == h and b.get('library_file_id') == m['library_file_id']
                     and known is not None and revision(b.get('version_id')) == known)
        if can_reuse:
            reused[p] = {'sha256': h, 'library_file_id': m['library_file_id'], 'version_id': known}
        else:
            reads.append(p)
            reasons[p] = 'full_audit' if full else ('changed_or_new' if old.get(p) != h else 'revision_unproven')
    return {'schema_version': 1, 'mode': 'full' if full else 'incremental',
            'prior_release_sha256': digest(prior_raw), 'candidate_release_sha256': digest(candidate_raw),
            'core_version': candidate['core_version'], 'full_audit_at': now.isoformat() if full else baseline['full_audit_at'], 'expected_hashes': wanted,
            'metadata': metadata, 'read_paths': sorted(reads), 'reuse': reused, 'read_reasons': reasons,
            'pointer_readback': 'required_after_activation', 'created_at': now.isoformat()}


def verify(audit, reads, latest):
    expected = audit['expected_hashes']
    identities(latest, set(expected) | {POINTER})
    if set(audit['read_paths']) | set(audit['reuse']) != set(expected) or set(audit['read_paths']) & set(audit['reuse']):
        raise ValueError('audit coverage incomplete')
    entries = {}
    for p, h in expected.items():
        initial, final = audit['metadata'][p], latest[p]
        if (initial['library_file_id'] != final['library_file_id'] or initial.get('version_id') != final.get('version_id')
                or initial.get('file_id') != final.get('file_id') or initial.get('modified_at') != final.get('modified_at')):
            raise ValueError('metadata changed during readback: ' + p)
        if p in audit['reuse']:
            b = audit['reuse'][p]
            if b['sha256'] != h or b['library_file_id'] != final['library_file_id'] or revision(final.get('version_id')) is None or revision(b['version_id']) != revision(final['version_id']):
                raise ValueError('invalid reused evidence: ' + p)
        else:
            b = reads.get(p, {})
            if b.get('sha256') != h or b.get('library_file_id') != final['library_file_id'] or b.get('version_id') != final.get('version_id'):
                raise ValueError('exact byte readback required: ' + p)
        entries[p] = {**final, 'sha256': h, 'verification': 'revision_reuse' if p in audit['reuse'] else 'fresh_bytes'}
    return {'schema_version': 1, 'status': 'sources_verified_pointer_pending',
            'release_sha256': audit['candidate_release_sha256'], 'core_version': audit['core_version'], 'full_audit_at': audit['full_audit_at'], 'mode': audit['mode'],
            'byte_read_count': len(audit['read_paths']), 'reused_count': len(audit['reuse']),
            'entries': entries, 'verified_at': datetime.now(timezone.utc).isoformat()}


def close(report, pointer_raw, pointer_metadata, latest):
    pointer = json.loads(pointer_raw)
    if report.get('status') != 'sources_verified_pointer_pending' or pointer.get('release_sha256') != report['release_sha256'] or pointer.get('release_manifest') != MANIFEST or pointer.get('schema_version') != 1 or pointer.get('core_version') != report['core_version']:
        raise ValueError('final pointer mismatch')
    manifest_entry = report['entries'][MANIFEST]
    if manifest_entry['sha256'] != report['release_sha256']:
        raise ValueError('manifest binding mismatch')
    identities(latest, set(report['entries']) | {POINTER})
    for p, e in report['entries'].items():
        m = latest[p]
        if any(e.get(k) != m.get(k) for k in ('library_file_id', 'version_id', 'file_id', 'modified_at')):
            raise ValueError('post-activation metadata drift: ' + p)
    if any(pointer_metadata.get(k) != latest[POINTER].get(k) for k in ('library_file_id', 'version_id', 'file_id', 'modified_at')):
        raise ValueError('final pointer readback stale')
    return {**report, 'status': 'verified', 'entries': {**report['entries'], POINTER: {**pointer_metadata, 'sha256': digest(pointer_raw), 'verification': 'fresh_bytes'}}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['plan', 'verify', 'close'])
    parser.add_argument('--input', type=Path, required=True, help='JSON adapter observations; manifest/pointer paths contain exact bytes')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        d = json.loads(args.input.read_text())
        if args.action == 'plan':
            result = plan(Path(d['prior_manifest']).read_bytes(), Path(d['candidate_manifest']).read_bytes(), d.get('baseline'), d['metadata'], d.get('mode', 'incremental'))
        elif args.action == 'verify':
            result = verify(d['plan'], d['reads'], d['metadata'])
        else:
            result = close(d['report'], Path(d['pointer']).read_bytes(), d['pointer_metadata'], d['metadata'])
        args.output.write_text(json.dumps(result, indent=2) + '\n')
        print('PUBLICATION AUDIT:', result.get('status', result.get('mode')))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, str(exc) + '\n')
