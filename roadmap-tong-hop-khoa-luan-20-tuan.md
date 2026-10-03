# LỘ TRÌNH TỔNG HỢP (20 TUẦN): TỪ NỀN TẢNG ĐẾN BẢO VỆ KHÓA LUẬN RAG
*(Gộp Roadmap cá nhân AI Application Engineer và Lộ trình Khóa luận)*

**Thời gian dự kiến:** 20 Tuần (~5 tháng) - Hoàn toàn phù hợp với quỹ thời gian 6 tháng của bạn, vừa đủ để bù đắp nền tảng vừa ra được sản phẩm chất lượng cao.
**Nhịp độ học/làm:** 6 ngày/tuần, 4-5 tiếng/ngày.

Lộ trình chia làm 5 Phase, kết nối chặt chẽ giữa việc "Học nền tảng lập trình/AI" và "Làm trực tiếp vào Khóa luận".

---

## PHASE A: VÁ LỖ HỔNG LẬP TRÌNH & HTTP API (Tuần 1 - 4)
*Mục tiêu: Đạt chuẩn lập trình ứng dụng Backend cơ bản, không bị "gãy" khi code xử lý dữ liệu và API.*

* **Tuần 1: Python Value, Type & Validation**
  * **Học:** Data types, input/output, type hints khác gì runtime validation, `try-except`.
  * **Làm:** Thực hành viết các hàm validate dữ liệu đơn giản, viết Unit test (như yêu cầu trong roadmap cá nhân).
* **Tuần 2: Collections & Batch Processing**
  * **Học:** List/Dict/Set, Comprehension, cách xử lý mảng mà không làm mutate dữ liệu gốc, xử lý partial failure (rất quan trọng khi code Pipeline sau này).
  * **Làm:** Viết script lọc và làm sạch list các dictionaries.
* **Tuần 3: Xử lý dữ liệu văn bản (Thay cho SQL)**
  * **Học:** Cách đọc, ghi file txt/json/csv. Regex cơ bản. (Giai đoạn này tạm bỏ qua SQL nâng cao vì khóa luận của bạn tập trung xử lý file text Quy chế).
  * **Làm:** Thu thập tài liệu Quy chế học vụ. Viết script parse dữ liệu từ PDF/Word sang dạng text sạch, loại bỏ header/footer.
* **Tuần 4: HTTP, REST, JSON & Backend (FastAPI)**
  * **Học:** URL, GET/POST, status codes (200, 400, 500, 429), JSON parse, Timeout/Retry.
  * **Làm:** Viết một endpoint FastAPI `/health` cơ bản. Gọi thử một API bên ngoài.

---

## PHASE B: NỀN TẢNG AI & RAG CƠ BẢN (Tuần 5 - 8)
*Mục tiêu: Hiểu cơ chế của LLM và ra được bản RAG Version 1.*

* **Tuần 5: LLM Mental Model & Prompt Contract**
  * **Học:** LLM sinh token, hiện tượng Hallucination. Prompt cần rõ ràng Input/Output/Missing-data behavior.
  * **Làm:** Viết prompt yêu cầu LLM trả lời câu hỏi dựa trên text Quy chế, ép LLM trích dẫn (citation) hoặc từ chối nếu không có data.
* **Tuần 6: Structured Output & Model API**
  * **Học:** JSON Schema, ép LLM trả về JSON định sẵn. Xử lý lỗi từ Provider (timeout, rate limit).
  * **Làm:** Tích hợp Gemini/OpenAI API vào Python code. Ép trả về JSON thay vì text thường.
* **Tuần 7: Hoàn thiện Pipeline RAG**
  * **Học:** Document, Chunking (Recursive, Semantic), Vector Similarity, Embedding. 
  * **Làm:** Cắt nhỏ văn bản Quy chế từ Tuần 3 thành chunk, nhúng Embedding và lưu vào Vector DB (Chroma/Qdrant). Viết hàm `retrieve()`.
* **Tuần 8: Tích hợp RAG Backend v1 & Testing**
  * **Làm:** Nối Retrieval -> Generator. Bọc toàn bộ vào 1 endpoint FastAPI `POST /ask`.
  * **Đánh giá (Checkpoint B):** Chạy thử 20 câu hỏi chay, kiểm tra API có trả về kết quả mượt mà không.

---

## PHASE C: NGHIÊN CỨU CHUYÊN SÂU KHÓA LUẬN (Tuần 9 - 12)
*Mục tiêu: Xây dựng thuật toán Cốt lõi của khóa luận (Claim Verification & Abstention).*

* **Tuần 9: Tách phát biểu (Claim Extraction)**
  * **Học/Làm:** Áp dụng bài học Structured Output (Tuần 6). Viết prompt nhận 1 đoạn trả lời dài -> LLM bẻ thành mảng các phát biểu nguyên tử (Atomic Claims).
  * **Test:** Chạy tách thử 50 câu, review xem bị sót ý không.
* **Tuần 10: Kiểm chứng NLI (Verification)**
  * **Học/Làm:** Tìm hiểu mô hình Cross-encoder tiếng Việt hoặc dùng LLM prompt để so sánh `[Claim, Evidence]`. Trả về nhãn `Supported`, `Contradicted`, `Insufficient`.
* **Tuần 11: Logic từ chối (Decision Policy)**
  * **Làm:** Code thuật toán đếm nhãn. (VD: 100% Xanh -> `FULL`, có Xám/Đỏ -> `PARTIAL`, 100% Xám -> `ABSTAIN`).
  * **Làm:** Chỉnh sửa cấu trúc JSON trả về của API `/ask` chứa đầy đủ Nodes (Question, Claims, Evidence) và Edges (Mối quan hệ) để sẵn sàng cho UI.
* **Tuần 12: Unit Test & Bắt lỗi**
  * **Học/Làm:** Viết Unit test cho luồng Backend. Xử lý các edge cases như: File text quá dài, API rate limit, LLM trả về sai format. Báo cáo chốt Backend.

---

## PHASE D: XÂY DỰNG SẢN PHẨM VISUAL GRAPH (Tuần 13 - 16)
*Mục tiêu: Thay vì làm các hệ thống "Handbook" chung chung, áp dụng trực tiếp xây Giao diện Obsidian-like cho Khóa luận.*

* **Tuần 13: Cơ bản Frontend & Vẽ Graph**
  * **Học/Làm:** Setup React (Vite). Đọc docs thư viện `React Flow`. 
  * **Thực hành:** Dùng data tĩnh (mock json) để render 1 cây đồ thị cơ bản lên màn hình (Custom node hình chữ nhật, có màu sắc theo status).
* **Tuần 14: Tích hợp Backend - Frontend**
  * **Làm:** Code ô nhập Chat, gọi API từ Backend. Khi nhận cục JSON từ hệ thống RAG NLI, update state để Graph "mọc" ra tự động.
* **Tuần 15: Tương tác người dùng (Interactivity)**
  * **Làm:** Thêm thuật toán `dagre.js` để tự sắp xếp node đẹp (Auto-layout). Cho phép click vào Node Bằng chứng để đọc toàn văn.
  * **Làm:** Thêm Filter (VD: Nút Ẩn các claim bị Contradicted).
* **Tuần 16: Polish UI & Đóng gói sản phẩm**
  * **Làm:** Thêm Loading skeleton, xử lý tràn chữ, style màu sắc đẹp mắt. Viết README cách chạy (Docker nếu cần).
  * **Đánh giá (Checkpoint D):** Demo sản phẩm End-to-End, có UI hoàn chỉnh.

---

## PHASE E: ĐÁNH GIÁ & VIẾT BÁO CÁO (Tuần 17 - 20)
*Mục tiêu: Đong đếm số liệu khoa học và hoàn thành Khóa luận.*

* **Tuần 17: Bộ dữ liệu Đánh giá (Eval Dataset)**
  * **Làm:** Xây dựng 100 câu hỏi chia 5 nhóm: *Answerable, Partially Answerable, Unanswerable, Misleading, Conflicting* (Như mục 5 trong PDF đề xuất). Tự gán nhãn Ground Truth.
* **Tuần 18: Chạy Đánh Giá Metrics (Ablation)**
  * **Làm:** Chạy tự động tập Test. So sánh hệ thống Verification của bạn với Baseline RAG thường. 
  * **Làm:** Lấy số liệu: Tỷ lệ Hallucination, Độ trễ (Latency), Chi phí (Cost). Vẽ biểu đồ.
* **Tuần 19: Viết Báo cáo Khóa luận (Drafting)**
  * **Làm:** Viết Chương Tổng quan, Cơ sở lý thuyết, và Phương pháp đề xuất (Vẽ flowchart các luồng API, Graph).
* **Tuần 20: Viết Thực nghiệm & Bảo vệ**
  * **Làm:** Viết phần Kết quả. Dựng Slide Bảo vệ. Quay 1 video Demo hệ thống Graphic mượt mà (5-8 phút). Chạy Mock-defense. Hoàn tất lộ trình!
