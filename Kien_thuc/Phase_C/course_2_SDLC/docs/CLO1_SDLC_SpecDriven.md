# CLO 1: Vòng đời phát triển phần mềm (SDLC) & Spec Driven Development

## Mục tiêu học tập
1. Nắm được SDLC (Software Development Life Cycle) và Agile Scrum cơ bản.
2. Hiểu khái niệm CI/CD tự động hóa.
3. **Quan trọng nhất:** Làm chủ kĩ thuật Spec Driven Development (Lập trình điều khiển bằng Tài liệu).

---

## 1. SDLC, Agile Scrum và CI/CD (Lý thuyết nền)
- **SDLC:** Quy trình chuẩn để làm ra 1 phần mềm từ số 0 (Phân tích yêu cầu -> Thiết kế hệ thống -> Code -> Test -> Triển khai lên mạng -> Bảo trì).
- **Agile Scrum:** Chia nhỏ thời gian làm dự án thành từng đợt ngắn (Sprint từ 1-2 tuần). Làm đến đâu họp kiểm tra đến đó, thay vì ôm đồm làm 6 tháng rồi đến cuối mới lòi ra lỗi sai.
- **CI/CD:** Hệ thống tích hợp tự động. Khi bạn gõ `git push` code lên mạng, máy chủ sẽ tự động tải code về, tự động chạy Unit Test, nếu không có lỗi thì tự động cập nhật web cho khách hàng dùng (Giúp lập trình viên không phải deploy bằng tay).

## 2. Spec Driven Development (Kỷ nguyên của Lập Trình Viên AI)
Trong thời đại AI lên ngôi, việc "code tay" đang dần lùi về sau. Phương pháp **Spec Driven Development** ra đời.

* **Ngày xưa:** Bạn viết một cái tài liệu (Spec) bằng lời văn lỏng lẻo -> Đưa cho 1 Coder con người đọc -> Coder tự suy đoán chỗ thiếu sót và hì hục tự gõ code.
* **Ngày nay:** Bạn viết một tài liệu Spec **CỰC KỲ CHẶT CHẼ, chi tiết đến từng file, từng biến số** -> Bạn nạp file Spec này vào cho AI (ChatGPT, Claude, hoặc Cursor IDE) -> AI sẽ đọc Spec và **tự động sinh ra 100% Source Code** chuẩn xác chỉ trong vài giây.

Điều kiện tiên quyết: **AI chỉ code đúng nếu bạn viết Spec đủ xịn.** Trình độ viết Spec chính là ranh giới phân biệt giữa AI Engineer "pro" và "gà mờ".

> 👉 **Hành động:** Mở file `VD/01_spec_template.md` ra xem mẫu một tài liệu Spec dùng để ra lệnh cho AI tự code (Bạn có thể copy file đó bỏ vào ChatGPT để thử nghiệm xem nó sinh ra code kinh khủng như thế nào nhé)!
