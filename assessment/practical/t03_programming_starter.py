"""T03 practical starter. Candidate implements normalize_records."""

from __future__ import annotations


def normalize_records(records: list[dict[str, object]]) -> tuple[list[dict[str, str]], list[dict[str, object]]]:
    """Normalize records without mutating input.

    Rules:
    - id/text must be strings and non-blank after strip;
    - duplicate normalized IDs are rejected;
    - valid output contains only stripped id/text;
    - errors contain input index and a stable reason string;
    - preserve input order and continue after record errors.
    """

    raise NotImplementedError("Implement normalize_records")

