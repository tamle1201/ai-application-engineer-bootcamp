# T08 — Testing, Code Quality & Reliability

Mục tiêu: test strategy, review, refactor, maintainability, testability, negative cases và reliability engineering.

## Part 1 — Testing foundation

Mode: `CLOSED_BOOK`  
Thời gian: 40 phút

### T08-P1-Q0 — MCQ calibration

Test nào phù hợp nhất để kiểm tra nhiều component thật hoạt động cùng nhau qua public API?

A. Unit test.  
B. End-to-end test.  
C. Linter.  
D. Type annotation.

Chọn và nêu trade-off.

### T08-P1-Q1 — Test levels

Phân biệt unit, integration, end-to-end và regression test cho một `/ask` API. Nêu bug mỗi loại bắt tốt nhất.

### T08-P1-Q2 — Test cases

Cho `parse_user(payload)` cần `id`, `email`, `age >= 18`. Liệt kê equivalence classes, boundaries và negative cases; không cần code.

### T08-P1-Q3 — Mock/fake

Khi nào mock model API có ích, khi nào làm test quá gắn implementation? So sánh mock, fake và sandbox integration.

### T08-P1-Q4 — Determinism

Test phụ thuộc current time, random và network. Thiết kế dependency injection để deterministic.

### T08-P1-Q5 — Coverage

Coverage 95% có chứng minh phần mềm tốt không? Đưa hai ví dụ coverage cao nhưng bug nghiêm trọng vẫn lọt.

## Part 2 — Code review

Mode: `CLOSED_BOOK`  
Thời gian: 50 phút

Review code:

```python
def process(data, client, db):
    for x in data:
        try:
            y = client.call(str(x))
            db.save(y)
        except Exception:
            print("failed")
    return True
```

### T08-P2-Q1

Tìm correctness bugs, hidden contract và failure semantics.

### T08-P2-Q2

Đánh giá readability, naming, cohesion, observability và testability.

### T08-P2-Q3

Đề xuất refactor nhỏ nhất có giá trị; không được biến thành framework lớn.

### T08-P2-Q4

Viết test plan gồm happy, invalid input, partial failure, duplicate, timeout, DB failure và retry/idempotency interaction.

## Part 3 — Reliability

Mode: `DOCS_ALLOWED`  
Thời gian: 55 phút

### T08-P3-Q1 — SLI/SLO

Đề xuất SLI/SLO cho availability, p95 latency, task success và harmful output. Phân biệt metric với target.

### T08-P3-Q2 — Retry/fallback

Thiết kế retry matrix theo HTTP/network errors, backoff/jitter, retry budget, circuit breaker và fallback. Nêu retry storm risk.

### T08-P3-Q3 — CI gate

Thiết kế CI cho AI service: lint/type/unit/integration/eval/security/build. Cái gì chạy mỗi commit, nightly và pre-release?

### T08-P3-Q4 — Canary/rollback

Prompt/model/index version mới cải thiện offline score nhưng chưa có production evidence. Thiết kế canary, guardrails và rollback criteria.

## Part 4 — Test architecture challenge

Mode: `WORK_SIMULATION`  
Thời gian: 65 phút

Hệ thống gồm ingestion, retrieval, LLM, tools và API. Hãy tạo test matrix theo:

- component;
- test level;
- normal/edge/adversarial/failure;
- deterministic vs model-based grader;
- environment;
- frequency;
- owner;
- release gate.

Bắt buộc bao phủ:

- stale/duplicate document;
- retrieval miss;
- hallucination/no-answer;
- invalid structured output;
- prompt injection;
- cross-tenant leakage;
- tool timeout/duplicate side effect;
- provider outage;
- latency/cost regression;
- rollback.

Sau đó chọn mười test ROI cao nhất cho MVP hai tuần và giải thích phần bị hoãn.
