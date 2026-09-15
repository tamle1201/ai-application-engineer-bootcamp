# Assessor Guide — Không đọc trong khi đang làm bài

File này chứa framework chấm, không chứa đáp án chi tiết. Người làm bài nên tránh đọc trước khi hoàn tất assessment.

## 1. Năm chiều chấm cho mọi competency

Mỗi chiều chấm 0–100 bằng evidence tích lũy:

| Chiều | Câu hỏi chấm |
|---|---|
| Knowledge | Có biết khái niệm/cơ chế cần thiết không? |
| Understanding | Có giải thích nguyên nhân và giới hạn bằng lời của mình không? |
| Application | Có áp dụng vào code/scenario mới không? |
| Reasoning | Có decomposition, hypothesis, evidence và logic nhất quán không? |
| Engineering judgment | Có chọn phương án phù hợp constraints, trade-off và risk không? |

## 2. Anchor 0–100

| Khoảng | Mô tả |
|---:|---|
| 0–19 | không có evidence hoặc hiểu sai nền tảng |
| 20–39 | nhận biết rời rạc, phụ thuộc hướng dẫn lớn |
| 40–59 | làm được happy path/task rõ, reasoning còn thiếu |
| 60–74 | xử lý độc lập bài thông thường, có edge cases chính |
| 75–89 | reasoning và trade-off tốt, production-aware |
| 90–100 | nhất quán ở bài khó/mơ hồ, định hướng được người khác |

Không dùng một đáp án tốt để cho 90+. Cần consistency qua nhiều test.

## 3. Trọng số overall

| Competency | Trọng số |
|---|---:|
| Software Engineering | 8% |
| Programming | 8% |
| OOP | 4% |
| Algorithms | 5% |
| SQL/Data | 7% |
| Debugging | 7% |
| Testing/Reliability | 6% |
| Problem Solving | 7% |
| Logical Reasoning | 5% |
| AI Fundamentals | 7% |
| LLM | 8% |
| RAG | 8% |
| System Design | 8% |
| Engineering Mindset | 7% |
| Communication | 5% |
| **Tổng** | **100%** |

Overall chỉ được tính nếu coverage đủ. Nếu bất kỳ nhóm trọng yếu `Programming`, `Debugging`, `LLM/RAG`, `System Design` chưa được kiểm tra ở application level, ghi `OVERALL NOT READY TO CALCULATE`.

## 4. Level classification

| Level | Diễn giải |
|---|---|
| 0 — Beginner | cần hướng dẫn phần lớn task |
| 1 — Junior Beginner | có nền tảng nhưng phụ thuộc hướng dẫn |
| 2 — Junior | xử lý task rõ ràng tương đối độc lập |
| 3 — Strong Junior | debug, thiết kế và xử lý vấn đề tương đối độc lập |
| 4 — Intermediate | engineering judgment và system thinking tốt |
| 5 — Strong Intermediate | ownership và thiết kế hệ thống đáng kể |
| 6 — Senior | đưa technical direction, quản trị risk và bài toán phức tạp |

Level không phải phép chia điểm đơn giản. Dùng điểm làm signal, sau đó áp hard gate và production evidence. Level 5–6 cần history thực tế, không thể xác nhận chỉ bằng take-home test.

## 5. Behavioral tracker

Sau mỗi test, ghi evidence cho 15 pattern:

1. clarify trước khi làm;
2. xác định requirement;
3. phân biệt fact/assumption;
4. tìm evidence;
5. biết nói không đủ thông tin;
6. ưu tiên;
7. tránh over-engineer;
8. chọn phương án đơn giản;
9. maintainability;
10. edge cases;
11. failure scenarios;
12. trade-off;
13. rollback/fallback;
14. ownership;
15. evidence-based reasoning.

Mỗi pattern ghi `POSITIVE`, `MIXED`, `NEGATIVE`, `NOT OBSERVED` và ít nhất một trích dẫn khi kết luận.

## 6. Confidence

- `HIGH`: nhiều evidence trực tiếp, điều kiện thi được giữ, code/runtime xác minh.
- `MEDIUM`: evidence trực tiếp nhưng coverage hoặc điều kiện còn thiếu.
- `LOW`: chủ yếu self-report/inference, có dấu hiệu đọc trước hoặc dùng trợ giúp không khai báo.

## 7. Role readiness

Chấm riêng cho:

- Software Engineer Intern;
- AI Engineer Intern;
- AI Application Engineer Intern;
- Junior Software Engineer;
- Junior AI Engineer;
- Junior Data Engineer.

Mỗi role dùng `READY`, `CONDITIONALLY READY`, `NOT READY`, `UNKNOWN`, kèm ba evidence và tối đa ba blocker.

