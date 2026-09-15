# T11 — AI System Design

Mục tiêu: requirements, estimates, architecture, data flow, APIs, storage, retrieval, model, caching, auth, observability, evaluation, deployment, scale, cost và trade-off.

## Part 1 — Requirements and first architecture

Mode: `CLOSED_BOOK`  
Thời gian: 55 phút

### T11-P1-Q0 — MCQ calibration

Trước khi chọn database/framework cho một hệ thống mới, bước nào có ROI cao nhất?

A. Làm rõ requirements, constraints và estimates.  
B. Chọn công nghệ nhiều stars nhất.  
C. Tách microservices ngay.  
D. Viết deployment YAML.

Chọn và giải thích.

Đề: thiết kế Enterprise Document Q&A cho 100 nhân viên và 1.000 documents.

### T11-P1-Q1

Hỏi tối đa 12 clarification questions, rồi đánh dấu ba câu blocker.

### T11-P1-Q2

Định nghĩa functional/non-functional requirements, assumptions, non-goals và success metrics.

### T11-P1-Q3

Ước lượng document size, ingestion volume, QPS, storage/context/cost ở mức order-of-magnitude. Nếu thiếu dữ liệu, nêu biến và công thức.

### T11-P1-Q4

Vẽ component và request/ingestion flow cho MVP. Chọn monolith modular hoặc services và giải thích.

## Part 2 — Detailed design

Mode: `DOCS_ALLOWED`  
Thời gian: 70 phút

### T11-P2-Q1 — APIs/data model

Thiết kế API cho upload/update/delete/status/ask/feedback và data model versioned cho document/chunk/index/eval.

### T11-P2-Q2 — Retrieval/LLM

Thiết kế chunking, hybrid retrieval, metadata/ACL filter, rerank, context construction, citation và no-answer behavior.

### T11-P2-Q3 — Auth/security

Thiết kế authentication, authorization, tenant/document ACL, secrets, PII, prompt injection defense và audit.

### T11-P2-Q4 — Async/cache

Xác định phần sync/async, queues, workers, cache keys/invalidation, idempotency và backpressure.

### T11-P2-Q5 — Request-handler pseudocode

Viết pseudocode cho `/ask` thể hiện authentication, authorization, retrieval ACL filter, context budget, model timeout, citation validation, audit/trace và safe error response.

## Part 3 — Scale evolution

Mode: `DOCS_ALLOWED`  
Thời gian: 75 phút

Hệ thống tăng theo ba mốc:

```text
1,000 → 100,000 → 1,000,000 documents
100 → 2,000 → 50,000 users
```

### T11-P3-Q1

Ở mỗi mốc, component nào có thể giữ nguyên, component nào cần thay đổi? Không được mặc định microservices/Kubernetes.

### T11-P3-Q2

Thiết kế partition/sharding/index lifecycle, reindex, delete propagation và disaster recovery.

### T11-P3-Q3

Thiết kế load test, SLI/SLO, capacity plan, rate limit, degradation và cost guardrail.

### T11-P3-Q4

Provider model có outage hoặc tăng giá. Thiết kế abstraction, fallback, data policy và migration test.

## Part 4 — Architecture review

Mode: `WORK_SIMULATION`  
Thời gian: 80 phút

Review một proposal có:

- 8 microservices cho MVP;
- multi-agent cho mọi query;
- một shared vector index không tenant filter;
- cache key chỉ là query;
- log full prompts;
- không golden eval set;
- retry vô hạn;
- release trực tiếp production.

Thực hiện:

1. tìm critical risks và severity;
2. đề xuất minimal architecture an toàn hơn;
3. viết ba ADR quan trọng;
4. tạo launch checklist;
5. nêu technical debt chấp nhận/không chấp nhận;
6. trình bày design review tối đa 500 từ cho CTO và team kỹ thuật.
