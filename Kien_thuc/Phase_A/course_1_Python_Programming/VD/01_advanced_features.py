import time
from typing import List, Dict, Any

# ==========================================
# 1. TYPE HINTING
# ==========================================
def process_user_data(user_ids: List[int]) -> Dict[int, str]:
    print("--- 1. TYPE HINTING ---")
    result = {}
    for uid in user_ids:
        result[uid] = f"User_{uid}"
    print(f"Processed: {result}\n")
    return result


# ==========================================
# 2. DECORATORS
# ==========================================
def timer_decorator(func):
    """Một decorator dùng để đo thời gian chạy của hàm bất kỳ"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Bắt đầu chạy hàm: {func.__name__}")
        
        # Thực thi hàm gốc
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"Hàm {func.__name__} chạy mất: {end_time - start_time:.4f} giây\n")
        return result
    return wrapper

@timer_decorator
def heavy_computation():
    print("--- 2. DECORATOR ---")
    print("Đang tính toán nặng (giả lập sleep 1 giây)...")
    time.sleep(1)
    return "Done!"


# ==========================================
# 3. GENERATORS (yield)
# ==========================================
def large_file_reader_simulator():
    print("--- 3. GENERATORS ---")
    """Giả lập đọc 1 triệu dòng, nhưng chỉ trả về từng dòng một không làm đầy RAM"""
    for i in range(1, 4):
        yield f"Line {i} content..."

        
# ==========================================
# 4. CONTEXT MANAGERS (Cú pháp 'with')
# ==========================================
class MyDatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name

    def __enter__(self):
        print("--- 4. CONTEXT MANAGER ---")
        print(f"[DB] Đang mở kết nối tới database '{self.db_name}'...")
        return self # Đối tượng này sẽ được gán cho biến sau chữ 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[DB] Đã ngắt kết nối an toàn khỏi '{self.db_name}'!\n")

    def query(self, sql: str):
        print(f"[DB] Đang thực thi query: {sql}")


# ==========================================
# HÀM MAIN CHẠY THỬ
# ==========================================
if __name__ == "__main__":
    # Test Type Hinting
    process_user_data([101, 102])
    
    # Test Decorator
    heavy_computation()
    
    # Test Generator
    reader = large_file_reader_simulator()
    for line in reader:
        print(f"Đọc được: {line}")
    print("\n")
    
    # Test Context Manager
    with MyDatabaseConnection("AI_Vector_DB") as db:
        db.query("SELECT * FROM embeddings LIMIT 10")
        # Khi block code này kết thúc (hoặc dù có lỗi văng ra), hàm __exit__ luôn được gọi để đóng DB!
