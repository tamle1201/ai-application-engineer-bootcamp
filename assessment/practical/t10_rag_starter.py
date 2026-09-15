"""T10 secure RAG context-selection starter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True, slots=True)
class Chunk:
    tenant_id: str
    document_id: str
    chunk_id: str
    text: str
    score: float


@dataclass(frozen=True, slots=True)
class ContextPack:
    chunks: tuple[Chunk, ...]
    citations: tuple[str, ...]
    used_chars: int


def build_context_pack(
    candidates: Sequence[Chunk],
    *,
    tenant_id: str,
    allowed_document_ids: frozenset[str],
    max_context_chars: int,
    top_k: int,
) -> ContextPack:
    """Build deterministic context after fail-closed tenant/ACL filtering.

    Ignore blank identity/text, negative/non-finite score, other tenants, and
    documents outside the allowlist. Deduplicate by document/chunk identity,
    keeping the highest score; equal-score conflicts use lexicographically lower
    text. Sort score descending then identity ascending. Greedily select complete
    chunks; skip oversized candidates and continue to later smaller chunks.
    Citations are '<document_id>#<chunk_id>'. Invalid request boundaries raise
    ValueError. Do not mutate input.
    """

    raise NotImplementedError("Implement build_context_pack")

