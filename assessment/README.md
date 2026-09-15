# AI Application Engineer — Comprehensive Competency Assessment

Phiên bản: 1.0  
Ngày tạo: 14/09/2026  
Mục tiêu vai trò: **AI Application Engineer = Software Engineering + AI Engineering + Problem Solving**

## 1. Mục đích

Bộ assessment này đo năng lực thực tế theo 12 bài, từ nền tảng đến mô phỏng công việc. Nó tách riêng:

- knowledge;
- understanding;
- application;
- reasoning;
- engineering judgment.

Một câu trả lời đúng nhưng reasoning yếu không được đánh giá ngang với câu trả lời có bằng chứng, giả định, trade-off và cách kiểm chứng rõ.

## 2. Danh mục 12 test

| Mã | Test | Part | Thời lượng dự kiến |
|---|---|---:|---:|
| T01 | Logic & Reasoning | 3 | 90 phút |
| T02 | Problem Solving | 3 | 110 phút |
| T03 | Programming Fundamentals | 4 | 240 phút |
| T04 | OOP & Software Engineering | 4 | 220 phút |
| T05 | Algorithms & Data Structures | 4 | 200 phút |
| T06 | SQL & Data Engineering Thinking | 4 | 220 phút |
| T07 | Debugging | 4 | 210 phút |
| T08 | Testing, Code Quality & Reliability | 4 | 210 phút |
| T09 | AI Fundamentals | 4 | 220 phút |
| T10 | LLM & AI Application Engineering | 5 | 300 phút |
| T11 | AI System Design | 4 | 280 phút |
| T12 | Real-world AI Engineering Simulation | 9 stage | 420–600 phút |

Tổng thời gian ước tính: 40–45 giờ, nên chia trong 4–8 tuần. Không làm tất cả trong một ngày.

## 3. File test

- [T01 — Logic & Reasoning](tests/01-logic-reasoning.md)
- [T02 — Problem Solving](tests/02-problem-solving.md)
- [T03 — Programming Fundamentals](tests/03-programming-fundamentals.md)
- [T04 — OOP & Software Engineering](tests/04-oop-software-engineering.md)
- [T05 — Algorithms & Data Structures](tests/05-algorithms-data-structures.md)
- [T06 — SQL & Data Engineering Thinking](tests/06-sql-data-engineering.md)
- [T07 — Debugging](tests/07-debugging.md)
- [T08 — Testing, Code Quality & Reliability](tests/08-testing-code-quality-reliability.md)
- [T09 — AI Fundamentals](tests/09-ai-fundamentals.md)
- [T10 — LLM & AI Application Engineering](tests/10-llm-ai-application.md)
- [T11 — AI System Design](tests/11-ai-system-design.md)
- [T12 — Real-world Simulation](tests/12-real-world-simulation.md)

Hồ sơ làm bài:

- [Assessment protocol](ASSESSMENT_PROTOCOL.md)
- [Assessor guide](ASSESSOR_GUIDE.md) — không đọc trong khi đang thi
- [Answer template](submissions/ANSWER_TEMPLATE.md)
- [Progress tracker](submissions/PROGRESS.md)
- [Final report template](submissions/FINAL_REPORT_TEMPLATE.md)
- [Manifest và trạng thái kiểm tra](MANIFEST.md)

## 4. Cách thực hiện đúng

1. Người chấm chỉ đưa một Part tại một thời điểm.
2. Người làm khóa câu trả lời của Part hiện tại trước khi nhận Part tiếp theo.
3. Người chấm ghi nhận nội bộ, không đưa đáp án hoặc chữa bài giữa test.
4. Difficulty được điều chỉnh trong phạm vi part adaptive của từng test.
5. Nếu một competency liên tục sai, thêm một câu biến thể để phân biệt thiếu kiến thức với hiểu sai đề.
6. Chỉ công bố báo cáo năng lực tổng thể sau T12.

Toàn bộ câu hỏi được lưu để quản lý phiên bản, nhưng người làm không nên tự đọc trước các Part chưa tới. Nếu đã đọc trước, phải khai báo; độ tin cậy của assessment sẽ giảm.

## 5. Quy tắc không gợi ý

- Không tiết lộ đáp án, expected reasoning hoặc hidden scoring criteria trước khi khóa Part.
- Không sửa câu trả lời giữa Part.
- Khi người làm hỏi đáp án, yêu cầu họ tiếp tục reasoning hoặc ghi `KHÔNG BIẾT`.
- Hint chỉ được dùng trong câu ghi rõ có hint; mọi hint phải được log.
- Không dùng AI/Internet ở closed-book part.
- Open-book/coding part phải khai báo tài liệu và công cụ đã dùng.

## 6. Bắt đầu

Trạng thái ban đầu:

```text
Current test: T01
Current part: Part 1
Overall level: UNKNOWN
```

Bắt đầu tại T01 Part 1. Không mở Part 2 cho đến khi Part 1 đã được khóa.
