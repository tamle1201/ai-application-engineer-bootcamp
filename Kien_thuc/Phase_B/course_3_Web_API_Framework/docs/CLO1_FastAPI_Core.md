# CLO 1: FastAPI Core (Backend Framework)

## Mục tiêu học tập
1. Cài đặt và khởi chạy một Web Server bằng FastAPI.
2. Viết được API (Routing) cho phép Client gọi tới.
3. Nhận dữ liệu đầu vào (Path Parameters, Query Parameters, JSON Body).

---

## 1. Tại sao là FastAPI?
Cùng với Flask và Django, FastAPI là framework Python phổ biến nhất hiện nay.
**Điểm mạnh cực lớn:**
- Hỗ trợ `Async/Await` mặc định (Xử lý hàng vạn request cùng lúc không bị giật lag).
- Tích hợp sâu với `Pydantic` (Ép kiểu dữ liệu nghiêm ngặt).
- **Tự động sinh ra tài liệu API (Swagger UI)** siêu đẹp ở URL `/docs`, giúp bạn không bao giờ phải hì hục gõ tài liệu hướng dẫn cho đội Frontend nữa!

## 2. Kiến trúc cơ bản
Để viết 1 API, bạn chỉ cần 3 dòng code:
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

- `@app.get("/")`: Đây là **Route** (Định tuyến). Khi ai đó vào trang chủ `localhost:8000/`, nó sẽ chạy hàm bên dưới.
- Hàm `read_root`: Thực thi logic (Có thể truy vấn DB ở đây).
- Giá trị `return`: FastAPI tự động chuyển hóa dictionary (Dict) thành định dạng JSON chuẩn để gửi về cho Client.

> 👉 **Hành động:** 
> 1. Mở terminal, chạy lệnh cài đặt: `pip install fastapi uvicorn`
> 2. Chạy file `VD/01_fastapi_app.py` bằng lệnh: `uvicorn 01_fastapi_app:app --reload`
> 3. Mở trình duyệt web của bạn và gõ `http://127.0.0.1:8000/docs` để chiêm ngưỡng sự vi diệu của Swagger UI!
