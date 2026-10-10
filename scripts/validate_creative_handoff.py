#!/usr/bin/env python3
"""Offline, advisory DEDAL creative-handoff checks; NOT rendered-media or canon verification."""
import json
import math
import sys
from pathlib import Path


def finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def check(doc):
    errors = []
    def fail(message): errors.append(message)
    if not isinstance(doc, dict): return ['document must be an object']
    kind = doc.get('kind')
    if kind == 'scene_shots':
        if not all(isinstance(doc.get(k), str) and doc[k].strip() for k in ('scene_id', 'beat_id')):
            fail('nonblank scene_id and beat_id required')
        canon = doc.get('canon_subject_ids', [])
        if not isinstance(canon, list) or not all(isinstance(x, str) and x.strip() for x in canon) or len(canon) != len(set(canon)):
            fail('canon_subject_ids must be a string list'); canon = []
        shots = doc.get('shots', [])
        if not isinstance(shots, list) or not 1 <= len(shots) <= 4:
            return errors + ['shots must contain 1..4 cards']
        ids = set(); phases = []; previous_axis = None
        for i, shot in enumerate(shots):
            if not isinstance(shot, dict): fail(f'shot {i}: must be object'); continue
            sid = shot.get('id')
            if not isinstance(sid, str) or not sid.strip() or sid in ids: fail(f'shot {i}: missing/duplicate id')
            else: ids.add(sid)
            subjects = shot.get('subject_ids', [])
            if not isinstance(subjects, list) or any(not isinstance(x, str) or not x.strip() for x in subjects) or len(subjects) != len(set(subjects)):
                fail(f'shot {i}: subject_ids must be string list')
            else:
                unknown = set(subjects) - set(canon)
                if unknown: fail(f'shot {i}: noncanon subjects {sorted(unknown)}')
            phase = shot.get('action_phase'); phases.append(phase)
            axis = shot.get('camera_axis')
            if axis not in ('left', 'right', 'on_axis', 'intentional_cross'):
                fail(f'shot {i}: invalid camera_axis')
            if previous_axis in ('left', 'right') and axis in ('left', 'right') and previous_axis != axis and not (isinstance(shot.get('axis_crossing_justification'), str) and shot['axis_crossing_justification'].strip()):
                fail(f'shot {i}: unmotivated axis crossing')
            previous_axis = axis
            edges = shot.get('contact_edges', [])
            if not isinstance(edges, list): fail(f'shot {i}: contact_edges must be list'); continue
            for edge in edges:
                if not isinstance(edge, dict): fail(f'shot {i}: contact edge not object'); continue
                if edge.get('observability') not in ('visible', 'occluded', 'unknown'): fail(f'shot {i}: observability unspecified')
                if edge.get('verdict') == 'PASS' and edge.get('observability') != 'visible':
                    fail(f'shot {i}: cannot PASS unobservable contact')
        if doc.get('distinct_action_phases') and (any(not isinstance(p,str) or not p.strip() for p in phases) or len(set(phases)) != len(phases)):
            fail('repeated/unspecified action phase')
        if doc.get('acceptance') == 'accepted' and not (isinstance(doc.get('creator_acceptance_evidence'), str) and doc['creator_acceptance_evidence'].strip()):
            fail('accepted state needs Creator evidence')
    elif kind == 'edit_decisions':
        assets = doc.get('assets', {}); clips = doc.get('clips', [])
        if not isinstance(assets, dict): fail('assets must be object'); assets = {}
        if not isinstance(clips, list) or not clips: return errors + ['clips required']
        for i, clip in enumerate(clips):
            if not isinstance(clip, dict): fail(f'clip {i}: must be object'); continue
            asset = assets.get(clip.get('asset_id'))
            if not isinstance(asset, dict): fail(f'clip {i}: asset missing'); continue
            duration = asset.get('duration_s'); start = clip.get('in_s'); end = clip.get('out_s'); at = clip.get('timeline_start_s')
            if not all(finite_number(v) for v in (duration, start, end, at)):
                fail(f'clip {i}: numeric finite times required'); continue
            if not 0 <= start < end <= duration: fail(f'clip {i}: invalid source interval')
            if at < 0: fail(f'clip {i}: negative timeline start')
            if duration <= 0: fail(f'clip {i}: invalid source duration')
        if doc.get('render_status') == 'verified' and not (isinstance(doc.get('playback_evidence'), str) and doc['playback_evidence'].strip()):
            fail('verified render requires playback evidence')
    elif kind == 'evidence':
        assertions = doc.get('assertions', [])
        if not isinstance(assertions, list) or not assertions: return ['assertions required']
        for i, assertion in enumerate(assertions):
            if not isinstance(assertion, dict): fail(f'assertion {i}: must be object'); continue
            if assertion.get('status') not in ('PASS', 'FAIL', 'UNKNOWN'): fail(f'assertion {i}: invalid status')
            if assertion.get('status') == 'PASS' and not (isinstance(assertion.get('evidence_ref'), str) and assertion['evidence_ref'].strip()):
                fail(f'assertion {i}: PASS requires evidence')
    else: fail(f'unsupported kind: {kind}')
    return errors


def main():
    if len(sys.argv) != 2: print('usage: validate_creative.py FILE.json'); return 2
    try: payload = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc: print(f'INVALID_INPUT: {exc}'); return 2
    errors = check(payload)
    print(json.dumps({'status':'FAIL' if errors else 'PASS','scope':'static-contract-only','errors':errors},indent=2))
    return 1 if errors else 0

if __name__ == '__main__': sys.exit(main())
