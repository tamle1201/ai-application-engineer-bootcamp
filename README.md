# Bootcamp AI Application Engineer (16 Tuần Cường Độ Cao)

Ngày cập nhật: 15/09/2026
Định dạng: Bootcamp cá nhân 1-kèm-1 (cùng AI Study Buddy).
Cường độ: **8 - 10 giờ/ngày** (56 - 70 giờ/tuần).
Mục tiêu: Đào tạo từ một người có nền tảng Software/Data Engineering còn yếu trở thành một **AI Application Engineer** chuẩn Production trong vòng 16 tuần.

---

## 1. Triết lý của Bootcamp này

Khác với các lộ trình thong thả 32 tuần, Bootcamp này tận dụng tối đa quỹ thời gian khổng lồ của bạn (8-10h/ngày) để **ép xung** việc học. Tuy nhiên, nguyên tắc bất di bất dịch là: **Không nhảy cóc!**

Trọng tâm của khóa học này không phải là lao ngay vào gọi API của ChatGPT, mà là dành trọn vẹn 1 tháng đầu tiên (Phase 1) để xây dựng một cái móng bê tông cốt thép về:
- Lập trình hướng đối tượng (OOP) và Type Hints trong Python.
- Tư duy Database và truy vấn SQL (PostgreSQL).
- Kiến trúc API bất đồng bộ (FastAPI) và Background Jobs.
- Đóng gói ứng dụng (Docker) và ghi log.

Một khi móng đã vững, việc tiếp thu kiến thức về AI (RAG, Agents, LLM Routing) sẽ cực kỳ nhanh và bạn có thể tự tay xây dựng các hệ thống AI chạy ổn định ngoài thực tế (Production-ready).

## 2. Cách sử dụng bộ tài liệu này

Do tính chất đặc thù của Bootcamp 16 tuần, bạn có thể **bỏ qua** file lộ trình cũ `03-roadmap-32-tuan.md` (vì nó quá chậm) và `00-ban-do-nang-luc.md`.

Cách học chuẩn:
1. Đọc kỹ file **`16-tuan-hoc-tap-chi-tiet.md`** để nắm được bức tranh toàn cảnh và mục tiêu của từng tuần.
2. Tuân thủ **Flow làm việc hàng ngày** (Xem chi tiết ở Mục 4). Mở đúng folder của ngày hôm đó ra để học.
3. Không tự ý xóa thư mục `assessment/`. Dù hiện tại chúng ta chưa dùng đến, nhưng sau khi hoàn thành 16 tuần, bạn sẽ cần làm 12 bài test trong đó để đánh giá lại năng lực trước khi đi phỏng vấn.

## 3. Cấu trúc thư mục hiện tại

```text
ai-application-engineer-roadmap/
├── README.md                          # (File bạn đang đọc) Hướng dẫn tổng quan
├── 16-tuan-hoc-tap-chi-tiet.md        # Bức tranh toàn cảnh lộ trình 16 tuần
├── ke-hoach-hoc-tap/                  # Chứa file kế hoạch chi tiết từng ngày
├── nhat-ky-hoc-tap/                   # Nơi ghi chú bài học, lưu lại Bug và kinh nghiệm
├── tai-lieu-hoc-tap/                  # Kho lưu trữ các tài liệu, folder riêng từng ngày
├── thuc-hanh/                         # Nơi chứa source code bài Lab của từng ngày
├── assessment/                        # Bộ 12 bài test đánh giá năng lực (Làm ở cuối khóa)
```

## 4. Flow làm việc hàng ngày (Daily Workflow)

Đây là kỷ luật sống còn để duy trì cường độ 10 tiếng/ngày mà không bị kiệt sức. Bạn sẽ có một **AI Study Buddy** đồng hành xuyên suốt:

- **🌞 Sáng (Nhận nhiệm vụ & Nạp lý thuyết):** Mở file kế hoạch trong thư mục `ke-hoach-hoc-tap/`. Đọc tài liệu (Docs chính hãng). Mọi khái niệm kỹ thuật khó hiểu phải yêu cầu AI giải thích ngay lập tức. Gom nhặt link hay vào `tai-lieu-hoc-tap/`.
- **🌤️ Chiều (Code Lab & Giải quyết Bug):** Bắt tay vào gõ code. Code bằng tay, không copy-paste vô tội vạ. Khi gặp bug đỏ màn hình, copy log lỗi gửi cho AI để cùng phân tích nguyên nhân và tìm cách sửa (Pair-programming).
- **🌙 Tối (Review & Đóng gói):** 
  1. Gọi AI để báo cáo tổng kết ngày.
  2. Điền những kiến thức cốt lõi vào file `nhat-ky-hoc-tap/`.
  3. AI sẽ tự động sinh ra Kế hoạch học tập, Nhật ký rỗng và file Tài liệu cho ngày hôm sau dựa trên tiến độ thực tế của bạn.
- **🏁 Cuối khóa (Tuần 16):** Mở thư mục `assessment/` để AI đóng vai Giám khảo phỏng vấn (Mock Interview).

## 5. Quy tắc thép của Bootcamp

1. **Code every day:** Phải có code, có bug và sửa được bug mỗi ngày. Nếu một ngày chỉ ngồi xem video/đọc docs mà không gõ phím, ngày đó coi như bỏ đi.
2. **Nói KHÔNG với Framework ở giai đoạn đầu:** Bạn phải tự viết Agent loop bằng vòng lặp `while`, tự code RAG bằng cách chẻ chuỗi và tính Cosine Similarity, trước khi được phép dùng LangGraph hay LlamaIndex. Hiểu bản chất quan trọng hơn gọi thư viện.
3. **Debug là học:** Thời gian kẹt lại ở một cái Bug chính là lúc tư duy kỹ sư của bạn đang phát triển. Đừng nản chí!
