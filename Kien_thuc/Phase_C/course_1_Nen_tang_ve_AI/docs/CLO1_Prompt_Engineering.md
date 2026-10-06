# CLO 1: Kiến trúc Nền tảng của một AI/LLM

## Mục tiêu học tập
1. Nắm được cách giao tiếp với LLM (Large Language Model) một cách có hệ thống, không chỉ là chat hỏi đáp thông thường.
2. Phân biệt được các khái niệm: Instruction, Prompt, Context, Memory, Skill, Hook.

---

## Các thành phần cấu tạo nên một "Bộ não" AI 
Khi xây dựng ứng dụng AI, để AI trả lời chính xác, thông minh và không bịa chuyện (Hallucination), ta phải cung cấp cho nó một môi trường gồm 6 yếu tố:

1. **System Instruction (Chỉ thị hệ thống):**
   - Đóng vai trò định hình "nhân cách", "giọng điệu" và "luật lệ cốt lõi" của AI. 
   - Ví dụ: *"Ngươi là một chuyên gia lập trình Python, chỉ được phép trả lời bằng code, cấm nói lý thuyết."*

2. **Prompt (Câu lệnh người dùng):**
   - Lệnh yêu cầu hoặc câu hỏi trực tiếp từ người dùng.
   - Ví dụ: *"Hãy viết cho tôi vòng lặp for."*

3. **Context (Ngữ cảnh):**
   - Dữ liệu nền được cung cấp cho AI trước khi nó đưa ra câu trả lời (Đây chính là linh hồn của hệ thống RAG).
   - Ví dụ: Nhét toàn bộ nội dung tài liệu nội bộ công ty vào làm Context, AI sẽ đọc Context này để trả lời câu hỏi của nhân viên.

4. **Memory (Bộ nhớ):**
   - LLM bản chất bị "mất trí nhớ" (Stateless) sau mỗi tin nhắn. Memory là kĩ thuật lưu lại toàn bộ lịch sử đoạn chat ở Backend và gửi kèm lại cho LLM mỗi lần hỏi mới để nó nhớ bạn là ai và đang nói về chủ đề gì.

5. **Skill (Kỹ năng) / Tools / Function Calling:**
   - Cấp cho AI quyền thực thi hành động bên ngoài. (Ví dụ: AI không biết thời tiết hôm nay, ta cung cấp cho nó Skill `get_weather_api()`. AI sẽ tự động phân tích và gọi hàm này lấy dữ liệu rồi mới phản hồi cho người dùng).

6. **Hook:**
   - Các điểm chèn mã (code) để can thiệp vào luồng suy nghĩ của AI. Ví dụ: Hook trước khi gửi câu hỏi để kiểm tra xem có từ ngữ nhạy cảm không.

> 👉 **Hành động:** Xem file `VD/01_prompt_engineering_demo.py` để hiểu tận mắt cách truyền Instruction và Memory vào API của các LLM như OpenAI!
