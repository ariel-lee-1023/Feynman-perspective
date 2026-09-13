#!/usr/bin/env python3
"""Read-only 1.0 Candidate integrity check; no model calls or historical rescoring."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / 'transworld-identity'


def digest(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False)
    return 'sha256:' + hashlib.sha256(raw.encode()).hexdigest()


def load(name):
    return json.loads((EVIDENCE / name).read_text())


def check():
    status = load('validation.json')
    assert status['delivery_status'] == 'candidate', '1.0 was authorized as Candidate'
    assert status['gates'] == {'package': 'passed', 'source': 'passed', 'machine_recognition': 'not_run'}
    assert status['budget']['budget'] == status['budget']['consumed'] == 0
    assert status['budget']['calls'] == []
    assert not status['research']['assessed']
    assert not (ROOT / 'fidelity-ledger').exists(), 'duplicate live evidence tree'
    link = ROOT / '.agents/skills/feynman-perspective'
    assert link.is_symlink() and link.readlink().as_posix() == '../..'
    assert link.resolve() == ROOT
    assert list((ROOT / '.agents/skills').iterdir()) == [link]
    assert re.search(r'^name: feynman-perspective$', (ROOT / 'SKILL.md').read_text(), re.M)
    paths = [ROOT / 'SKILL.md'] + sorted(p for p in (ROOT / 'references').rglob('*') if p.is_file())
    runtime = {p.relative_to(ROOT).as_posix(): p.read_text() for p in paths}
    assert all(p.resolve().is_relative_to(ROOT / 'references') for p in paths[1:])
    assert digest(runtime) == status['runtime_hash'], 'runtime changed after source review'
    assert {p: digest(t) for p, t in runtime.items()} == status['module_hashes']
    assert not any(re.search(r'transworld-identity/|fidelity-ledger/', t) for t in runtime.values())
    mapping = load('applicability-1.0.json')
    for row in mapping['previous_results']:
        path = ROOT / row['current_path']
        assert path.resolve().is_relative_to(ROOT)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row['sha256'], row['current_path']
    for rel in mapping['runtime_preserved']:
        before = mapping['baseline']['runtime_files'][rel]
        assert 'sha256:' + hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == before, rel
    migrations = [json.loads(p.read_text()) for p in (EVIDENCE / 'migrations').glob('*.json')]
    migrated = {('fidelity-ledger/' + rel, sha) for m in migrations for rel, sha in m.get('files', {}).items() if sha != 'directory'}
    indexed = {(r['legacy_path'], r['sha256']) for r in mapping['previous_results']}
    assert migrated == indexed, 'migration index omits or alters historical records'
    evidence = {e['id']: e for e in load('evidence.json')['records']}
    for e in evidence.values():
        assert all(p in runtime for p in e['runtime_support'])
        assert all(i in evidence for i in e['conflicts'])
        assert all(e[k] for k in ['source', 'locator', 'attribution', 'group_id', 'situation', 'audience', 'available_information', 'constraints', 'observation'])
    review = load('source-review-1.0.json')
    assert review == status['source_review']
    assert review['reviewed_all_core_claims']
    for row in review['source_checks']:
        assert row['outcome'] == 'passed'
        assert row.get('implementation_safeguard') or row['evidence_ids']
        assert all(i in evidence for i in row['evidence_ids'])
        assert all(status['module_hashes'].get(p) == h for p, h in row['dependencies'].items())
    log = load('source-reading-log-1.0.json')
    assert log['actual_reading_units'] == len(log['records']) <= log['boundary']['reading_units']
    assert log['actual_ocr_pages'] == log['new_sources_acquired'] == 0
    profiles = load('recognition-profile-1.0.json')['profile']
    assert 3 <= len(profiles) <= 5
    assert all(set(p['scoring_anchors']) == set('01234') and all(i in evidence for i in p['evidence_ids']) for p in profiles)
    json_files = [p for p in ROOT.rglob('*.json') if '.git' not in p.parts]
    for p in json_files:
        json.loads(p.read_text())
    assert not any(p.is_file() and any(part in {'raw', 'corpus', 'private', '_work'} for part in p.relative_to(ROOT).parts) for p in ROOT.rglob('*') if '.git' not in p.parts)
    prohibited = {'.pdf', '.epub', '.docx', '.png', '.tiff', '.sqlite'}
    assert not any(p.is_file() and p.suffix.lower() in prohibited for p in ROOT.rglob('*') if '.git' not in p.parts)
    result = {'verdict': 'PASS', 'historical_files_verified': len(indexed), 'preserved_runtime_files': len(mapping['runtime_preserved']), 'evidence_records': len(evidence), 'source_checks': len(review['source_checks']), 'json_files_parsed': len(json_files), 'new_evaluation_calls': 0}
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    check()
