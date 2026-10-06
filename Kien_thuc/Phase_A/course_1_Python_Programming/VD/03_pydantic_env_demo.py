import os
from pydantic import BaseModel, ValidationError, Field
from dotenv import load_dotenv

# ==========================================
# 1. ĐỌC BIẾN MÔI TRƯỜNG AN TOÀN (.env)
# ==========================================
print("--- 1. BẢO MẬT BIẾN MÔI TRƯỜNG ---")
# Hàm load_dotenv() sẽ tìm file .env trong thư mục và tải các biến vào bộ nhớ
load_dotenv()

# Lấy biến ra xài bằng os.getenv. Nếu không có sẽ lấy giá trị mặc định bên phải.
api_key = os.getenv("OPENAI_API_KEY", "Chưa có key (nhưng an toàn!)")
print(f"API Key đang được bảo mật: {api_key}\n")


# ==========================================
# 2. PYDANTIC - ÉP KIỂU DỮ LIỆU CỰC KỲ CHẶT CHẼ
# ==========================================
print("--- 2. PYDANTIC DATA VALIDATION ---")

# Tạo một cái "Khuôn" (Model) bằng Pydantic
class UserProfile(BaseModel):
    name: str
    age: int = Field(..., gt=0, description="Tuổi bắt buộc phải lớn hơn 0")
    email: str

# TRƯỜNG HỢP 1: Dữ liệu chuẩn (Giả lập khi AI trả về JSON đúng cấu trúc)
valid_data = {
    "name": "Lê Văn Tâm",
    "age": 25,
    "email": "tamle@gmail.com"
}
try:
    user = UserProfile(**valid_data)
    print("✅ Dữ liệu hợp lệ!")
    print(f"Tạo object thành công: Tên: {user.name}, Tuổi: {user.age}")
except ValidationError as e:
    print("❌ Lỗi dữ liệu:", e)


print("\n" + "-" * 30 + "\n")


# TRƯỜNG HỢP 2: Dữ liệu rác (Giả lập khi Hacker tấn công hoặc AI bị ảo giác)
invalid_data = {
    "name": "Hacker",
    "age": -5,      # Lỗi: tuổi bị âm
    "email": 12345  # Lỗi: email phải là chuỗi (str) chứ không phải số
}
try:
    print("⏳ Đang thử parse dữ liệu lỗi...")
    user2 = UserProfile(**invalid_data)
except ValidationError as e:
    print("🚫 Pydantic đã phát hiện lỗi và chặn đứng dữ liệu rác! Chi tiết:")
    print(e)
