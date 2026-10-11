#!/usr/bin/env python3
"""Check compact cross-domain execution coverage; never authenticate observations."""
import argparse
import json
from pathlib import Path


def check(record, phase):
    if phase not in {'plan', 'close'}:
        raise ValueError('unknown phase')
    if not isinstance(record, dict) or record.get('schema_version') != 1:
        raise ValueError('execution record schema')
    for field in ('task_id', 'owner', 'operation', 'release_sha256'):
        if not isinstance(record.get(field), str) or not record[field].strip():
            raise ValueError('missing work-unit identity: ' + field)
    digest = record['release_sha256']
    if len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
        raise ValueError('invalid release digest')
    items = record.get('items')
    if not isinstance(items, list) or not items:
        raise ValueError('required result scope missing')
    seen, pending = set(), []
    statuses = {'planned', 'verified', 'failed', 'blocked', 'unknown', 'partial'}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not item['id'] or item['id'] in seen:
            raise ValueError('duplicate/invalid result identity')
        seen.add(item['id'])
        if type(item.get('required')) is not bool or item.get('status') not in statuses:
            raise ValueError('invalid required/status declaration')
        if item.get('status') == 'verified' and not item.get('evidence_ref'):
            raise ValueError('verified claim without evidence reference')
        if item['required'] and item['status'] != 'verified':
            pending.append(item['id'])
    effects = record.get('pending_effects')
    if not isinstance(effects, list):
        raise ValueError('pending effects must be explicit')
    if phase == 'close' and (pending or effects):
        raise ValueError('incomplete required outcomes or unknown effects: ' + repr(pending))
    return {'task_id': record['task_id'], 'phase': phase, 'pending': pending,
            'coverage': 'complete' if not pending and not effects else 'incomplete',
            'boundary': 'declarations_only_not_authenticated_outcome_or_permission'}


def continue_unit(prior, task_id, release_sha256, *, material_change=False):
    """Return a context hint, never permission to replay or skip current gates."""
    check(prior, 'plan')
    if material_change or prior['task_id'] != task_id or prior['release_sha256'] != release_sha256:
        return {'action': 'recompose', 'authority': 'current_task_and_owner_required'}
    return {'action': 'reuse_task_context_refresh_volatile_owner_state',
            'owner': prior['owner'], 'operation': prior['operation'],
            'pending_effects': prior['pending_effects'], 'retry_authorized': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--record', type=Path, required=True)
    parser.add_argument('--phase', choices=['plan', 'close'], required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(check(json.loads(args.record.read_text()), args.phase)))
    except (ValueError, OSError, TypeError) as exc:
        parser.exit(1, str(exc) + '\n')
