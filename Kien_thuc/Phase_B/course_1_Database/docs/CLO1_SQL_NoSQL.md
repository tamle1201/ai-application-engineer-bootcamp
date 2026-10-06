# CLO 1: Phân biệt và ứng dụng SQL vs No-SQL

## Mục tiêu học tập
1. Phân biệt được cơ sở dữ liệu quan hệ (SQL) và phi quan hệ (No-SQL).
2. Viết được các câu lệnh SQL cơ bản: `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
3. Hiểu khái niệm ORM (Object-Relational Mapping) để dùng Python thao tác với DB.

---

## 1. Cơ sở dữ liệu quan hệ (SQL - VD: PostgreSQL, MySQL, SQLite)
Lưu dữ liệu dưới dạng các BẢNG (có dòng và cột) và RÀNG BUỘC chặt chẽ. Phù hợp cho dữ liệu có cấu trúc (như quản lý đơn hàng, người dùng).

**Ví dụ lệnh SQL thần thánh:**
- Lấy tất cả user: `SELECT * FROM users;`
- Thêm user: `INSERT INTO users (name, age) VALUES ('Tam', 25);`
- Lấy user có tuổi > 20: `SELECT * FROM users WHERE age > 20;`

## 2. Cơ sở dữ liệu phi quan hệ (No-SQL - VD: MongoDB)
Lưu dữ liệu dưới dạng văn bản (Document) giống hệt định dạng JSON. Không có cột cố định.
Phù hợp cho dữ liệu lưu trữ không cố định (như lịch sử chat của LLM, log hệ thống).
```json
{
   "_id": 1,
   "name": "Tam",
   "messages": ["Xin chào", "Giúp tôi code Python"]
}
```

## 3. ORM (Object-Relational Mapping) là gì?
Trong thực tế, kĩ sư Python RẤT ÍT KHI gõ lệnh SQL thuần. Họ dùng **ORM (như SQLAlchemy)**.
Thay vì gõ: `SELECT * FROM users`, bạn gõ code Python: `db.query(User).all()`.
Hệ thống ORM sẽ tự động dịch câu lệnh Python của bạn thành lệnh SQL bên dưới để chạy. Nó giúp code an toàn (chống hacker SQL Injection) và dễ bảo trì.

> 👉 **Hành động:** Mở file `VD/01_sqlite_demo.py` để chạy thử một Database SQL thực tế ngay trên máy tính của bạn (bằng SQLite tích hợp sẵn).
