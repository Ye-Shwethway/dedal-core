#!/usr/bin/env python3
"""Validate optional creative planning contracts; never certify rendered physics."""
from copy import deepcopy
import json
from pathlib import Path
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
shot = json.loads((ROOT / 'skills/visual-narrative-production/schemas/shot-spec.schema.json').read_text())
motion = json.loads((ROOT / 'skills/generative-video-direction/schemas/motion-shot-spec.schema.json').read_text())
for schema in (shot, motion):
    Draft202012Validator.check_schema(schema)

def accepts(data, schema):
    Draft202012Validator(schema).validate(data)

def rejects(data, schema):
    try:
        accepts(data, schema)
    except ValidationError:
        return
    raise AssertionError('invalid planning declaration accepted')

old_shot = {'shot_id': 'S1', 'purpose': 'free hand before knock', 'subjects': [{}], 'continuity': {}}
old_motion = {'shot_id': 'M1', 'narrative_function': 'transfer', 'start_state': {},
              'temporal_change': {}, 'end_state': {}, 'acceptance_checks': []}
accepts(old_shot, shot)
accepts(old_motion, motion)
design = {'beat_id': 'B1', 'physical_events': [{'precondition': 'right hand holds case',
          'action': 'place case in supported recess', 'resulting_state': 'right hand free'}],
          'evidence_landmarks': ['case support and open right palm'],
          'observed_qa': [{'relation': 'case support', 'result': 'not_observable',
                           'evidence': 'support outside supplied crop'}]}
accepts({**old_shot, 'production_design': design}, shot)
rejects({**old_shot, 'production_design': {**design, 'physical_events': []}}, shot)
rejects({**old_shot, 'production_design': {**design, 'observed_qa': [
    {'relation': 'grip', 'result': 'pass', 'evidence': ''}]}}, shot)
pair = {'from_asset': 'A', 'to_asset': 'B', 'relation': 'continuous',
        'mechanism': 'settle implement on floor, open grip, withdraw hand',
        'timing_assumptions': 'provisional 2s, provider unknown',
        'camera_relation': 'locked', 'decision': 'unresolved'}
plan = {'stage': 'planned', 'pixel_qa_status': 'pending', 'pairs': [pair]}
accepts({**old_motion, 'source_only_plan': plan}, motion)
for stage in ('source_ready', 'sent', 'acknowledged'):
    rejects({**old_motion, 'source_only_plan': {**plan, 'stage': stage}}, motion)
    rejects({**old_motion, 'source_only_plan': {**plan, 'stage': stage,
             'pixel_qa_status': 'passed'}}, motion)
rejects({**old_motion, 'source_only_plan': {**plan, 'stage': 'video_verified'}}, motion)
accepts({**old_motion, 'source_only_plan': {**plan, 'stage': 'source_ready',
         'pixel_qa_status': 'passed', 'pairs': [{**pair, 'decision': 'ready'}]}}, motion)
accepts({**old_motion, 'source_only_plan': {**plan, 'stage': 'source_ready',
         'pixel_qa_status': 'passed', 'pairs': [{**pair, 'relation': 'cut', 'decision': 'cut'}]}}, motion)

for owner, name in [('story-weaver', 'causal-scene-design.md'),
                    ('visual-narrative-production', 'source-production-design.md'),
                    ('generative-video-direction', 'source-only-motion-readiness.md')]:
    body = (ROOT / f'skills/{owner}/SKILL.md').read_text()
    assert f'references/{name}' in body
    assert len(body.splitlines()) < 500
    assert (ROOT / f'skills/{owner}/references/{name}').is_file()

print('Creative source contracts: 2 schemas, 6 valid / 9 rejected declarations; 3 skill entrypoints linked')
print('Scope: structural planning only; pixel realism, motion and external ACK remain unverified')
