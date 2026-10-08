#!/usr/bin/env python3
"""Validate supplied records; cannot authenticate approval or live service state."""
import argparse, hashlib, json, re
from datetime import date
from decimal import Decimal

def digest(snapshot):
    return hashlib.sha256(json.dumps(snapshot,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()

def validate(package, export=False):
    s=package['snapshot']
    assert re.fullmatch(r'\d{4}-(0[1-9]|1[0-2])',s['month']), 'invalid month'
    assert s['hospital_id'], 'missing hospital'
    assert isinstance(s['revision'],int) and s['revision']>0, 'invalid revision'
    assert package['snapshot_sha256']==digest(s), 'digest mismatch'
    assert not s.get('unresolved'), 'unresolved questions'
    assert s.get('source_coverage_complete') is True, 'source coverage incomplete'
    assert not s.get('formula_errors'), 'formula errors'
    a={k:Decimal(str(s['totals'][k])) for k in ['opening','income','expenses','closing']}
    assert all(v.is_finite() for v in a.values()), 'nonfinite amount'
    assert a['opening']+a['income']-a['expenses']==a['closing'], 'cash reconciliation'
    ids=set()
    for r in s['transactions']:
        assert r['id'] not in ids, 'duplicate transaction'
        ids.add(r['id'])
        assert r.get('source_ref') and r.get('reporting_currency')==s['currency'], 'source/currency missing'
        if r.get('included'):
            assert r.get('confirmed') is True, 'unconfirmed included transaction'
            parsed=date.fromisoformat(r['reporting_date'])
            assert parsed.strftime('%Y-%m')==s['month'], 'out-of-period transaction'
            if r.get('original_currency')!=s['currency']:
                assert r.get('conversion_source_ref'), 'unconfirmed currency conversion'
            assert Decimal(str(r['reporting_amount'])).is_finite(), 'invalid amount'
            assert r['kind'] in ['income','expense'], 'invalid kind'
    for kind,total in [('income',a['income']),('expense',a['expenses'])]:
        actual=sum((Decimal(str(r['reporting_amount'])) for r in s['transactions'] if r.get('included') and r['kind']==kind),Decimal(0))
        assert actual==total, f'{kind} ledger mismatch'
    if export:
        for key in ['approval','export_request']:
            r=package.get(key,{})
            assert r.get('instruction_ref') and r.get('observed_at'), f'missing {key} evidence'
            assert r.get('snapshot_sha256')==package['snapshot_sha256'], f'stale {key}'
            assert r.get('month')==s['month'] and r.get('hospital_id')==s['hospital_id'], f'wrong {key} scope'
    return {'snapshot_sha256':package['snapshot_sha256'],'export_gate_checked':export,'record_validation':'passed','live_authority_authenticated':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('package');p.add_argument('--export',action='store_true');args=p.parse_args()
    with open(args.package) as f: package=json.load(f)
    print(json.dumps(validate(package,args.export)))
