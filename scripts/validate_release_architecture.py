#!/usr/bin/env python3
"""Regression probes for release fanout, revision reuse and fail-closed audits."""
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone, timedelta
from pathlib import Path
from publication_audit import plan, verify, close, digest, MANIFEST, POINTER
from publication import request

ROOT = Path(__file__).resolve().parents[1]


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now(timezone.utc)
        old = {f'skills/domain/references/{i}.md': digest(str(i).encode()) for i in range(500)}
        old['VERSION'] = digest(b'1.0.0\n')
        new = {**old, 'skills/domain/references/0.md': digest(b'changed'), 'VERSION': digest(b'1.0.1\n')}
        encode = lambda files, v: json.dumps(dict(schema_version=1, algorithm='sha256', core_version=v, files=files)).encode()
        self.before, self.after = encode(old, '1.0.0'), encode(new, '1.0.1')
        self.metadata = {p: dict(library_file_id='libfile_'+str(i), version_id='1', file_id='bytes_'+str(i), modified_at='observed') for i, p in enumerate(set(new) | {MANIFEST, POINTER})}
        self.baseline = dict(schema_version=1, status='verified', release_sha256=digest(self.before), full_audit_at=self.now.isoformat(), entries={p: {**self.metadata[p], 'sha256': h} for p, h in old.items()})

        self.baseline['entries'][MANIFEST] = {**self.metadata[MANIFEST], 'sha256': digest(self.before)}
        self.baseline['entries'][POINTER] = {**self.metadata[POINTER], 'sha256': digest(b'prior-pointer')}

    def planned(self, **kw):
        return plan(self.before, self.after, self.baseline, self.metadata, now=self.now, **kw)

    def verified(self, audit=None):
        a = audit or self.planned()
        reads = {p: {**self.metadata[p], 'sha256': a['expected_hashes'][p]} for p in a['read_paths']}
        return verify(a, reads, self.metadata)

    def test_sparse_500_file_update(self):
        a = self.planned()
        self.assertEqual(len(a['read_paths']), 3)  # domain source + VERSION + manifest
        self.assertEqual(len(a['reuse']), 499)
        self.assertEqual(self.verified(a)['status'], 'sources_verified_pointer_pending')

    def test_null_revision_requires_bytes(self):
        self.metadata['skills/domain/references/1.md']['version_id'] = None
        self.assertIn('skills/domain/references/1.md', self.planned()['read_paths'])

    def test_revision_changed_requires_bytes(self):
        self.metadata['skills/domain/references/1.md']['version_id'] = '2'
        self.assertIn('skills/domain/references/1.md', self.planned()['read_paths'])

    def test_identity_changed_requires_bytes(self):
        self.metadata['skills/domain/references/1.md']['library_file_id'] = 'replacement'
        self.assertIn('skills/domain/references/1.md', self.planned()['read_paths'])

    def test_wrong_baseline_release_full(self):
        self.baseline['release_sha256'] = 'a'*64
        self.assertEqual(self.planned()['mode'], 'full')

    def test_expired_baseline_full(self):
        self.baseline['full_audit_at'] = (self.now-timedelta(days=8)).isoformat()
        self.assertEqual(self.planned()['mode'], 'full')

    def test_incremental_does_not_reset_full_clock(self):
        self.baseline['full_audit_at'] = (self.now-timedelta(days=6)).isoformat()
        self.assertEqual(self.verified()['full_audit_at'], self.baseline['full_audit_at'])

    def test_explicit_full(self):
        a=self.planned(mode='full')
        self.assertEqual(len(a['reuse']), 0)
        self.assertEqual(len(a['read_paths']), 502)

    def test_structural_change_full(self):
        d=json.loads(self.after);d['files']['kernel/boot.yaml']=digest(b'contract');self.after=json.dumps(d).encode()
        self.metadata['kernel/boot.yaml']=dict(library_file_id='libfile_new',version_id='1')
        self.assertEqual(self.planned()['mode'], 'full')

    def test_extra_inventory_rejected(self):
        self.metadata['extra.md']=dict(library_file_id='libfile_extra')
        with self.assertRaises(ValueError): self.planned()

    def test_duplicate_identity_rejected(self):
        paths=list(self.metadata);self.metadata[paths[1]]['library_file_id']=self.metadata[paths[0]]['library_file_id']
        with self.assertRaises(ValueError): self.planned()

    def test_missing_readback_rejected(self):
        with self.assertRaises(ValueError): verify(self.planned(), {}, self.metadata)

    def test_metadata_race_rejected(self):
        a=self.planned();self.metadata=copy.deepcopy(self.metadata);self.metadata['skills/domain/references/1.md']['modified_at']='changed'
        with self.assertRaises(ValueError): self.verified(a)

    def test_bad_bytes_rejected(self):
        a=self.planned();reads={p:{**self.metadata[p],'sha256':'0'*64} for p in a['read_paths']}
        with self.assertRaises(ValueError): verify(a,reads,self.metadata)

    def test_pointer_close_and_post_activation_drift(self):
        report=self.verified();raw=json.dumps(dict(schema_version=1,core_version='1.0.1',release_manifest=MANIFEST,release_sha256=digest(self.after))).encode()
        self.assertEqual(close(report,raw,self.metadata[POINTER],self.metadata)['status'],'verified')
        bad=copy.deepcopy(self.metadata);bad['VERSION']['version_id']='3'
        with self.assertRaises(ValueError): close(report,raw,self.metadata[POINTER],bad)
        pointer=json.loads(raw);pointer['core_version']='9.0.0'
        with self.assertRaises(ValueError): close(report,json.dumps(pointer).encode(),self.metadata[POINTER],self.metadata)

    def test_pointer_request_requires_source_audit(self):
        with tempfile.TemporaryDirectory() as d:
            m=Path(d)/'release.json';m.write_bytes(self.after)
            p=Path(d)/'pointer.json';p.write_bytes(b'pointer')
            entries=[dict(path=MANIFEST, library_file_id='manifest',prior_sha256=digest(self.before),candidate_sha256=digest(self.after),candidate_path=str(m)),dict(path=POINTER,library_file_id='pointer',prior_sha256=digest(b'old'),candidate_sha256=digest(b'pointer'),candidate_path=str(p))]
            j=dict(schema_version=2,ordered_write_set=entries,outcomes=[])
            snap={MANIFEST:dict(library_file_id='manifest',version_id='2',sha256=digest(self.after)),POINTER:dict(library_file_id='pointer',version_id='1',sha256=digest(b'old'))}
            with self.assertRaises(ValueError): request(j,snap,'pointer')
            j['source_audit']=self.verified()
            self.assertEqual(len(request(j,snap,'pointer')['uploads']),1)
            j['source_audit']['entries'].pop('VERSION')
            with self.assertRaises(ValueError): request(j,snap,'pointer')


class ReleaseFanoutTests(unittest.TestCase):
    def test_release_bump_leaves_contracts_and_checkpoints_unchanged(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'core';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
            files=json.loads((root/'core-files.json').read_text())['files'];before={p:digest((root/p).read_bytes()) for p in files}
            (root/'VERSION').write_text('0.42.1\n')
            subprocess.run([sys.executable,str(root/'scripts/build_release_manifest.py')],check=True,capture_output=True)
            changed={p for p in files if digest((root/p).read_bytes())!=before[p]}
            self.assertEqual(changed,{'VERSION',MANIFEST,POINTER})
            for script in ['validators/validate_core.py','scripts/validate_runtime_contracts.py','scripts/validate_library_authority.py','scripts/validate_youtube_publishing_hardening.py']:
                result=subprocess.run([sys.executable,str(root/script)],capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stdout+result.stderr)


if __name__ == '__main__':
    unittest.main()
