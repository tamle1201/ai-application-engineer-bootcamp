# T07 — Debugging

Mục tiêu: reproduce, observe, hypothesis, evidence, narrow, fix, verify và prevent regression trên syntax, logic, runtime, data, integration, performance, configuration, dependency và concurrency bugs.

## Part 1 — Basic bug identification

Mode: `CLOSED_BOOK`  
Thời gian: 40 phút

### T07-P1-Q0 — MCQ calibration

Khi nhận bug “thỉnh thoảng lỗi”, bước đầu tốt nhất thường là:

A. Viết lại module.  
B. Tái hiện và thu thập input/log/timestamp/environment.  
C. Thêm retry vô hạn.  
D. Đổi framework.

Chọn và giải thích.

### T07-P1-Q1 — Syntax/runtime

```python
def parse_amount(value)
    return float(value)
```

Liệt kê syntax bug, runtime/data risks và tests tối thiểu.

### T07-P1-Q2 — Logic

```python
def success_rate(rows):
    successes = sum(1 for row in rows if row["success"])
    return successes / len(rows) * 100
```

Tìm edge cases và semantic assumptions, không chỉ division by zero.

### T07-P1-Q3 — Data bug

Revenue tăng đột biến. Một source gửi `amount` theo cents, source khác theo dollars. Viết investigation plan và containment; không sửa dữ liệu trước khi xác định phạm vi.

### T07-P1-Q4 — Configuration

Local pass, production fail vì `MODEL_NAME` rỗng. Nêu cách reproduce, inspect config, validate startup và prevent regression.

### T07-P1-Q5 — Dependency

Deployment mới lỗi import dù code không đổi; lockfile và base image vừa đổi. Nêu evidence và bisect/rollback plan.

## Part 2 — Structured debugging

Mode: `DOCS_ALLOWED`  
Thời gian: 50 phút

Executable debugging target: `../practical/t07_debug_target.py` và public tests tương ứng.

### T07-P2-Q1 — API timeout

5% call timeout, tập trung ở payload lớn. Thiết kế log/trace, controlled experiment và hypothesis. Phân biệt client timeout, server timeout, queue wait và network.

### T07-P2-Q2 — Non-deterministic test

Test pass local nhưng fail CI 1/20 lần. Có shared temp file và phụ thuộc clock. Nêu cách tái hiện, cô lập và sửa flakiness mà không chỉ tăng retry test.

### T07-P2-Q3 — Cache bug

User A đôi khi thấy answer của User B. Cache key hiện chỉ là normalized query. Xác định severity, containment, root cause areas và tests. Không giới hạn điều tra ở cache nếu chưa đủ evidence.

### T07-P2-Q4 — Fix verification

Sau khi sửa bug, “chạy lại một lần thấy đúng” có đủ không? Tạo verification matrix gồm regression, negative, load và rollback validation.

## Part 3 — Performance and concurrency

Mode: `DOCS_ALLOWED`  
Thời gian: 55 phút

### T07-P3-Q1 — Performance

CPU thấp nhưng p95 cao, queue depth tăng, external model latency ổn định. Lập hypothesis về connection pool, lock, worker starvation và backpressure; chọn measurement.

### T07-P3-Q2 — Race condition

Hai worker xử lý cùng event và tạo hai refund. Thiết kế reproduction, idempotency/locking/unique constraint và test concurrency.

### T07-P3-Q3 — Async cancellation

Client disconnect nhưng task gọi model/tool vẫn chạy và tạo side effect. Phân tích cancellation propagation, shield/background job và ownership.

### T07-P3-Q4 — Memory leak

Memory tăng chậm theo traffic; restart tạm giải quyết. Nêu profiling plan, suspected objects, load reproduction và cách xác nhận fix.

## Part 4 — Production incident simulation

Mode: `WORK_SIMULATION`  
Thời gian: 65 phút

Sau release:

- error rate 1% → 12%;
- chỉ tenant lớn bị ảnh hưởng;
- database connections đạt max;
- model provider healthy;
- retry volume tăng 4 lần;
- một thay đổi mới bỏ connection timeout.

Thực hiện:

1. severity/impact assessment;
2. timeline và evidence table;
3. ranked hypothesis tree;
4. năm kiểm tra đầu;
5. containment/rollback decision;
6. recovery criteria;
7. regression tests;
8. stakeholder update tối đa 150 từ;
9. postmortem actions theo prevention/detection/mitigation.
