#!/usr/bin/env python3
from copy import deepcopy
from visual_execution_check import check

base = {'mode': 'group', 'requested_assets': 1, 'format': 'standalone',
        'subjects': [{'slot': 'A', 'identity': 'canonical', 'instances': 1, 'required_pixel_roles': ['face', 'body']},
                     {'slot': 'B', 'identity': 'peer', 'instances': 1, 'required_pixel_roles': []}],
        'bindings': [{'subject': 'A', 'role': role, 'source_id': role, 'actual_input': role + '.png', 'status': 'bound'} for role in ['face', 'body']]}
assert check(base)['pixel_truth'] == 'unverified'
mutations = [lambda r: r['subjects'][1].update(identity='canonical'),
             lambda r: r['subjects'][0].update(instances=2),
             lambda r: r['subjects'][1].update(slot='A'),
             lambda r: r['bindings'].pop(),
             lambda r: r['bindings'][0].update(status='unbound'),
             lambda r: r['bindings'][0].pop('actual_input'),
             lambda r: r['bindings'][0].update(subject='unknown'),
             lambda r: r.update(requested_assets=True),
             lambda r: r.update(format='collage'),
             lambda r: r.update(mode='edit')]
for mutate in mutations:
    record = deepcopy(base); mutate(record)
    try:
        check(record)
    except ValueError:
        continue
    raise AssertionError('bad visual contract accepted')
edit = {**base, 'mode': 'edit', 'base_input': 'accepted.png', 'change': ['hair'], 'preserve': ['face', 'physique']}
assert check(edit)['coverage'] == 'declared_inputs_complete'
print('VISUAL INPUT COVERAGE: PASS group/edit positives and ten negative cases; pixels remain unverified')
