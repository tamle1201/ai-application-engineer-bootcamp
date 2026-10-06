from fastapi import FastAPI
from pydantic import BaseModel

# Khởi tạo ứng dụng FastAPI
app = FastAPI(title="My First AI Backend", version="1.0")

# --- 1. GET METHOD Cơ bản ---
@app.get("/")
def home():
    return {"message": "Chào mừng đến với Backend FastAPI đầu tiên của bạn!"}

# --- 2. GET METHOD với Path Parameter ---
# (Ví dụ url: /users/1)
@app.get("/users/{user_id}")
def get_user_info(user_id: int):
    # Trả về data (thực tế sẽ gọi Database ở đây)
    return {"user_id": user_id, "name": f"Người dùng số {user_id}"}

# --- 3. POST METHOD với Pydantic Validation ---
# Định nghĩa khuôn JSON đầu vào
class Item(BaseModel):
    name: str
    price: float
    description: str = None # Không bắt buộc

@app.post("/items/")
def create_item(item: Item):
    # Nhờ Pydantic, biến 'item' ở đây chắc chắn đã chuẩn cấu trúc. Không sợ lỗi rác.
    return {
        "status": "success",
        "message": f"Đã lưu sản phẩm {item.name}",
        "received_price": item.price
    }

# ==========================================
# CÁCH CHẠY SERVER:
# Mở terminal ở đúng thư mục này và gõ:
# uvicorn 01_fastapi_app:app --reload
# Sau đó vào trình duyệt xem: http://127.0.0.1:8000/docs
# ==========================================
