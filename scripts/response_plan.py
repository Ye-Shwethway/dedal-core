#!/usr/bin/env python3
"""Plan optional response presentation from explicit declarations; never execute UI actions."""
import argparse
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def plan(request, policy=None):
    policy = policy or yaml.safe_load((ROOT / 'kernel/response.yaml').read_text())
    fields = {'function', 'interaction_benefit', 'host_ui_supported', 'narrative',
              'ui_requested', 'data_state', 'source_ref', 'observed_at', 'readback_ref',
              'authorized_write', 'stale', 'consequential', 'essential_fields'}
    if not isinstance(request, dict) or set(request) - fields:
        raise ValueError('unknown request fields')
    for key in ['interaction_benefit', 'host_ui_supported', 'narrative', 'ui_requested',
                'authorized_write', 'stale', 'consequential']:
        if key in request and type(request[key]) is not bool:
            raise ValueError('boolean declaration required: ' + key)
    if type(request.get('essential_fields', 0)) is not int or request.get('essential_fields', 0) < 0:
        raise ValueError('essential field count must be a nonnegative integer')
    function = request.get('function', 'plain')
    if function not in ['plain', *policy['eligible_functions']]:
        raise ValueError('unknown presentation function')
    state = request.get('data_state', 'illustrative_demo')
    if state not in policy['state_labels']:
        raise ValueError('unknown data state')
    nonempty = lambda key: isinstance(request.get(key), str) and bool(request[key].strip())
    if state in {'verified_live', 'persisted'}:
        if request.get('stale', False) or not all(nonempty(k) for k in ['source_ref', 'observed_at', 'readback_ref']):
            raise ValueError('current live/persisted state requires attributable readback declarations')
    if state == 'persisted' and not request.get('authorized_write', False):
        raise ValueError('persistence requires authorized owner write declaration')
    useful = function in policy['eligible_functions'] and request.get('interaction_benefit', False)
    supported = request.get('host_ui_supported', False)
    narrative = request.get('narrative', False)
    ui = useful and supported and (not narrative or request.get('ui_requested', False))
    return {
        'surface': 'prose_with_secondary_ui' if ui and narrative else 'compact_ui_with_text' if ui else 'prose',
        'reason': 'useful_supported_interaction' if ui else 'prose_default_or_unavailable_surface',
        'data_label': state,
        'snapshot_label': 'stale' if request.get('stale', False) else 'declared_state',
        'form_allowed': ui and function == 'workflow_configuration' and request.get('essential_fields', 0) > 1,
        'local_control_effect': 'presentation_or_session_intent_only',
        'action_path': 'authorized_domain_tools_and_readback_required' if request.get('consequential', False) else 'local_presentation',
        'executed': False,
        'canon_mutated': False,
        'essential_text_required': True,
        'mobile_and_accessibility_review_required': ui,
        'evidence_boundary': 'declarations_only_not_host_rendering_or_service_verification',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('request', type=Path)
    args = parser.parse_args()
    print(json.dumps(plan(json.loads(args.request.read_text())), indent=2))
