# CLO 1: Kiến trúc mô hình LLM cơ bản

## Mục tiêu học tập
Ở góc độ **Application Engineer** (kỹ sư ứng dụng, đứng trên vai người khổng lồ), bạn KHÔNG CẦN biết Toán học phức tạp để tự train mô hình LLM từ con số 0. Nhưng bạn cần hiểu "cách cái máy nó vận hành" để tối ưu hóa Prompt và tiết kiệm chi phí.

---

## 1. LLM thực chất là "Máy dự đoán từ tiếp theo"
ChatGPT không có tư duy, không có cảm xúc. Nó đơn giản chỉ là một cỗ máy thống kê siêu hạng. Dựa trên chuỗi từ (Prompt) bạn nhập vào, nó sẽ tính toán xác suất xem **"từ tiếp theo"** phù hợp nhất là gì.
- VD: Bạn nhập "Hôm nay trời đẹp..." -> Toán học LLM tính ra xác suất từ tiếp theo là "quá" (80%), "nhiều" (10%), "nhỉ" (5%). Khả năng cao nó sẽ sinh ra chữ "quá".

## 2. Token và Context Window
- **Token:** AI không đọc theo từng chữ cái (word), mà nó cắt chữ thành những Token. 
  - Trong tiếng Anh, 1 chữ thường bằng 1 Token (VD: "Apple"). 
  - Nhưng tiếng Việt có dấu, chữ "Bình thường" có thể tốn tới 3-4 Token.
  - **Vì sao phải biết?** Vì các công ty như OpenAI tính tiền API dựa trên số Token bạn gửi đi và nhận về. Viết Prompt tiếng Anh sẽ tiết kiệm tiền hơn tiếng Việt!
- **Context Window:** Kích thước "bộ nhớ làm việc" của LLM. (VD: GPT-4 có giới hạn 128.000 Tokens, tương đương khoảng 300 trang sách). Nếu tài liệu RAG bạn bơm vào vượt quá 128k, nó sẽ báo lỗi và từ chối trả lời.

## 3. Attention Mechanism (Cơ chế chú ý)
Đây là công nghệ cốt lõi tạo nên sự vĩ đại của ChatGPT (kiến trúc Transformer ra đời năm 2017).
Khi AI đọc câu: *"Con mèo trèo lên cây vì con chó đuổi theo nó"*.
Cơ chế Attention (Toán học Ma trận) giúp AI "chú ý" và hiểu chữ **"nó"** ở đây đang trỏ về **"con mèo"** chứ không phải "con chó" hay "cái cây". 

> 👉 **Bài học:** Chính nhờ cơ chế này, bạn càng cung cấp Context (ngữ cảnh) chi tiết và mạch lạc trong Prompt, hệ thống Attention của LLM càng "bắt" đúng ý và trả lời chuẩn xác. Viết Prompt mơ hồ sẽ làm "nhiễu" bộ máy Attention của nó.
