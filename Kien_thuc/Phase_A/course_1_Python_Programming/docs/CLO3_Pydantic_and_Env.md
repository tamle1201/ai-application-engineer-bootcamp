# CLO 3: Tiêu chuẩn kỹ thuật đi làm (Virtual Env, Pydantic, Dotenv)

## Mục tiêu học tập
Sau khi học xong phần này, bạn sẽ trang bị được thói quen code chuẩn của một kĩ sư phần mềm thực thụ:
1. Sử dụng **Virtual Environment (`venv`)** để cách ly các dự án không bị xung đột thư viện.
2. Bảo mật thông tin nhạy cảm bằng **Biến môi trường (`.env`)**.
3. Ép kiểu dữ liệu nghiêm ngặt bằng **`Pydantic`** (Vũ khí tối thượng khi làm việc với LLMs và xây dựng API bằng FastAPI).

---

## 1. Môi trường ảo (Virtual Environment)
Khi bạn làm 10 dự án AI khác nhau, bạn có thể cần 10 phiên bản thư viện khác nhau. Nếu cài chung toàn bộ trên máy (bằng `pip install`), chúng sẽ "đánh nhau" gây lỗi phiên bản.
**Cách làm chuẩn:**
- Tạo môi trường ảo riêng cho project: `python -m venv venv`
- Kích hoạt (Trên Windows): `.\venv\Scripts\activate`
- Lúc này chữ `(venv)` sẽ hiện lên ở terminal. Kể từ giờ bạn có thể cài đặt thư viện thoải mái mà không sợ rác máy: `pip install pydantic python-dotenv`
- (Khi code xong, để thoát ra: gõ `deactivate`)

## 2. Bảo mật với Dotenv (`.env`)
Tuyệt đối KHÔNG BAO GIỜ viết key OpenAI vào thẳng file code như thế này: `api_key = "sk-12345..."`
Lý do: Nếu bạn push code lên Github, hacker có con bọ (bot) rà quét tự động sẽ đánh cắp key của bạn và xài chùa hết tiền chỉ trong vài phút.
**Cách giải quyết:**
1. Tạo một file tên là `.env` ngang hàng với file code.
2. Viết vào đó: `OPENAI_API_KEY=sk-12345...`
3. Đảm bảo file `.env` đã được liệt kê trong file `.gitignore` (để Git bỏ qua, không push lên mạng).
4. Dùng thư viện `python-dotenv` để đọc key này lên bộ nhớ RAM một cách an toàn lúc code chạy.

## 3. Pydantic (Data Validation)
Pydantic là một thư viện giúp kiểm tra tính hợp lệ của dữ liệu cực kỳ mạnh mẽ.
Trong AI Application Engineer, mô hình AI (như ChatGPT) thường hay "ảo giác" và trả lời lung tung. Bạn sẽ dùng Pydantic để dựng lên một cái "khuôn", ép AI phải trả ra data khớp 100% với cái khuôn đó (Ví dụ bắt buộc phải có thuộc tính `name` là chuỗi, `age` là số lớn hơn 0).

> 👉 **Hành động:** 
> 1. Cài đặt thư viện: `pip install pydantic python-dotenv`
> 2. Mở chạy file `VD/03_pydantic_env_demo.py` để xem Pydantic bắt lỗi dữ liệu rác xịn như thế nào!
