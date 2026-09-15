from __future__ import annotations

import unittest

from t07_debug_target import retry_operation, success_rate, tenant_cache_key


class SuccessRateTests(unittest.TestCase):
    def test_empty_is_zero(self) -> None:
        self.assertEqual(success_rate([]), 0.0)

    def test_ignores_invalid_labels(self) -> None:
        rows = [{"success": True}, {"success": "yes"}, {}]
        self.assertEqual(success_rate(rows), 1.0)


class RetryTests(unittest.TestCase):
    def test_does_not_retry_non_retryable_error(self) -> None:
        calls = 0

        def operation() -> str:
            nonlocal calls
            calls += 1
            raise ValueError("bad request")

        with self.assertRaises(ValueError):
            retry_operation(operation, max_attempts=3, retryable=(TimeoutError,))
        self.assertEqual(calls, 1)

    def test_never_exceeds_max_attempts(self) -> None:
        calls = 0

        def operation() -> str:
            nonlocal calls
            calls += 1
            raise TimeoutError("transient")

        with self.assertRaises(TimeoutError):
            retry_operation(operation, max_attempts=3, retryable=(TimeoutError,))
        self.assertEqual(calls, 3)


class CacheKeyTests(unittest.TestCase):
    def test_key_is_normalized_and_permission_scoped(self) -> None:
        first = tenant_cache_key("tenant-a", "user-1", " Policy ")
        same = tenant_cache_key("tenant-a", "user-1", "policy")
        other_tenant = tenant_cache_key("tenant-b", "user-1", "policy")
        other_user = tenant_cache_key("tenant-a", "user-2", "policy")
        self.assertEqual(first, same)
        self.assertNotEqual(first, other_tenant)
        self.assertNotEqual(first, other_user)


if __name__ == "__main__":
    unittest.main()
