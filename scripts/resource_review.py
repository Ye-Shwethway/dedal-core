#!/usr/bin/env python3
"""Validate declared screening/review evidence; cannot judge pixels or intercept tools."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from datetime import datetime


def stamp(value):
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00')).timestamp()
    except (ValueError, TypeError, AttributeError):
        return None


def check(profile, record, stage='accept', scope='resource', opportunity_id=None, asset_paths=None):
    errors = []
    policy = profile.get('review_policy')
    if not isinstance(policy, dict):
        return {'passed': False, 'errors': ['review_policy_unresolved']}
    if stage not in ('present', 'accept') or scope not in ('resource', 'opportunity'):
        return {'passed': False, 'errors': ['invalid_review_operation']}
    keys = ('visual_required', 'creator_acceptance_required', 'visual_dimensions',
            'allowed_resource_evidence', 'allowed_opportunity_evidence')
    if (any(k not in policy for k in keys)
            or type(policy['visual_required']) is not bool
            or type(policy['creator_acceptance_required']) is not bool
            or any(not isinstance(policy[k], list) for k in keys[2:])):
        return {'passed': False, 'errors': ['review_policy_invalid']}
    if not profile.get('profile_id'):
        return {'passed': False, 'errors': ['profile_identity_missing']}
    if scope == 'opportunity' and not opportunity_id:
        return {'passed': False, 'errors': ['opportunity_identity_missing']}
    relevant = lambda x: x.get('scope') == scope and x.get('opportunity_id') == opportunity_id
    decisions = [x for x in record.get('reviews', []) if relevant(x) and x.get('profile_id') == profile['profile_id']]
    times = [stamp(x.get('decided_at')) for x in decisions]
    if any(t is None for t in times) or any(b < a for a, b in zip(times, times[1:])):
        errors.append('review_history_chronology_invalid')
    decision = decisions[-1] if decisions else {}
    if decision.get('status') in ('rejected', 'hold'):
        errors.append('creator_' + decision['status'])
    required = policy.get('visual_required', False)
    dimensions = policy.get('visual_dimensions', [])
    evidence = [x for x in record.get('visual_evidence', []) if relevant(x)]
    eligible = {}
    if required:
        if not dimensions:
            errors.append('visual_dimensions_missing')
        for e in evidence:
            eid = e.get('asset_id')
            why = []
            if not eid or eid in eligible:
                why.append('asset_identity_invalid')
            if e.get('kind') not in policy.get('allowed_' + scope + '_evidence', []):
                why.append('evidence_kind_wrong_for_scope')
            if e.get('origin') == 'generated':
                why.append('generated_image_is_not_observational_proof')
            if not e.get('source_ref') or not e.get('storage_ref'):
                why.append('source_or_retained_identity_missing')
            if not re.fullmatch('[0-9a-f]{64}', e.get('sha256', '')):
                why.append('digest_missing')
            if not e.get('media_type', '').startswith('image/'):
                why.append('image_bytes_unverified')
            inspection = e.get('inspection', {})
            inspected = stamp(inspection.get('observed_at'))
            if (inspection.get('status') != 'passed' or not inspection.get('read_ref') or inspected is None
                    or inspection.get('profile_id') != profile['profile_id']):
                why.append('direct_visual_inspection_missing')
            judged = {x.get('id'): x for x in inspection.get('dimensions', [])}
            if any(judged.get(d, {}).get('result') != 'pass' or not judged.get(d, {}).get('reason') for d in dimensions):
                why.append('visual_dimension_failed_or_unknown')
            displayed = stamp(e.get('displayed_at'))
            if not e.get('display_ref') or displayed is None or (inspected is not None and displayed < inspected):
                why.append('review_display_missing_or_before_screening')
            if asset_paths is not None:
                path = asset_paths.get(eid)
                if not path or not Path(path).is_file():
                    why.append('retained_bytes_missing')
                else:
                    data = Path(path).read_bytes()
                    if hashlib.sha256(data).hexdigest() != e.get('sha256'):
                        why.append('retained_bytes_digest_mismatch')
                    # Prevent HTML/error pages masquerading as images by suffix/MIME.
                    valid = (data.startswith(b'\xff\xd8\xff') or data.startswith(b'\x89PNG\r\n\x1a\n')
                             or (data.startswith(b'RIFF') and data[8:12] == b'WEBP')
                             or data.startswith((b'GIF87a', b'GIF89a')))
                    if not valid:
                        why.append('retained_bytes_not_supported_image')
            if not why:
                eligible[eid] = e
        if not eligible:
            errors.append('saved_inspected_displayed_visual_proof_missing')
    if stage == 'accept' and policy.get('creator_acceptance_required', False):
        decided = stamp(decision.get('decided_at'))
        if decision.get('status') != 'accepted' or not decision.get('decision_source') or not decision.get('reason') or decided is None:
            errors.append('explicit_scoped_creator_acceptance_missing')
        refs = decision.get('evidence_refs', [])
        if required:
            if not refs or any(x not in eligible for x in refs):
                errors.append('acceptance_not_bound_to_valid_proof')
            elif decided is not None and any(decided < stamp(eligible[x]['displayed_at']) for x in refs):
                errors.append('acceptance_precedes_display')
        earlier_rejection = next((x for x in reversed(decisions[:-1]) if x.get('status') == 'rejected'), None)
        if earlier_rejection and decision.get('status') == 'accepted':
            if not decision.get('reconsideration_reason') or set(refs) == set(earlier_rejection.get('evidence_refs', [])):
                errors.append('rejection_requires_new_evidence_and_explicit_reconsideration')
    return {'passed': not errors, 'errors': errors, 'eligible_evidence': list(eligible),
            'scope': scope, 'stage': stage, 'enforcement': 'declared_evidence_only_not_pixel_judgment_or_host_interception'}


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--profile', required=True, type=Path)
    p.add_argument('--record', required=True, type=Path)
    p.add_argument('--stage', choices=['present', 'accept'], default='accept')
    p.add_argument('--scope', choices=['resource', 'opportunity'], default='resource')
    p.add_argument('--opportunity-id')
    p.add_argument('--asset-paths', type=Path, help='asset_id -> local file path; enables byte/hash checks')
    a = p.parse_args()
    result = check(json.loads(a.profile.read_text()), json.loads(a.record.read_text()), a.stage,
                   a.scope, a.opportunity_id, json.loads(a.asset_paths.read_text()) if a.asset_paths else None)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
