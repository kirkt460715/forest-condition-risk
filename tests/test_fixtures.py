import csv
import json
import unittest
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "data"


class FixtureContractTests(unittest.TestCase):
    def test_declared_sources_have_headers_and_records(self):
        manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
        for filename, columns in manifest["sources"].items():
            with self.subTest(source=filename):
                with (DATA / filename).open(encoding="utf-8", newline="") as source:
                    reader = csv.DictReader(source)
                    self.assertEqual(reader.fieldnames, columns)
                    rows = list(reader)
                    self.assertTrue(rows)
                    for row in rows:
                        self.assertNotIn(None, row)
                        self.assertNotIn(None, row.values())

    def records(self, filename):
        with (DATA / filename).open(encoding="utf-8", newline="") as source:
            return list(csv.DictReader(source))

    def test_history_contains_multiple_seasons_and_unobserved_visits(self):
        history = self.records("historical_seasons.csv")
        self.assertGreaterEqual(len({row["year"] for row in history}), 5)
        self.assertEqual({row["season"] for row in history}, {"春", "夏", "秋"})
        self.assertEqual(len({row["sensor"] for row in history}), 2)
        self.assertTrue(any(row["visit_basis"] == "未访问" and not row["verification"] for row in history))
        self.assertTrue(any(row["verification_received"].startswith("2026") for row in history))


if __name__ == "__main__":
    unittest.main()
