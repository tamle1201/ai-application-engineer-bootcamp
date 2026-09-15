# Executable Practical Pack

Các file này dùng cho T03, T07 và T10. Các lệnh bên dưới giả định terminal đang ở thư mục `ai-application-engineer-roadmap`. Không dùng chung một lệnh chạy tất cả trong lúc thi; chỉ chạy target của Part hiện tại.

## T03 — Batch normalization

Sửa `t03_programming_starter.py`, không sửa/xóa public tests.

```bash
cd assessment/practical
python -m unittest test_t03_programming -v
```

## T07 — Debugging target

`t07_debug_target.py` có bug cố ý. Trước khi sửa, ghi hypothesis và predicted failing tests. Sau đó sửa source, không làm yếu test.

```bash
cd assessment/practical
python -m unittest test_t07_debug_target -v
```

## T10 — Secure context pack

Sửa `t10_rag_starter.py`, không sửa/xóa public tests.

```bash
cd assessment/practical
python -m unittest test_t10_rag -v
```

## Evidence bắt buộc

- start/end time;
- files changed;
- tests added;
- commands và output thật;
- assumptions;
- tests còn fail;
- complexity;
- known limitations.

Starter code cố ý làm tests fail trước khi candidate thực hiện. Syntax/collection failure do đề là blocker; assertion/NotImplemented failure là trạng thái baseline dự kiến.

Baseline đã xác nhận khi phát hành:

| Target | Số test | Trạng thái ban đầu dự kiến |
|---|---:|---|
| T03 | 5 | 5 errors tại `NotImplementedError` |
| T07 | 5 | 4 failures + 1 error do bug chủ đích |
| T10 | 4 | 4 errors tại `NotImplementedError` |
