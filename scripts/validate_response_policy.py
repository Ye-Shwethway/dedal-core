#!/usr/bin/env python3
"""Check response-policy wiring and local planner cases; not a host or rendering test."""
import json
from pathlib import Path
import yaml
from response_plan import plan

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    root = Path(root)
    p = yaml.safe_load((root / 'kernel/response.yaml').read_text())
    assert p['schema_version'] == 1 and 'version' not in p
    assert p['default'] == 'prose' and p['mandatory_ui'] is False and p['mandatory_specialist_skill'] is False
    assert p['scope'] == 'global_response_orchestration'
    assert p['universe']['modes'] == ['Observing', 'Guided', 'Autonomous']
    assert p['universe']['canon_mutation_from_local_controls'] == 'forbidden'
    assert set(p['state_labels']) == {'illustrative_demo','calculated_from_entered_data','verified_live','persisted'}
    boot = yaml.safe_load((root / 'kernel/boot.yaml').read_text())
    step = next(s for s in boot['boot_sequence'] if s['id'] == 'operating_contract')
    assert 'kernel/response.yaml' in step['sources']
    kernel = yaml.safe_load((root / 'kernel/kernel.yaml').read_text())
    assert any(i['id'] == 'response_presentation' and i['enforce'] == 'reasoning' and i['spec'] == 'ref:kernel/response.yaml' for i in kernel['invariants'])
    assert yaml.safe_load((root / 'core-manifest.yaml').read_text())['response_contract'] == 'kernel/response.yaml'
    session = yaml.safe_load((root / 'kernel/session.yaml').read_text())
    assert any(s.get('file') == 'kernel/response.yaml' and s.get('required') for s in session['start'])
    fixtures = json.loads((root / 'evals/response-ui-contract.json').read_text())['cases']
    assert len({c['id'] for c in fixtures}) == len(fixtures)
    for c in fixtures:
        try:
            result = plan(c['request'], p)
        except ValueError:
            assert c.get('reject'), c['id']
            continue
        assert not c.get('reject'), c['id']
        assert result['surface'] == c['surface'], c['id']
        assert result['executed'] is False and result['canon_mutated'] is False
        assert result['essential_text_required'] is True
        assert result['local_control_effect'] == 'presentation_or_session_intent_only'
        for key, target in [('label','data_label'),('action','action_path'),('form','form_allowed')]:
            if key in c: assert result[target] == c[key], c['id']
    return len(fixtures)


if __name__ == '__main__':
    print(f'Response UI policy: boot/session wiring and {validate()} local planner cases PASS')
    print('Boundary: declarations/properties only; actual rendered controls, mobile layout and service truth require live evidence.')
