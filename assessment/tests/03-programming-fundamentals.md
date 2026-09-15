# T03 — Programming Fundamentals

Mục tiêu: Python fundamentals, data types, scope, functions, references, collections, exceptions, file/JSON, APIs, environment, dependencies, concurrency, async và code quality.

## Part 1 — Reading and fundamentals

Mode: `CLOSED_BOOK`  
Thời gian: 35 phút

### T03-P1-Q0 — MCQ calibration

Trong Python, annotation `price: float`:

A. Luôn tự động từ chối string khi runtime.  
B. Là metadata/type-hint; muốn chặn input sai vẫn cần validation phù hợp.  
C. Tự chuyển mọi string thành float.  
D. Chỉ hoạt động trong class.

Chọn và giải thích.

### T03-P1-Q1 — Values and references

Không chạy code. Cho output và giải thích:

```python
a = [1, 2]
b = a
c = a.copy()
b.append(3)
c.append(4)
print(a, b, c)
```

### T03-P1-Q2 — Scope

Phân tích lỗi/behavior:

```python
count = 10

def increment():
    count += 1
    return count
```

Nêu hai cách sửa và trade-off.

### T03-P1-Q3 — Mutable default

Dự đoán hai lần gọi và sửa:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

### T03-P1-Q4 — Exceptions

Phân biệt `ValueError`, `TypeError`, trả `None` và custom exception trong một parser. Khi nào dùng mỗi cách?

### T03-P1-Q5 — JSON/serialization

JSON có biểu diễn trực tiếp `datetime`, `Decimal`, `set` không? Đề xuất contract serialization có thể round-trip và xử lý timezone/money.

### T03-P1-Q6 — Environment

Giải thích vai trò của virtual environment, dependency lock/version constraint, environment variable và secret. Nêu một lỗi production nếu hiểu sai mỗi mục.

## Part 2 — Implementation

Mode: `DOCS_ALLOWED`  
Thời gian: 70 phút

Executable starter tùy chọn: `../practical/t03_programming_starter.py` và public tests tương ứng.

### T03-P2-Q1 — Batch normalization

Viết:

```python
def normalize_records(records: list[dict]) -> tuple[list[dict], list[dict]]:
    ...
```

Contract:

- `id` và `text` là string không rỗng sau strip;
- ID không trùng;
- valid output chỉ giữ `id`, `text` đã normalize;
- errors là `{index, reason}`;
- không mutate input; giữ thứ tự; một record lỗi không dừng batch.

Viết tối thiểu sáu tests.

### T03-P2-Q2 — File ingestion

Viết iterator đọc JSON Lines mà không load toàn bộ file. Phân biệt lỗi file-level và record-level. Nêu cách đảm bảo file được đóng khi lỗi.

### T03-P2-Q3 — Refactor

Refactor hàm 60 dòng đang vừa validate, transform, gọi API, ghi DB và log. Không cần code đầy đủ; đưa interface/function boundaries và error ownership.

## Part 3 — API and concurrency

Mode: `DOCS_ALLOWED`  
Thời gian: 65 phút

### T03-P3-Q1 — HTTP client

Thiết kế hàm gọi API có timeout, retry/backoff cho lỗi phù hợp, request ID và error taxonomy. Giải thích 400, 401, 403, 404, 409, 429, 500, 503 và network timeout.

### T03-P3-Q2 — Async review

Review:

```python
async def enrich(rows, client):
    result = []
    for row in rows:
        try:
            value = await client.generate(row["text"])
        except Exception:
            value = await client.generate(row["text"])
        result.append({"id": row["id"], "value": value})
    return result
```

Tìm vấn đề về concurrency, timeout, retry, cancellation, partial failure, ordering, idempotency và observability. Đề xuất pseudocode.

### T03-P3-Q3 — Backpressure

Bạn có 100.000 rows, provider chỉ cho 50 request/s và tối đa 20 concurrent connections. Thiết kế batching/queue/rate limit; nêu memory và retry risk.

## Part 4 — Adaptive coding challenge

Mode: `DOCS_ALLOWED`  
Thời gian: 70 phút  
Người chấm chọn một trong hai.

### Option A — Event aggregator

Implement module tổng hợp events theo UTC date, reject timestamp naive/invalid, dedupe event ID, dùng `Decimal` cho money, output deterministic và thu thập record errors.

### Option B — Resilient provider client

Implement provider abstraction với fake client, timeout, bounded retry, idempotency key, structured result/error và tests cho success, 429, timeout, invalid response, cancellation.

Nộp source, tests, commands/output thật, complexity và known limitations.
