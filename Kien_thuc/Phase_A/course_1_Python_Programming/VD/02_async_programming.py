import asyncio
import time

# ==========================================
# HÀM GIẢ LẬP GỌI API (TỐN THỜI GIAN)
# ==========================================
async def call_openai_api(task_id: int, delay_seconds: int):
    """
    Giả lập một tác vụ I/O bound (ví dụ: gọi API LLM tốn thời gian).
    Từ khóa 'async' báo hiệu đây là một Coroutine.
    """
    print(f"⏳ Tác vụ {task_id}: Đang gọi OpenAI API (Mất {delay_seconds}s)...")
    
    # Từ khóa 'await' nhường quyền điều khiển lại cho Event Loop
    # Trong lúc hàm này đang 'ngủ', Event Loop sẽ chạy các hàm khác!
    await asyncio.sleep(delay_seconds) 
    
    print(f"✅ Tác vụ {task_id}: Hoàn thành!")
    return f"Result_{task_id}"


# ==========================================
# CHẠY ĐỒNG BỘ (SYNC - CHẬM) - ĐỂ SO SÁNH
# ==========================================
async def run_sync_style():
    print("\n--- CHẠY TUẦN TỰ (SYNC STYLE) ---")
    start = time.time()
    
    # Chờ tác vụ 1 xong mới chạy tác vụ 2
    await call_openai_api(1, 2)
    await call_openai_api(2, 3)
    await call_openai_api(3, 1)
    
    end = time.time()
    print(f"> Tổng thời gian chạy tuần tự: {end - start:.2f} giây")
    # Tổng thời gian sẽ là 2 + 3 + 1 = 6 giây!


# ==========================================
# CHẠY BẤT ĐỒNG BỘ (ASYNC - NHANH)
# ==========================================
async def run_async_style():
    print("\n--- CHẠY ĐỒNG THỜI (ASYNC STYLE) ---")
    start = time.time()
    
    # Gom tất cả tác vụ lại và chạy cùng một lúc (concurrently)
    tasks = [
        call_openai_api(4, 2),
        call_openai_api(5, 3),
        call_openai_api(6, 1)
    ]
    
    # asyncio.gather sẽ kích hoạt tất cả chạy đồng thời
    results = await asyncio.gather(*tasks)
    
    end = time.time()
    print(f"> Kết quả trả về: {results}")
    print(f"> Tổng thời gian chạy bất đồng bộ: {end - start:.2f} giây")
    # Tổng thời gian chỉ bằng tác vụ lâu nhất = 3 giây! (Nhanh gấp đôi)


# ==========================================
# HÀM MAIN EVENT LOOP
# ==========================================
async def main():
    await run_sync_style()
    await run_async_style()

if __name__ == "__main__":
    # Khởi tạo Event Loop của Python
    asyncio.run(main())
