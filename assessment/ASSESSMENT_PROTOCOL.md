# Assessment Protocol

## 1. Chế độ thi

Mỗi Part phải ghi một trong ba chế độ:

- `CLOSED_BOOK`: không AI, Internet, IDE execution hoặc ghi chú, trừ khi đề cho phép.
- `DOCS_ALLOWED`: được đọc tài liệu chính thức, không dùng AI sinh lời giải.
- `WORK_SIMULATION`: được dùng công cụ như môi trường làm việc thật nhưng phải lưu audit log, prompt, nguồn và quyết định.

Nếu vi phạm điều kiện, không tự động cho 0; đánh dấu `CONDITION_VIOLATION` và giảm confidence của kết luận liên quan.

## 2. Quy trình mỗi Part

```text
Introduce competency and time
→ Present only current Part
→ Candidate answers and states completion
→ Lock answer
→ Assessor records evidence silently
→ Optional clarification that does not teach answer
→ Adaptive routing
→ Next Part
```

Không chữa bài giữa một Test. Sau khi kết thúc Test có thể báo `completed` và các điều kiện dữ liệu còn thiếu, nhưng chưa công bố overall level trước T12.

## 3. Adaptive routing

Sau mỗi Part, người chấm chọn:

- `RAISE`: đúng và reasoning rõ → dùng câu edge case/trade-off khó hơn.
- `PROBE`: đáp án đúng nhưng reasoning yếu → hỏi “vì sao/cách kiểm chứng” ở biến thể mới.
- `RETEST`: sai một câu → kiểm tra cùng competency bằng ngữ cảnh khác.
- `STOP_DEPTH`: sai liên tiếp → ghi knowledge gap, không tiếp tục làm khó vô ích.
- `CONTINUE`: năng lực phù hợp với difficulty hiện tại.

Không kết luận competency từ một câu duy nhất. Tối thiểu hai evidence items cho một kết luận mạnh.

## 4. Evidence tagging

Mỗi quan sát dùng tag:

- `DIRECT`: thể hiện trực tiếp trong câu trả lời/code.
- `INFERRED`: suy luận hợp lý nhưng chưa kiểm tra trực tiếp.
- `SELF_REPORTED`: người làm tự khai.
- `NOT_TESTED`: chưa có câu hỏi/bài thực hành.
- `UNKNOWN`: dữ liệu không đủ hoặc mâu thuẫn.

Không nâng `SELF_REPORTED` thành `DIRECT` nếu chưa có code, reasoning hoặc runtime evidence.

## 5. Quy tắc coding

- Ghi thời gian bắt đầu/kết thúc.
- Không xóa test có sẵn.
- Lưu command và output thật.
- Nếu không chạy được, ghi blocker nguyên văn.
- Chấm correctness, readability, maintainability, robustness, complexity và edge cases.
- Code chạy được nhưng không giải thích được bị giảm confidence về ownership.

## 6. Quy tắc system design

Người làm phải tự làm rõ requirement trước. Nếu họ lập tức vẽ kiến trúc, người chấm không nhắc. Quan sát:

- functional/non-functional requirements;
- estimates và constraints;
- assumptions/unknowns;
- API/data model/component/flow;
- failure, security, reliability, cost;
- trade-off và non-goals.

Không yêu cầu dùng một cloud/framework cụ thể trừ khi đề nêu.

## 7. Quy tắc final report

Chỉ sau T12 mới tạo:

- overall weighted score;
- 15 competency scores;
- năm điểm mạnh/yếu;
- hidden gaps và reasoning patterns;
- role readiness;
- roadmap theo evidence;
- confidence và phần chưa kiểm tra.

Không dùng từ `job-ready`, `senior` hoặc tương đương nếu hard gate chưa đạt.

## 8. Hard gates

Dù điểm tổng cao, không thể đạt Level 3+ nếu:

- không tự viết/test/debug code cơ bản;
- authorization hoặc tenant isolation fail-open;
- agent được thực hiện side effect rủi ro không có policy/approval;
- không có cách đánh giá AI output tái lập;
- retry vô hạn hoặc không có timeout ở external calls;
- bịa metric, test output hoặc fact;
- không phân biệt fact, assumption và inference trong incident quan trọng.

