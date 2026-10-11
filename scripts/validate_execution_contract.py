#!/usr/bin/env python3
"""Cross-domain partial-result, unknown-effect and continuation regressions."""
from copy import deepcopy
from execution_check import check, continue_unit


def rejects(record, phase='close'):
    try:
        check(record, phase)
    except ValueError:
        return
    raise AssertionError('incomplete/invalid execution accepted')


for owner in ['medicine-store-assistant', 'files', 'youtube-publishing', 'research',
              'visual-narrative-production', 'software-development']:
    base = {'schema_version': 1, 'task_id': 'task', 'owner': owner, 'operation': 'review',
            'release_sha256': 'a' * 64, 'pending_effects': [],
            'items': [{'id': 'result', 'required': True, 'status': 'verified', 'evidence_ref': 'observed:1'}]}
    assert check(base, 'close')['coverage'] == 'complete'
    for status in ['planned', 'partial', 'blocked', 'failed', 'unknown']:
        candidate = deepcopy(base); candidate['items'][0]['status'] = status
        assert check(candidate, 'plan')['coverage'] == 'incomplete'
        rejects(candidate)
    for mutate in [lambda r: r['items'][0].pop('evidence_ref'),
                   lambda r: r['pending_effects'].append('unacknowledged_write'),
                   lambda r: r['items'].append(deepcopy(r['items'][0])),
                   lambda r: r.update(items=[]), lambda r: r.update(release_sha256='not-a-digest')]:
        candidate = deepcopy(base); mutate(candidate); rejects(candidate)
    assert continue_unit(base, 'task', 'a' * 64)['retry_authorized'] is False
    assert continue_unit(base, 'new', 'a' * 64)['action'] == 'recompose'
    assert continue_unit(base, 'task', 'b' * 64)['action'] == 'recompose'
    assert continue_unit(base, 'task', 'a' * 64, material_change=True)['action'] == 'recompose'
print('EXECUTION COVERAGE: PASS six domains, incomplete outcomes, unknown effects and continuation boundaries')
