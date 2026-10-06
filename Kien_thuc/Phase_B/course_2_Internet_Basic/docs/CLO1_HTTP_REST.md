# CLO 1: Internet Basic & RESTful API

## Mục tiêu học tập
1. Hiểu cách Internet hoạt động ở mức cơ bản (Client - Server).
2. Hiểu cấu trúc của một HTTP Request & HTTP Response.
3. Biết cách dùng JSON làm chuẩn giao tiếp.

---

## 1. Client - Server Model
- **Client (Khách hàng):** Trình duyệt web (Chrome), hoặc App điện thoại, hoặc code ReactJS. Là nơi gửi yêu cầu.
- **Server (Nhà hàng):** Máy chủ chạy code Python/FastAPI của bạn để xử lý yêu cầu và trả về kết quả.

## 2. Giao thức HTTP
Khi Client và Server nói chuyện với nhau, chúng dùng ngôn ngữ chung là HTTP.
**Các Phương thức (Method) phổ biến:**
- `GET`: Lấy dữ liệu về (VD: Xem danh sách bài viết).
- `POST`: Gửi dữ liệu lên để tạo mới (VD: Bấm nút Đăng ký tài khoản).
- `PUT`: Cập nhật dữ liệu cũ (VD: Đổi mật khẩu).
- `DELETE`: Xóa dữ liệu.

**Mã trạng thái (Status Code):** Để biết gọi API có thành công không.
- `200`: OK (Thành công mĩ mãn).
- `400`: Bad Request (Lỗi do Client gửi thiếu/sai data).
- `404`: Not Found (Không tìm thấy URL).
- `500`: Internal Server Error (Lỗi do code Backend của bạn bị sập).

## 3. JSON - Chuẩn giao tiếp toàn cầu
Máy chủ và Trình duyệt chạy 2 ngôn ngữ khác nhau (VD: Server chạy Python, Client chạy Javascript). Để hiểu nhau, chúng chuyển đổi dữ liệu thành chữ (String) theo định dạng JSON.
```json
{
  "status": "success",
  "data": {
    "user": "Tam",
    "role": "Admin"
  }
}
```

> 👉 **Hành động:** Bạn có thể phải chạy lệnh `pip install requests` trước khi mở file `VD/01_http_request.py` để xem cách Python đóng vai Client đi gọi API mạng internet!
