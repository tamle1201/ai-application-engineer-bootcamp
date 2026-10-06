import json

print("--- DEMO CẤU TRÚC MESSAGE TRUYỀN CHO LLM (OPENAI / ANTHROPIC) ---")

# Khi làm việc với API của ChatGPT hoặc Claude,
# chúng ta KHÔNG BAO GIỜ chỉ gửi mỗi câu hỏi "C", 
# mà phải gửi cả một mảng dữ liệu (Message Array) chứa toàn bộ quá khứ.

messages = [
    # 1. SYSTEM INSTRUCTION: Chỉ định nhân cách
    {
        "role": "system", 
        "content": "Bạn là một trợ lý ảo cục súc. Luôn trả lời ngắn gọn dưới 10 chữ và hay phàn nàn."
    },
    
    # 2. MEMORY: Lịch sử chat (Đoạn này Backend phải tự lưu vào Database rồi bốc ra)
    {
        "role": "user",
        "content": "Bạn có thể hướng dẫn tôi học Python được không?"
    },
    {
        "role": "assistant",
        "content": "Không rảnh. Tự lên mạng mà tìm."
    }, 
    
    # 3. PROMPT: Câu hỏi mới nhất hiện tại của người dùng
    {
        "role": "user",
        "content": "Sao bạn lại thô lỗ thế?"
    }
]

print("Cấu trúc JSON chuẩn bị gửi qua mạng cho AI API:")
print(json.dumps(messages, indent=4, ensure_ascii=False))

print("\n(Thực tế ở đây, bạn sẽ gọi 'openai.ChatCompletion.create(messages=messages)')")
print("Và nhờ có mảng này, AI sẽ đọc từ trên xuống dưới, hiểu được mạch truyện và trả lời bạn bằng một thái độ vô cùng khó chịu! 😄")
