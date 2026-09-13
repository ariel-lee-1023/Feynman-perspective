#!/usr/bin/env python3
"""Read-only Candidate integrity check after structure revision 2; no model calls."""
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
    migration = load('structure-revision-2.json')
    assert status['structure_revision'] == migration['structure_revision'] == 2
    assert status['delivery_status'] == 'candidate'
    assert status['gates'] == {'package': 'passed', 'source': 'inconclusive', 'machine_recognition': 'not_run'}
    assert status['budget']['consumed'] == migration['evaluation_calls'] == 0
    assert status['budget']['calls'] == []
    assert not status['research']['assessed']
    assert not (ROOT / 'fidelity-ledger').exists()
    assert (EVIDENCE / 'scope.md').is_file()
    assert not (ROOT / 'references/scope.md').exists()
    link = ROOT / '.agents/skills/feynman-perspective'
    assert link.is_symlink() and link.readlink().as_posix() == '../..' and link.resolve() == ROOT
    assert list((ROOT / '.agents/skills').iterdir()) == [link]
    assert re.search(r'^name: feynman-perspective$', (ROOT / 'SKILL.md').read_text(), re.M)
    paths = [ROOT / 'SKILL.md'] + sorted(p for p in (ROOT / 'references').rglob('*') if p.is_file())
    assert all(p.resolve().is_relative_to(ROOT / 'references') for p in paths[1:])
    runtime = {p.relative_to(ROOT).as_posix(): p.read_text() for p in paths}
    assert digest(runtime) == status['runtime_hash'] == migration['runtime_hash']
    assert {p: digest(t) for p, t in runtime.items()} == status['module_hashes'] == migration['module_hashes']
    assert not any(re.search(r'transworld-identity/|fidelity-ledger/', t) for t in runtime.values())
    for row in migration['preserved_files']:
        p = ROOT / row['preserved_path']
        assert p.resolve().is_relative_to(ROOT)
        assert 'sha256:' + hashlib.sha256(p.read_bytes()).hexdigest() == row['sha256'], row['original_path']
    for record in (EVIDENCE / 'migrations').glob('scope-*.json'):
        data = json.loads(record.read_text())
        for rel, sha in data['after_hashes'].items():
            p = ROOT / rel
            assert ('sha256:' + hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None) == sha, rel
    evidence = {e['id']: e for e in load('evidence.json')['records']}
    for e in evidence.values():
        assert all(p in runtime for p in e['runtime_support'])
        assert all(i in evidence for i in e['conflicts'])
        assert all(e[k] for k in ['source', 'locator', 'attribution', 'group_id', 'situation', 'audience', 'available_information', 'constraints', 'observation'])
    # Original source review remains tied to its original inputs, not today's hashes.
    historical = load('history/structure-revision-2/transworld-identity/validation.json')
    review = load('source-review-1.0.json')
    assert historical['source_review'] == review and review['reviewed_all_core_claims']
    for row in review['source_checks']:
        assert row['outcome'] == 'passed'
        assert row.get('implementation_safeguard') or row['evidence_ids']
        assert all(i in evidence for i in row['evidence_ids'])
        assert all(historical['module_hashes'].get(p) == h for p, h in row['dependencies'].items())
    log = load('source-reading-log-1.0.json')
    assert log['actual_reading_units'] == len(log['records']) <= log['boundary']['reading_units']
    assert log['actual_ocr_pages'] == log['new_sources_acquired'] == 0
    profiles = load('recognition-profile-1.0.json')['profile']
    assert 3 <= len(profiles) <= 5
    assert all(set(p['scoring_anchors']) == set('01234') and all(i in evidence for i in p['evidence_ids']) for p in profiles)
    json_files = [p for p in ROOT.rglob('*.json') if '.git' not in p.parts]
    for p in json_files:
        json.loads(p.read_text())
    prohibited = {'.pdf', '.epub', '.docx', '.png', '.tiff', '.sqlite'}
    for p in ROOT.rglob('*'):
        if p.is_file() and '.git' not in p.parts:
            assert not any(part in {'raw', 'corpus', 'private', '_work'} for part in p.relative_to(ROOT).parts)
            assert p.suffix.lower() not in prohibited
    print(json.dumps({'verdict': 'PASS', 'original_files_verified': len(migration['preserved_files']), 'evidence_records': len(evidence), 'historical_source_checks': len(review['source_checks']), 'json_files_parsed': len(json_files), 'new_evaluation_calls': 0}, sort_keys=True))


if __name__ == '__main__':
    check()
