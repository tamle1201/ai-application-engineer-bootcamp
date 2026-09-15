# T01 — Logic & Reasoning

Mục tiêu: pattern recognition, deduction, constraints, probability, information sufficiency, assumption detection và logical consistency.

Quy tắc: đưa từng Part; không chữa cho đến khi T01 kết thúc. Part 3 được chọn thích ứng, không nhất thiết dùng mọi câu.

## Part 1 — Foundation

Mode: `CLOSED_BOOK`  
Thời gian: 20 phút

### T01-P1-Q1 — Pattern

Tìm số tiếp theo và giải thích:

```text
3, 8, 15, 24, 35, ?
```

### T01-P1-Q2 — Deduction

1. Mọi tool có quyền ghi dữ liệu đều cần approval.
2. Tool R có quyền ghi dữ liệu.
3. Một số tool cần approval được chạy tự động sau approval hợp lệ.

Kết luận nào bắt buộc đúng?

A. Tool R luôn chạy tự động.  
B. Tool R cần approval.  
C. Mọi tool cần approval đều có quyền ghi.  
D. Tool R không thể chạy.

Giải thích.

### T01-P1-Q3 — Constraints

Có bốn task `A`, `B`, `C`, `D`:

- `A` trước `C`;
- `B` không đứng đầu;
- `D` đứng ngay sau `B`.

Liệt kê mọi thứ tự hợp lệ.

### T01-P1-Q4 — Probability

Túi có 3 viên đỏ, 2 viên xanh. Lấy hai viên không hoàn lại. Biết viên đầu là xanh. Xác suất viên hai là đỏ bằng bao nhiêu? Giải thích.

### T01-P1-Q5 — Base rate

1.000 request gồm 800 mobile và 200 desktop. Có 90 lỗi: 72 từ mobile, 18 từ desktop. Có thể kết luận mobile dễ lỗi hơn không? Tính trước khi kết luận.

### T01-P1-Q6 — Fact và assumption

Manager nói: “Phiên bản mới chậm vì dùng AI.” Chỉ biết latency trung bình tăng từ 2 giây lên 5 giây; chưa có timing database/retrieval/model/network.

Nêu fact, assumption và ba bằng chứng cần thu thập.

## Part 2 — Application

Mode: `CLOSED_BOOK`  
Thời gian: 30 phút

### T01-P2-Q1 — Truth consistency

Ba service A, B, C. Chính xác một phát biểu dưới đây là sai:

1. A đang healthy.
2. Nếu A healthy thì B không timeout.
3. B đang timeout.
4. C đang healthy.

Xác định trạng thái có thể kết luận chắc chắn và điều còn chưa chắc. Trình bày logic.

### T01-P2-Q2 — Scheduling

Năm job `A–E` chạy một lần:

- A trước D;
- B sau A nhưng trước E;
- C không đứng cạnh D;
- E không đứng cuối;
- D đứng sau C.

Tìm một lịch hợp lệ và chứng minh từng constraint. Sau đó cho biết thông tin hiện tại có đủ để khẳng định lịch đó là duy nhất không.

### T01-P2-Q3 — Information sufficiency

Conversion giảm sau release. Đánh giá từng thông tin là `đủ`, `hữu ích nhưng chưa đủ` hoặc `không liên quan trực tiếp` để kết luận release gây ra giảm conversion:

A. Conversion trước 12%, sau 9%.  
B. Nhóm control không nhận release vẫn giữ 12%.  
C. Traffic source sau release thay đổi mạnh.  
D. CEO không thích giao diện mới.

Giải thích.

### T01-P2-Q4 — Conditional reasoning

Nếu cache miss thì database được gọi. Nếu database được gọi và quá tải thì latency vượt 2 giây. Quan sát latency vượt 2 giây.

Có thể kết luận cache miss không? Nếu không, hãy đưa hai nguyên nhân khác phù hợp với quan sát.

### T01-P2-Q5 — Ambiguity

Stakeholder nói: “Hệ thống phải chính xác 95%.” Liệt kê ít nhất năm cách câu này có thể được hiểu khác nhau. Chọn hai câu hỏi làm rõ có ROI cao nhất.

## Part 3 — Adaptive challenge bank

Mode: `CLOSED_BOOK`  
Thời gian: 40 phút  
Người chấm chọn 4/8 câu dựa trên Part 1–2.

### T01-P3-Q1 — Counterexample

Một người phát biểu: “Mọi hệ thống có test coverage trên 90% đều ít bug.” Hãy đưa counterexample hợp lệ và chỉ ra biến bị bỏ qua.

### T01-P3-Q2 — Bayesian update

Một alert phát hiện incident thật với xác suất 90%, nhưng cũng báo nhầm 5% khi không có incident. Trong một ngày bất kỳ, xác suất có incident là 1%. Khi alert bật, có nên nói xác suất incident là 90% không? Tính hoặc mô tả đầy đủ cách tính.

### T01-P3-Q3 — Minimum information

Bạn có hai model A/B. A đúng 80/100 case, B đúng 85/100 case. Nêu ít nhất bốn thông tin còn thiếu trước khi nói B tốt hơn trong production.

### T01-P3-Q4 — Constraint conflict

Yêu cầu đồng thời: zero data retention, audit toàn bộ prompt trong 90 ngày và debug mọi incident bằng exact input. Xác định xung đột và đề xuất câu hỏi/thiết kế để giải quyết.

### T01-P3-Q5 — Causal reasoning

Sau khi thêm cache, latency giảm 30% nhưng error rate tăng. Hãy xây ba hypothesis không mâu thuẫn với cả hai quan sát và chọn phép đo phân biệt chúng.

### T01-P3-Q6 — Elimination

Một batch có output sai. Có bốn nguyên nhân: input, transform, configuration, output writer. Bạn chỉ được chạy hai kiểm tra trước. Chọn hai kiểm tra có information gain cao và giải thích.

### T01-P3-Q7 — Logical communication

Viết kết luận tối đa 100 từ cho một tình huống có evidence mâu thuẫn, phân biệt rõ `đã biết`, `có khả năng`, `chưa biết`.

### T01-P3-Q8 — Code reasoning

Không chạy code. Cho biết function có luôn dừng không, output với `n=10`, và complexity:

```python
def reduce(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        steps += 1
    return steps
```
