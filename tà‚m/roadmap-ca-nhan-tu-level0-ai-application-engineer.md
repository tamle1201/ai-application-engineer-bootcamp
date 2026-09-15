# Đánh giá và roadmap cá nhân: từ Level 0 đến AI Application Engineer

Ngày đánh giá: 14/09/2026  
Nguồn đánh giá:

- `/Users/andinh307/Downloads/Bailam_level0.md`
- `/Users/andinh307/Downloads/Bailam_level1.md`

Phạm vi kết luận: chỉ dựa trên câu trả lời Level 0 và Level 1. Level 2–4, coding thực hành, system design và production ownership chưa được kiểm tra.

Giả định chấm: nội dung trong hai file là bài làm nguyên bản. Điều kiện “không AI/không Internet” và tổng thời gian thực tế chưa có bằng chứng để xác minh nên được ghi `UNKNOWN`. Ở L0.2, ký tự `n` sau `print(result)` được xem là lỗi sao chép đề; câu trả lời được chấm theo đoạn code dự kiến `print(result)`.

## 1. Kết luận hiện tại

```text
Level 0: 7.0/10 — PASS sát ngưỡng
Level 1: 1.0/20 — NOT YET
Level 2–4: NOT TESTED

Level cao nhất đã vượt: Level 0
Định vị: Beginner/Foundation — đủ nền tối thiểu để bắt đầu học AI Application
Sẵn sàng làm AI Application Engineer: NOT READY
Năng lực production: UNKNOWN/NOT TESTED
```

Đây không phải kết luận rằng người làm bài “không có khả năng”. Kết quả cho thấy một số nền tảng lập trình/dữ liệu đã có, nhưng các khái niệm kết nối chúng thành ứng dụng AI còn thiếu. Học ngay agent framework, vector database hoặc multi-agent ở thời điểm này sẽ dễ dẫn đến copy tutorial mà không hiểu failure mode.

## 2. Chấm Level 0

| Câu | Điểm | Nhận xét |
|---|---:|---|
| L0.1 | 1.0/1 | Xác định đúng CSV là input, có bước đọc/tính toán và output là báo cáo theo ngày. |
| L0.2 | 1.0/1 | Xác định đúng các giá trị 4 và 16; nên viết chính xác output Python là `[4, 16]`. |
| L0.3 | 1.0/1 | Nhận ra mẫu số phải khác 0. Chưa đề cập type invalid nhưng đề chỉ yêu cầu một trường hợp. |
| L0.4 | 1.0/1 | SQL đúng điều kiện `status` và `amount`. |
| L0.5 | 0.0/1 | Nhầm endpoint `/orders/123` với port; chưa hiểu GET, POST và status 404. |
| L0.6 | 1.0/1 | Đúng: JSON chuẩn dùng dấu nháy kép cho key/string. |
| L0.7 | 0.5/1 | Đúng khi nói LLM không đảm bảo sự thật; đổi đáp án gợi ý chỉ kiểm tra tính dễ bị dẫn dắt, không xác minh fact. |
| L0.8 | 1.0/1 | Chọn đúng prompt B vì output contract cụ thể. |
| L0.9 | 0.0/1 | “Cá nhân hóa” chưa trả lời vai trò RAG: retrieve tài liệu hiện hành rồi đưa context vào model. |
| L0.10 | 0.5/1 | Có ý đúng về tái hiện lỗi và tìm điều kiện; chưa đủ ba bước, thiếu example/log/phạm vi ảnh hưởng. |
| **Tổng** | **7.0/10** | **PASS sát ngưỡng** |

### Điều Level 0 cho thấy

- Có thể đọc biểu thức Python đơn giản.
- Viết được câu SQL filter cơ bản.
- Nhận biết JSON và prompt có yêu cầu rõ.
- Có trực giác ban đầu rằng lỗi cần được tái hiện theo điều kiện.
- Chưa có mental model đúng về HTTP API và RAG.

## 3. Chấm Level 1

| Câu | Điểm | Nhận xét |
|---|---:|---|
| L1.1 | 0.5/2 | Nhớ được điều kiện invalid nhưng hiểu sai rằng khai báo `float` sẽ tự chặn chuỗi/`None`; Python type hint không tự validate runtime. Trả `None` cũng cần contract rõ. |
| L1.2 | 0.0/2 | Chưa biết mutable default argument và state bị giữ giữa các lần gọi. |
| L1.3 | 0.0/2 | Chưa làm được SQL aggregation theo ngày với `COUNT`, conditional count và `AVG`. |
| L1.4 | 0.25/2 | Nhận biết 429 là quá nhiều request nhưng đánh giá sai 400 là lỗi hệ thống có thể retry; thiếu timeout và retry limit. |
| L1.5 | 0.0/2 | Chưa hiểu schema validation ngoài prompt và cách xử lý missing field. |
| L1.6 | 0.0/2 | Chưa mô tả được luồng RAG cơ bản. |
| L1.7 | 0.25/2 | Có trực giác về vector nhiều chiều nhưng chưa nêu semantic retrieval và vai trò metadata/tenant filter. |
| L1.8 | 0.0/2 | Chưa biết application phải validate tool, arguments và authorization. |
| L1.9 | 0.0/2 | Chưa phân biệt deterministic test, content evaluation và kiểm thử lặp. |
| L1.10 | 0.0/2 | Chưa phân biệt HTTP 200 với task success/business outcome. |
| **Tổng** | **1.0/20** | **NOT YET** |

### Điểm gãy năng lực

Điểm gãy xuất hiện khi bài toán chuyển từ cú pháp đơn lẻ sang cơ chế ứng dụng:

1. Python type/runtime behavior và error contract.
2. HTTP request/response/status/retry.
3. SQL tổng hợp dữ liệu thay vì chỉ filter.
4. LLM output phải được application validate.
5. RAG là một pipeline có retrieval/context/citation, không chỉ “cá nhân hóa”.
6. Embedding không thực thi quyền truy cập.
7. Tool call từ model là input không đáng tin; application giữ quyền quyết định.
8. HTTP success không chứng minh câu trả lời hữu ích.

## 4. Mục tiêu roadmap

Sau 20 tuần, người học cần có khả năng:

- viết Python có validation, exception và unit test;
- xây REST API nhỏ và xử lý status/timeout/retry đúng mức;
- dùng SQL filter, aggregate, join và truy vấn metric;
- gọi model qua interface có fake provider và validate structured output;
- giải thích và xây RAG nhỏ có citations, metadata filter và no-answer behavior;
- tạo eval set, phân biệt technical success với task success;
- xây tool-using workflow có authorization/approval cơ bản;
- hoàn thành một capstone chạy được, có test và README;
- thử lại Level 3 để xác định job-readiness; không mặc định đã sẵn sàng chỉ vì học đủ tuần.

## 5. Thời lượng và nhịp học

Nhịp mặc định: **10 giờ/tuần**, tổng khoảng 200 giờ.

| Ngày | Thời lượng | Hoạt động |
|---|---:|---|
| Thứ 2 | 60 phút | học một khái niệm và viết lại bằng lời của mình |
| Thứ 3 | 90 phút | code ví dụ nhỏ không copy nguyên tutorial |
| Thứ 4 | 90 phút | bài tập biến thể và edge case |
| Thứ 5 | 60 phút | SQL/API/AI concept practice |
| Thứ 7 | 3 giờ | mini-project |
| Chủ nhật | 2 giờ | test, sửa lỗi, nhật ký và tự giải thích |

Nếu chỉ có 6 giờ/tuần, kéo roadmap thành 28–30 tuần; không bỏ bài tập và gate.

Mỗi buổi ghi bốn dòng:

1. Tôi vừa làm được gì?
2. Tôi đã sai ở đâu?
3. Bằng chứng nào cho thấy đã hiểu?
4. Bước nhỏ tiếp theo là gì?

## 6. Phase A — Sửa nền lập trình, SQL và HTTP (Tuần 1–4)

### Tuần 1 — Python value, type và validation

Học:

- `int`, `float`, `str`, `bool`, `None`;
- function input/output;
- type hints khác runtime validation như thế nào;
- `if`, `raise ValueError`, `TypeError`;
- tránh mutable default argument.

Bài tập:

1. Viết `calculate_total(price, quantity)` và test 10 input hợp lệ/không hợp lệ.
2. Sửa `add_tag(tags=[])` bằng `None` hoặc immutable default.
3. Viết `parse_age(value)` nhận số nguyên dương, từ chối `True`, chuỗi rỗng và `None`.

Đầu ra:

- `week01_python_validation.py`;
- `test_week01.py` có ít nhất 12 tests;
- ghi rõ mỗi lỗi dùng `ValueError` hay `TypeError` và lý do.

Gate W1: tự giải thích được vì sao `price: float` không tự chặn chuỗi khi chạy.

### Tuần 2 — Collections, batch và lỗi từng record

Học:

- list/dict/set/tuple;
- comprehension, loop và function decomposition;
- không mutate input ngoài ý muốn;
- xử lý partial failure trong batch.

Bài tập:

1. Chuẩn hóa list record `{id, text}`.
2. Loại duplicate `id`.
3. Trả riêng `valid_records` và `errors` nhưng giữ thứ tự input.
4. Test empty list, missing field, duplicate và wrong type.

Gate W2: đọc và dự đoán được list comprehension; tự viết được batch function có test.

### Tuần 3 — SQL từ filter đến aggregation

Học:

- `SELECT`, `WHERE`, `ORDER BY`;
- `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`;
- `GROUP BY`, `HAVING`;
- `CASE WHEN` và xử lý `NULL`;
- `DATE(created_at)` hoặc date truncation theo database đang dùng.

Bài tập với bảng `requests`:

1. Tổng request theo ngày.
2. Số và tỷ lệ request thành công.
3. Latency trung bình theo ngày.
4. Chỉ lấy ngày có ít nhất 30 request.
5. So sánh hai `config_version`.

Gate W3: viết được truy vấn Level 1 mà không nhìn đáp án.

### Tuần 4 — HTTP, REST, JSON và API contract

Học:

- URL, host, port, path và query parameter;
- GET/POST/PUT/PATCH/DELETE;
- status `200`, `201`, `400`, `401`, `403`, `404`, `409`, `429`, `500`, `503`;
- request/response JSON;
- timeout, retry và lý do không retry mọi lỗi.

Bài tập:

1. Vẽ request flow cho `GET /orders/123`.
2. Thiết kế `POST /orders` gồm request, response và validation errors.
3. Lập bảng: status nào retry/không retry và điều kiện.
4. Dùng Python gọi một fake API function; chưa cần Internet.

Checkpoint A:

- làm 15 câu biến thể về Python/SQL/API;
- yêu cầu ≥12/15;
- nếu chưa đạt, lặp lại hai tuần yếu nhất trước khi sang Phase B.

## 7. Phase B — Nền tảng AI Application (Tuần 5–8)

### Tuần 5 — LLM mental model và prompt contract

Học:

- LLM sinh token và có thể hallucinate;
- prompt rõ task, input, output và missing-data behavior;
- sự khác nhau giữa câu trả lời trôi chảy và fact đúng;
- cách kiểm chứng bằng nguồn/gold/rule thay vì hỏi dẫn dắt lần hai.

Bài tập:

1. Viết lại 10 prompt mơ hồ thành prompt có output contract.
2. Với mỗi output, ghi cách application kiểm tra.
3. Tạo năm case model phải trả “không đủ dữ liệu”.

Gate W5: không dùng “model tự tin” hoặc “model đồng ý lần hai” làm bằng chứng correctness.

### Tuần 6 — Structured output và model API boundary

Học:

- JSON schema ở mức cơ bản;
- required/optional/null;
- parse và validate output;
- provider error, timeout, 429 và retry có giới hạn;
- fake provider để test không cần API key.

Mini-project:

`Email Extractor` nhận text và trả `{sender, intent, urgency}`.

Yêu cầu:

- input validation;
- fake model trả các output hợp lệ/sai schema;
- output validation;
- tối đa ba lần retry chỉ với transient error;
- test missing field, invalid JSON, timeout và 429.

### Tuần 7 — RAG từ đầu đến cuối

Học đúng luồng:

`question → retrieve chunks → filter metadata/permission → attach context → generate → validate/cite`

Khái niệm:

- document, chunk, embedding, vector similarity;
- metadata filter;
- citation và no-answer;
- retrieval failure khác generation failure.

Bài tập:

1. Dùng 10 đoạn văn local, tìm theo keyword trước khi dùng embedding.
2. Trả top-3 chunks cùng document ID.
3. Nếu không có chunk phù hợp, từ chối thay vì bịa.
4. Thêm `department` và chỉ trả document được phép.

### Tuần 8 — Test AI và product metric

Học:

- unit test deterministic;
- eval nội dung;
- exact match, schema-valid rate, retrieval hit, citation correctness;
- HTTP success, answer quality, task success và business outcome khác nhau;
- eval phải chạy nhiều case và lưu config/version.

Bài tập:

1. Tạo 20 câu hỏi cho RAG tuần 7.
2. Mỗi câu có expected document và loại `answerable/no-answer`.
3. Chạy hai cấu hình top-k khác nhau.
4. Ghi số đúng/sai thật; không có gold thì ghi `NOT MEASURED`.

Checkpoint B — làm lại Level 1:

- mục tiêu ≥14/20;
- mỗi câu ít nhất 1/2;
- không được sai nghiêm trọng ở retry, permission hoặc tool validation;
- nếu chưa đạt, lặp Phase B thêm hai tuần bằng bài tập biến thể.

## 8. Phase C — AI App Builder (Tuần 9–12)

### Tuần 9 — FastAPI/service nhỏ

Học:

- route, request/response model;
- validation và error envelope;
- dependency injection ở mức đơn giản;
- configuration qua environment, không hard-code secret.

Đầu ra: biến `Email Extractor` thành API có `/health` và `/extract`.

### Tuần 10 — Testing và debugging

Học:

- unit vs integration test;
- fixture/mock/fake;
- structured log và request ID;
- debug theo reproduce → isolate → hypothesis → test → verify.

Bài tập:

- tạo năm lỗi cố ý rồi viết test bắt lỗi;
- không dùng `except Exception: pass`;
- log không chứa toàn bộ email nhạy cảm.

### Tuần 11 — RAG application v1

Build `Handbook Assistant v1`:

- ingest file Markdown;
- stable document/chunk ID;
- retrieve top-k;
- filter `department`;
- answer với citation hoặc no-answer;
- API endpoint `/ask`;
- dùng fake model mặc định để test offline.

### Tuần 12 — Eval và review v1

Yêu cầu project:

- ≥30 eval cases;
- có slice `simple`, `no-answer`, `wrong-department`;
- metric retrieval và citation;
- test cross-department leakage;
- README có architecture, commands và known limitations.

Checkpoint C — Level 2:

- mục tiêu ≥18/25;
- coding L2.2 ít nhất 3.5/5;
- security L2.6 ít nhất 2/3;
- nếu chưa đạt, tiếp tục project v1 và chưa sang agent.

## 9. Phase D — Production foundations (Tuần 13–16)

Chỉ bắt đầu khi đã PASS Level 2 hoặc được review cho phép tiếp tục có điều kiện.

### Tuần 13 — Persistence và idempotent ingestion

- PostgreSQL schema cho document/chunk/version;
- upsert/deduplicate;
- update/delete propagation;
- job chạy lại không tạo duplicate.

### Tuần 14 — Authorization và tenant isolation

- authentication vs authorization;
- tenant/document ACL;
- permission-aware cache key;
- least privilege;
- negative/adversarial tests.

### Tuần 15 — Reliability và observability

- timeout/retry/backoff có giới hạn;
- structured logs, metrics, traces;
- p95 latency, error rate, retrieval failure;
- fallback và graceful degradation;
- cost trên task thành công.

### Tuần 16 — Handbook Assistant v2

Nâng cấp v1:

- PostgreSQL và một retrieval backend;
- tenant/ACL fail-closed;
- ingestion idempotent;
- ≥50 eval cases;
- Docker, test command, runbook;
- report quality/latency/cost với provenance rõ.

Gate D:

- zero cross-tenant leak trong test suite;
- không bịa metric;
- service chạy lại được từ README;
- giải thích được retrieval failure và generation failure.

## 10. Phase E — Tools, agent và capstone (Tuần 17–20)

### Tuần 17 — Tool calling an toàn

- model chỉ đề xuất tool call;
- application validate tool name/arguments/scope;
- read tool trước write tool;
- idempotency key và audit log;
- high-risk action cần approval.

### Tuần 18 — Agent loop tối giản

- state, step, exit condition;
- max turns/time/token budget;
- tool failure và human handoff;
- chưa dùng multi-agent nếu single-agent đủ.

### Tuần 19 — Capstone: Data & Knowledge Assistant

Tận dụng kiến thức dữ liệu:

- hỏi handbook bằng RAG;
- xem metadata/data catalog bằng read-only tool;
- citation và no-answer;
- tool policy, approval và audit;
- eval theo task và failure type.

### Tuần 20 — Harden, demo và kiểm tra

Nộp:

- source và tests;
- README chạy local;
- architecture diagram;
- eval report;
- security checklist;
- incident giả lập và postmortem ngắn;
- demo 5–8 phút.

Checkpoint E — thử Level 3:

- chỉ thử khi Level 2 đã PASS và capstone v1 chạy được;
- mục tiêu ≥18/25 và vượt hard gates;
- nếu chưa đạt, kết luận là Builder; tiếp tục production practice, không tự gắn job-ready.

## 11. Stack tối thiểu

Giai đoạn đầu chỉ dùng:

- Python 3.11+;
- `unittest` hoặc `pytest`;
- SQLite trước, PostgreSQL sau;
- FastAPI + Pydantic từ Phase C;
- fake model/retriever cho test;
- một model provider thật khi đã có validation và budget;
- Docker từ Phase D.

Chưa cần LangChain/LangGraph, Kubernetes, multi-agent hoặc nhiều vector database trong 12 tuần đầu.

## 12. Nguồn học chính

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [MDN HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [MDN HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic documentation](https://docs.pydantic.dev/latest/)
- Nguồn RAG, agent, eval và production đã tổng hợp tại `05-nguon-doi-chieu-doanh-nghiep.md`.

Quy tắc: đọc phần cần dùng cho bài tập hiện tại; không đọc hết tài liệu một cách thụ động.

## 13. Cách đánh giá lại

| Thời điểm | Bài kiểm tra | Điều kiện đi tiếp |
|---|---|---|
| Cuối tuần 4 | quiz Python/SQL/API biến thể | ≥80% |
| Cuối tuần 8 | Level 1 biến thể | ≥14/20 |
| Cuối tuần 12 | Level 2 | ≥18/25 và security không fail |
| Cuối tuần 16 | review Handbook Assistant v2 | test/eval/ACL/README đạt gate |
| Cuối tuần 20 | Level 3 | ≥18/25 và hard gates PASS |

Không làm lại nguyên câu đã biết thuộc lòng. Đề retest phải đổi dữ liệu và tình huống nhưng giữ cùng competency.

## 14. Việc cần làm ngay trong 7 ngày đầu

1. Tạo folder `week01-python-validation`.
2. Viết ba hàm `calculate_total`, `add_tag`, `parse_age`.
3. Viết ít nhất 12 tests, chạy thật và lưu output.
4. Viết một trang ghi chú: type hint khác runtime validation như thế nào.
5. Làm lại câu L1.1 và L1.2 bằng lời của mình.
6. Chưa học agent hoặc vector database trong tuần này.

Đầu ra tuần đầu phải là code và test chạy được, không chỉ là ghi chú hoặc video đã xem.
