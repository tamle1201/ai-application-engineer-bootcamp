from __future__ import annotations

import math
import unittest

from t10_rag_starter import Chunk, build_context_pack


class ContextPackTests(unittest.TestCase):
    def test_enforces_tenant_and_document_acl(self) -> None:
        candidates = [
            Chunk("a", "allowed", "1", "safe", 0.5),
            Chunk("b", "allowed", "2", "cross tenant", 1.0),
            Chunk("a", "secret", "3", "not allowed", 0.9),
        ]
        pack = build_context_pack(
            candidates,
            tenant_id="a",
            allowed_document_ids=frozenset({"allowed"}),
            max_context_chars=100,
            top_k=5,
        )
        self.assertEqual([chunk.text for chunk in pack.chunks], ["safe"])
        self.assertEqual(pack.citations, ("allowed#1",))

    def test_deduplicates_and_orders_deterministically(self) -> None:
        candidates = [
            Chunk("t", "b", "1", "b", 0.8),
            Chunk("t", "a", "1", "z", 0.8),
            Chunk("t", "a", "1", "a", 0.8),
            Chunk("t", "c", "1", "c", 0.9),
        ]
        pack = build_context_pack(
            candidates,
            tenant_id="t",
            allowed_document_ids=frozenset({"a", "b", "c"}),
            max_context_chars=100,
            top_k=5,
        )
        self.assertEqual(
            [(chunk.document_id, chunk.text) for chunk in pack.chunks],
            [("c", "c"), ("a", "a"), ("b", "b")],
        )

    def test_skips_invalid_and_oversized_then_continues(self) -> None:
        candidates = [
            Chunk("t", "a", "nan", "bad", math.nan),
            Chunk("t", "a", "big", "x" * 20, 0.9),
            Chunk("t", "a", "small", "small", 0.8),
        ]
        pack = build_context_pack(
            candidates,
            tenant_id="t",
            allowed_document_ids=frozenset({"a"}),
            max_context_chars=5,
            top_k=2,
        )
        self.assertEqual([chunk.chunk_id for chunk in pack.chunks], ["small"])
        self.assertEqual(pack.used_chars, 5)

    def test_rejects_invalid_boundaries(self) -> None:
        with self.assertRaises(ValueError):
            build_context_pack(
                [],
                tenant_id="",
                allowed_document_ids=frozenset(),
                max_context_chars=100,
                top_k=1,
            )


if __name__ == "__main__":
    unittest.main()

