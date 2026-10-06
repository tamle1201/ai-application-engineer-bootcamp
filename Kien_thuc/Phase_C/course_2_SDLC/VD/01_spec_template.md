# TÀI LIỆU YÊU CẦU DỰ ÁN (SPEC) DÀNH CHO AI
*(Đây là mẫu Spec để bạn ra lệnh cho AI. Hãy ném toàn bộ văn bản này vào ChatGPT / Cursor)*

## 1. Tổng quan dự án
- **Tên dự án:** Web API Quản lý công việc cá nhân (Todo List).
- **Công nghệ cốt lõi:** Python, FastAPI, SQLite, Pydantic.
- **Mục tiêu:** Tạo ra một API cho phép tạo và lấy danh sách công việc.

## 2. Cấu trúc Database (Models)
Sử dụng SQLAlchemy để thiết kế bảng `tasks` như sau:
- `id`: int, Khóa chính (Primary Key), tự tăng.
- `title`: string, Không được phép rỗng, tối đa 100 kí tự.
- `is_completed`: boolean, Mặc định là False.

## 3. Các API cần phát triển (Endpoints)
Cần viết 2 API sau trong hệ thống FastAPI:

1. **GET /tasks**
   - Chức năng: Lấy danh sách toàn bộ công việc.
   - Dữ liệu trả về: Mảng JSON chứa các task.
2. **POST /tasks**
   - Chức năng: Tạo công việc mới lưu vào Database.
   - Đầu vào (JSON body): Bắt buộc có trường `title`.
   - Trả về: Thông tin Task vừa tạo + Status Code 201 Created.
   
## 4. Yêu cầu kỹ thuật & Kiến trúc (Constraints)
- Phải dùng Pydantic Model để kiểm tra (validate) đầu vào của API POST, không được truyền thẳng biến vào hàm.
- Tách riêng logic xử lý Database ra một file `crud.py` riêng biệt.
- Không được viết tất cả code vào trong 1 file `main.py`.

---
**💡 Yêu cầu dành cho AI (System Prompt):** 
Đóng vai là một Senior Backend Developer, hãy đọc tài liệu Spec ở trên và sinh ra toàn bộ các file code chi tiết cho dự án này. Hãy cung cấp cấu trúc cây thư mục trước, sau đó in ra nội dung từng file code.
