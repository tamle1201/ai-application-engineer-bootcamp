"""T07 debugging target. This file contains intentional defects."""

from __future__ import annotations

from collections.abc import Callable, Sequence


def success_rate(rows: Sequence[dict[str, object]]) -> float:
    """Return successful rows divided by valid boolean-labeled rows.

    Empty input returns 0.0. Rows with non-boolean/missing success are ignored.
    """

    successes = sum(1 for row in rows if row.get("success"))
    return successes / len(rows)


def retry_operation(
    operation: Callable[[], str],
    *,
    max_attempts: int,
    retryable: tuple[type[Exception], ...],
) -> str:
    """Run operation at most max_attempts and retry only retryable errors."""

    attempts = 0
    while attempts <= max_attempts:
        try:
            return operation()
        except Exception:
            attempts += 1
    return ""


def tenant_cache_key(tenant_id: str, user_id: str, query: str) -> str:
    """Build a stable cache key scoped by tenant, user, and normalized query."""

    return query.strip().lower()

