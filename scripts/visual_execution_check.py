#!/usr/bin/env python3
"""Validate visual input declarations, not pixel truth or Creator acceptance."""
def check(card):
    if not isinstance(card, dict) or card.get('mode') not in {'single', 'anchor', 'edit', 'group', 'action', 'sequence'}:
        raise ValueError('visual mode missing')
    subjects = card.get('subjects')
    if not isinstance(subjects, list) or not subjects:
        raise ValueError('subject roster missing')
    slots, identities = {}, set()
    for subject in subjects:
        if not isinstance(subject, dict):
            raise ValueError('invalid subject')
        slot, identity = subject.get('slot'), subject.get('identity')
        if not isinstance(slot, str) or not slot or slot in slots or not isinstance(identity, str) or not identity:
            raise ValueError('subject identity/slot missing or duplicate')
        if identity in identities or type(subject.get('instances')) is not int or subject['instances'] != 1:
            raise ValueError('duplicate identity/instances; specialized scene requires separate reviewed contract')
        roles = subject.get('required_pixel_roles')
        if not isinstance(roles, list) or any(not isinstance(r, str) or not r for r in roles) or len(set(roles)) != len(roles):
            raise ValueError('required pixel roles must be explicit')
        slots[slot] = set(roles); identities.add(identity)
    bindings = card.get('bindings')
    if not isinstance(bindings, list):
        raise ValueError('bindings must be explicit')
    seen = set()
    for binding in bindings:
        if not isinstance(binding, dict):
            raise ValueError('invalid binding')
        key = binding.get('subject'), binding.get('role')
        if key[0] not in slots or key in seen or not isinstance(key[1], str) or not key[1]:
            raise ValueError('binding subject/role conflict')
        if not binding.get('source_id') or not binding.get('actual_input') or binding.get('status') != 'bound':
            raise ValueError('required pixels not declared bound to actual input')
        seen.add(key)
    if any((slot, role) not in seen for slot, roles in slots.items() for role in roles):
        raise ValueError('missing required subject pixel role')
    if type(card.get('requested_assets')) is not int or card['requested_assets'] < 1 or card.get('format') != 'standalone':
        raise ValueError('output count/format missing')
    if card['mode'] == 'edit' and (not card.get('base_input') or not card.get('change') or not card.get('preserve')):
        raise ValueError('edit base/change/preserve missing')
    return {'coverage': 'declared_inputs_complete', 'pixel_truth': 'unverified', 'host_binding': 'unattested'}
