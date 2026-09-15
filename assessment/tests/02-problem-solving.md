# T02 — Problem Solving

Mục tiêu: framing, decomposition, root cause, hypothesis, prioritization, ambiguity, evidence và decision making.

## Part 1 — Framing fundamentals

Mode: `CLOSED_BOOK`  
Thời gian: 30 phút

### T02-P1-Q0 — MCQ calibration

Khi nhận yêu cầu “làm chatbot AI càng sớm càng tốt”, hành động đầu tiên tốt nhất là:

A. Chọn model mạnh nhất.  
B. Làm rõ user, workflow, outcome và constraints.  
C. Tạo vector database.  
D. Viết prompt dài.

Chọn và giải thích.

### T02-P1-Q1 — Vague request

Stakeholder nói: “Làm một AI chatbot cho công ty càng sớm càng tốt.”

Viết tối đa tám câu hỏi làm rõ. Sau đó chọn ba câu phải hỏi trước tiên và giải thích vì sao.

### T02-P1-Q2 — Problem statement

Từ yêu cầu trên, viết một problem statement gồm user, pain, current workflow, desired outcome và non-goal. Không tự bịa số liệu.

### T02-P1-Q3 — Decomposition

Phân rã “chatbot trả lời sai” thành các vùng nguyên nhân có thể kiểm tra độc lập. Không đề xuất fix ở bước này.

### T02-P1-Q4 — Five Whys critique

Một engineer viết:

```text
Why sai? Vì model kém.
Why model kém? Vì model nhỏ.
Why model nhỏ? Vì muốn rẻ.
Root cause: ngân sách thấp.
```

Chỉ ra vấn đề trong reasoning và thiết kế lại cách điều tra.

### T02-P1-Q5 — Prioritization

Có ba issue: 2% request lỗi 500, 15% câu trả lời thiếu citation, màu nút sai design. Chưa có thêm dữ liệu. Bạn xử lý theo thứ tự nào? Nêu assumption và thông tin có thể làm đổi thứ tự.

## Part 2 — Root-cause application

Mode: `CLOSED_BOOK`  
Thời gian: 35 phút

### T02-P2-Q1 — Incident hypothesis

Sau deploy 10:00, p95 tăng từ 3s lên 9s. Model latency không đổi; database CPU tăng 30% lên 95%; cache hit giảm 80% xuống 20%.

Tạo hypothesis tree, xếp hạng và chọn năm kiểm tra đầu.

### T02-P2-Q2 — Incomplete information

Khách hàng nói “AI đôi khi bịa”. Bạn chỉ có ảnh chụp một câu trả lời, không có prompt, model version, retrieved context hoặc timestamp.

Viết phản hồi đầu tiên, danh sách evidence cần thu thập và containment tạm thời.

### T02-P2-Q3 — Decision matrix

MVP có deadline hai tuần. Chọn giữa:

- A: keyword search, nhanh làm, quality chưa biết;
- B: managed vector search, chi phí cao hơn, tích hợp nhanh;
- C: self-hosted vector DB, kiểm soát cao, team chưa từng vận hành.

Tạo tiêu chí quyết định, nêu lựa chọn tạm thời và điều kiện làm lựa chọn thay đổi.

### T02-P2-Q4 — Scope control

Ngày thứ 5/10, stakeholder thêm voice, mobile app và auto-write vào CRM. Hãy thương lượng lại scope mà không chỉ nói “không”.

## Part 3 — Adaptive ambiguity

Mode: `WORK_SIMULATION`  
Thời gian: 45 phút  
Người chấm chọn 3/6 câu.

### T02-P3-Q1 — Conflicting goals

Security muốn zero retention; Support muốn lưu toàn hội thoại để debug; Product muốn personalization. Xây options, trade-off và quyết định đề xuất.

### T02-P3-Q2 — Evidence conflict

Offline eval tăng 10 điểm nhưng user satisfaction giảm. Nêu hypothesis, phép đo và cách tránh tối ưu sai metric.

### T02-P3-Q3 — Build vs buy

Đánh giá build/buy cho OCR + document parsing khi deadline ngắn nhưng dữ liệu nhạy cảm. Không được chọn chỉ theo giá.

### T02-P3-Q4 — Failure budget

Team có một tuần. Bạn được chọn cải thiện một trong: task success +5%, p95 -30%, cost -25%, hoặc fix một security gap chưa exploit. Hãy đặt câu hỏi rồi quyết định.

### T02-P3-Q5 — Communication under uncertainty

Viết update tối đa 150 từ khi chưa có root cause, đã có impact và có hai hypothesis cạnh tranh. Phải có next checkpoint nhưng không bịa ETA.

### T02-P3-Q6 — Decision pseudocode

Viết pseudocode cho một triage function nhận `impact`, `security_risk`, `reversibility`, `evidence_quality` và trả `investigate`, `rollback`, `disable_feature` hoặc `escalate`. Nêu limitation: quyết định nào không nên tự động hóa chỉ bằng vài biến này?
