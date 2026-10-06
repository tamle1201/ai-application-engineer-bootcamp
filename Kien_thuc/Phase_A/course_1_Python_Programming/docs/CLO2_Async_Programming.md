# CLO 2: Lập trình bất đồng bộ (Asyncio)

## Mục tiêu học tập (Course Learning Outcome 2)
Sau khi hoàn thành phần này, bạn cần hiểu và làm được:
1. Phân biệt được sự khác nhau giữa **Đồng bộ (Synchronous)** và **Bất đồng bộ (Asynchronous)**.
2. Nắm được khái niệm **Event Loop** (Vòng lặp sự kiện).
3. Sử dụng thành thạo từ khóa `async def` và `await` để gọi nhiều API/Database cùng lúc mà không bị block.

---

## 1. Sync vs Async là gì?
- **Sync (Đồng bộ):** Bạn làm việc A, chờ việc A xong hẳn mới làm việc B. (Ví dụ: Đặt trà sữa, đứng chờ quán pha xong đưa cho bạn, rồi bạn mới đi mua bánh mì).
- **Async (Bất đồng bộ):** Bạn đặt trà sữa, lấy số thứ tự, trong lúc chờ họ pha thì bạn chạy đi mua bánh mì. Mua xong quay lại lấy trà sữa. Cùng 1 khoảng thời gian nhưng làm được 2 việc.

Trong AI Application, bạn sẽ thường xuyên phải gọi API của OpenAI/LLMs (thường mất 5-10 giây trả lời) hoặc chọc vào Vector Database. Nếu dùng Sync, app của bạn sẽ bị "treo" cứng 10s. Nếu dùng Async, app của bạn vẫn có thể phục vụ hàng ngàn người dùng khác trong lúc chờ OpenAI.

## 2. Các khái niệm cốt lõi trong Python Asyncio
* `async def`: Khai báo một hàm là hàm bất đồng bộ (Coroutine).
* `await`: Tạm dừng hàm hiện tại, nhường quyền kiểm soát (control) lại cho Event Loop để đi làm việc khác, chờ đến khi có kết quả thì quay lại chạy tiếp.
* `asyncio.gather()`: Chạy đồng thời (concurrently) nhiều tác vụ cùng một lúc.

> 👉 **Hành động tiếp theo:** Mở file `VD/02_async_programming.py` lên, chạy thử và chú ý quan sát thứ tự in ra màn hình cũng như tổng thời gian thực thi để cảm nhận sức mạnh của Async!
