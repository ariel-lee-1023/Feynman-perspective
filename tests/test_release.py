"""Exercise live integrity, immutable history and legitimate document maintenance."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'persona'
        shutil.copytree(ROOT, self.root, symlinks=True,
                        ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def check_release(self):
        return subprocess.run([sys.executable, '-B', str(self.root / 'scripts/check_release.py')],
                              capture_output=True, text=True)

    def test_reviewed_runtime_passes_without_new_assessment(self):
        result = self.check_release()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report['new_evaluation_calls'], 0)
        self.assertEqual(report['original_files_verified'], 182)

    def test_unreviewed_runtime_edit_fails(self):
        path = self.root / 'references/voice.md'
        path.write_text(path.read_text() + '\nUnexpected change.\n')
        result = self.check_release()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('current runtime hash changed', result.stderr)

    def test_preserved_document_corruption_fails(self):
        path = self.root / 'transworld-identity/history/ci-repair-2026-10-31/preserved/CHANGELOG.md.txt'
        path.write_text(path.read_text() + '\nCorrupted history.\n')
        result = self.check_release()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('CHANGELOG.md', result.stderr)

    def test_migration_content_corruption_fails(self):
        path = next((self.root / 'transworld-identity/migrations').glob('scope-*.json'))
        data = json.loads(path.read_text())
        data['changes'][0]['content'] += '\nCorrupted migration.\n'
        path.write_text(json.dumps(data))
        result = self.check_release()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('historical migration content changed', result.stderr)

    def test_historical_validation_corruption_fails(self):
        path = self.root / 'transworld-identity/history/ci-repair-2026-10-31/validation.json'
        data = json.loads(path.read_text())
        data['runtime_hash'] = 'sha256:corrupted'
        path.write_text(json.dumps(data))
        self.assertNotEqual(self.check_release().returncode, 0)

    def test_unresolved_evidence_support_fails(self):
        path = self.root / 'transworld-identity/evidence.json'
        data = json.loads(path.read_text())
        data['records'][0]['runtime_support'].append('references/missing.md')
        path.write_text(json.dumps(data))
        self.assertNotEqual(self.check_release().returncode, 0)

    def test_current_document_edits_do_not_rewrite_migration(self):
        for rel in ['README.md', 'CHANGELOG.md', 'transworld-identity/provenance.md']:
            path = self.root / rel
            path.write_text(path.read_text() + '\nEditorial clarification.\n')
        result = self.check_release()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
