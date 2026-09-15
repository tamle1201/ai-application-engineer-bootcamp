# T12 — Real-world AI Engineering Simulation

Mục tiêu: tích hợp toàn bộ năng lực trong một project simulation và các incident tuần tự. Người chấm chỉ đưa một Stage tại một thời điểm.

Mode chung: `WORK_SIMULATION`. Được dùng docs/tool như công việc thật nhưng phải lưu nguồn, prompt AI, command, output và quyết định. Không được dùng AI để thay toàn bộ reasoning/ownership.

## Initial brief

Một công ty muốn AI assistant cho 100 nhân viên dựa trên 50.000 tài liệu nội bộ. Bạn được giao build MVP trong hai tuần. Specification chưa đầy đủ.

## Stage 1 — Discovery

Thời gian: 45 phút

### T12-S1-Q0 — MCQ calibration

Với brief chưa đầy đủ và deadline hai tuần, hành động đầu tiên là:

A. Mua vector database.  
B. Làm rõ user/workflow/data/access/outcome và blocker constraints.  
C. Xây multi-agent.  
D. Fine-tune model.

Chọn và giải thích.

Không thiết kế kiến trúc ngay. Nộp:

1. stakeholder/user map;
2. tối đa 15 clarification questions;
3. ba blocker questions;
4. current workflow/baseline cần đo;
5. assumptions/unknowns/risk register ban đầu;
6. trường hợp nên dùng search/workflow thay vì agent.

## Stage 2 — Scope and success

Thời gian: 50 phút

Thông tin bổ sung:

- tài liệu thuộc HR, Legal, Engineering;
- quyền đọc khác nhau theo user;
- nguồn thay đổi mỗi ngày;
- câu trả lời cần citation;
- chưa cho phép AI thực hiện write action.

Nộp:

1. problem statement;
2. MVP/in-scope/out-of-scope;
3. functional và measurable non-functional requirements;
4. business/quality/operational/guardrail metrics;
5. acceptance criteria và launch blockers.

## Stage 3 — Architecture and execution plan

Thời gian: 100 phút

Nộp:

1. end-to-end ingestion/request architecture;
2. API và versioned data model;
3. parsing/chunking/index/retrieval/context/citation;
4. authorization/trust boundaries;
5. eval dataset, slices, graders và release gate;
6. logs/metrics/traces/SLO;
7. deployment/rollback;
8. 10-day plan, dependencies, owners và risks;
9. build/buy decisions;
10. ba trade-off và non-goals.
11. pseudocode request handler thể hiện ACL, retrieval, model timeout, citation validation và trace.

## Stage 4 — Incident A: Accuracy giảm

Thời gian: 45 phút

Ngày 3 sau pilot, answer acceptance giảm 84% → 62%.

- retrieval Recall@5 giảm 90% → 65%;
- khi chuyên gia đưa đúng context, answer accuracy vẫn 91%;
- ingestion vừa thay chunking và embedding model;
- chưa có evidence model generation đổi.

Nộp severity, fact/assumption, ranked hypotheses, năm checks, containment/rollback, recovery criteria và regression prevention.

## Stage 5 — Incident B/C: Latency tăng và provider lỗi

Thời gian: 55 phút

Sau khi accuracy phục hồi:

- p95 6s → 17s;
- provider thỉnh thoảng trả 429/503;
- app retry tối đa 5 lần đồng bộ;
- queue depth tăng;
- cost/task thành công tăng 60%.

Thiết kế stage timing, retry budget/backoff, concurrency/rate limit, fallback/degradation, circuit breaker, user experience và cost recovery metric.

## Stage 6 — Incident D: Database quá tải

Thời gian: 50 phút

- DB connections chạm max;
- query p95 tăng 10 lần;
- traffic chỉ tăng 30%;
- worker và API dùng chung pool;
- một query feedback mới scan bảng lớn.

Nộp containment, explain/query/index/pool investigation, workload isolation, capacity plan, verification và rollback.

## Stage 7 — Incident E: Hallucination

Thời gian: 45 phút

User báo assistant bịa policy. Chỉ có screenshot, chưa có trace.

Nộp evidence request, taxonomy retrieval/generation/stale/no-answer/evaluator, user containment, eval case addition, citation validation và stakeholder update. Không được kết luận root cause khi thiếu dữ liệu.

## Stage 8 — Incident F: Prompt injection

Thời gian: 60 phút

Một retrieved document chứa instruction yêu cầu model tiết lộ secret và bỏ qua policy. Red-team cho thấy agent đôi khi làm theo. Hiện chưa có write tool nhưng log có thể chứa dữ liệu nhạy cảm.

Nộp:

1. severity/threat model;
2. containment và secret/log review;
3. trust boundary;
4. defense layers;
5. least privilege/output handling;
6. adversarial tests;
7. incident disclosure/escalation;
8. điều không thể giải quyết chỉ bằng prompt.

## Stage 9 — Incident G: Deadline giảm một nửa

Thời gian: 70 phút

Deadline còn 5 ngày. Stakeholder vẫn muốn launch cho 100 users.

Nộp:

1. reprioritized scope;
2. must-have/remove/defer;
3. risk acceptance cần ai phê duyệt;
4. daily plan;
5. release/no-go criteria;
6. rollout/canary/rollback/support plan;
7. communication cho executive và engineering;
8. final recommendation: launch, limited pilot hoặc delay;
9. bằng chứng khiến quyết định thay đổi.

## Final reflection — chỉ sau Stage 9

Không tự chấm điểm. Trả lời:

- ba quyết định tốt nhất và evidence;
- ba chỗ reasoning yếu hoặc assumption sai;
- lúc nào đã over-engineer;
- lúc nào đã thay đổi quyết định nhờ evidence;
- điều gì cần học tiếp nếu nhận role ngày mai;
- phần nào của solution bạn có thể tự ownership;
- phần nào cần review/mentorship.

Sau phần này, assessor mới được tạo final competency report.
