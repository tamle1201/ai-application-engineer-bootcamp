from __future__ import annotations

import copy
import unittest

from t03_programming_starter import normalize_records


class NormalizeRecordsTests(unittest.TestCase):
    def test_normalizes_valid_records_and_preserves_order(self) -> None:
        records = [{"id": " a ", "text": " first "}, {"id": "b", "text": "second"}]
        valid, errors = normalize_records(records)
        self.assertEqual(valid, [{"id": "a", "text": "first"}, {"id": "b", "text": "second"}])
        self.assertEqual(errors, [])

    def test_collects_errors_without_stopping_batch(self) -> None:
        records = [{"id": "", "text": "x"}, {"id": "ok", "text": "value"}, {"text": "missing id"}]
        valid, errors = normalize_records(records)
        self.assertEqual(valid, [{"id": "ok", "text": "value"}])
        self.assertEqual([error["index"] for error in errors], [0, 2])

    def test_rejects_duplicate_after_normalization(self) -> None:
        valid, errors = normalize_records([{"id": "A", "text": "one"}, {"id": " A ", "text": "two"}])
        self.assertEqual(valid, [{"id": "A", "text": "one"}])
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0]["index"], 1)

    def test_rejects_wrong_types(self) -> None:
        valid, errors = normalize_records([{"id": 1, "text": "x"}, {"id": "x", "text": None}])
        self.assertEqual(valid, [])
        self.assertEqual(len(errors), 2)

    def test_does_not_mutate_input(self) -> None:
        records = [{"id": " a ", "text": " x ", "extra": {"nested": True}}]
        before = copy.deepcopy(records)
        normalize_records(records)
        self.assertEqual(records, before)


if __name__ == "__main__":
    unittest.main()

