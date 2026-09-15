# T06 — SQL & Data Engineering Thinking

Mục tiêu: SQL từ cơ bản đến window/index và tư duy data quality, schema drift, scale, lineage, idempotency, leakage.

Schema dùng xuyên test:

```sql
users(user_id, tenant_id, created_at)
requests(request_id, user_id, config_version, success, latency_ms, cost_usd, created_at)
documents(document_id, tenant_id, version, checksum, status, updated_at)
eval_results(case_id, config_version, slice_name, passed, score, created_at)
```

## Part 1 — SQL foundation

Mode: `CLOSED_BOOK`  
Thời gian: 40 phút

### T06-P1-Q0 — MCQ calibration

Muốn giữ cả tenant chưa có request, starting table là `users` và join sang `requests`, loại join phù hợp nhất là:

A. INNER JOIN  
B. LEFT JOIN  
C. CROSS JOIN  
D. UNION

Chọn và giải thích.

### T06-P1-Q1 — Filter/order

Lấy 100 request lỗi mới nhất trong bảy ngày gần đây.

### T06-P1-Q2 — Aggregation

Theo từng ngày, tính total requests, successful requests, success rate và average latency.

### T06-P1-Q3 — GROUP BY/HAVING

Tìm `config_version` có ít nhất 100 requests và success rate dưới 90%.

### T06-P1-Q4 — NULL/CASE

`latency_ms` có thể NULL khi request bị reject trước provider. Giải thích `AVG` xử lý NULL thế nào và thiết kế metric tránh hiểu sai.

### T06-P1-Q5 — JOIN

Theo tenant, tính tổng request và cost. Bao gồm cả tenant có user nhưng chưa có request.

## Part 2 — Intermediate SQL

Mode: `DOCS_ALLOWED`  
Thời gian: 55 phút

### T06-P2-Q1 — CTE and baseline

So sánh success rate từng config với config `baseline` theo `slice_name`; chỉ dùng group có ít nhất 30 case mỗi phía.

### T06-P2-Q2 — Window function

Với mỗi user, lấy ba request gần nhất và delta latency so với request ngay trước đó.

### T06-P2-Q3 — Deduplication

`documents` bị duplicate theo `(tenant_id, document_id, version)`. Viết query xác định duplicate và chọn một record canonical theo `updated_at`, nhưng chưa xóa dữ liệu.

### T06-P2-Q4 — Running metric

Tính rolling 7-day success rate theo ngày và config. Nêu vấn đề khi volume mỗi ngày khác nhau.

### T06-P2-Q5 — UNION

Phân biệt `UNION` và `UNION ALL`; nêu tình huống data pipeline mà dùng sai làm mất hoặc nhân đôi thông tin.

## Part 3 — Performance and modeling

Mode: `DOCS_ALLOWED`  
Thời gian: 55 phút

### T06-P3-Q1 — Slow query

Query nhanh ở 100K rows nhưng chậm ở 10M. Lập kế hoạch dùng `EXPLAIN`, statistics, index, selectivity, partition và query rewrite. Không được kết luận “thêm index” trước evidence.

### T06-P3-Q2 — Index design

Workload thường lọc `tenant_id`, `created_at` và đôi khi `success`. Đề xuất index, thứ tự cột và trade-off write/storage.

### T06-P3-Q3 — Data model

Thiết kế schema versioned cho document → chunks → embeddings. Hỗ trợ update/delete/reindex/rollback và nhiều embedding model.

### T06-P3-Q4 — Transaction/idempotency

Metadata DB commit thành công nhưng vector index update thất bại. Đề xuất outbox/reconciliation/state machine; phân biệt exactly-once claim với idempotent processing.

## Part 4 — Data engineering simulation

Mode: `WORK_SIMULATION`  
Thời gian: 70 phút

### T06-P4-Q1 — Quality incident

Sau source schema drift, 8% document mất `tenant_id`, duplicate tăng và retrieval trả stale chunks. Tạo validation gates, quarantine, backfill và recovery checks.

### T06-P4-Q2 — Leakage

Feature/eval dataset chứa answer được sinh sau thời điểm prediction. Phân tích data leakage, ảnh hưởng metric và cách tạo split đúng theo time/entity.

### T06-P4-Q3 — SCD/history

Thiết kế lưu lịch sử policy document để trả lời “chính sách tại thời điểm X”. Chọn SCD/version strategy và query semantics.

### T06-P4-Q4 — Pipeline design

Thiết kế ingestion cho 1 triệu documents/ngày: source offsets, batching, retries, dedupe, DLQ, lineage, monitoring, backfill và cost. Nêu khi batch tốt hơn streaming.
