# CLO 1: Xử lý dữ liệu đa chiều với Numpy & Pandas

## Mục tiêu học tập
Sau khi hoàn thành tài liệu này, bạn có thể:
1. Hiểu được tại sao `Numpy` lại xử lý số liệu nhanh hơn cấu trúc List thông thường của Python.
2. Nắm vững cấu trúc mảng đa chiều `N-dimensional Array (ndarray)` của Numpy.
3. Làm chủ `Pandas DataFrame` - công cụ mạnh mẽ nhất để thao tác với dữ liệu dạng bảng (giống như thao tác trên Excel nhưng bằng code).
4. Biết cách đọc/ghi file (CSV/JSON), lọc dữ liệu, xử lý dữ liệu bị thiếu (Missing Values), và gom nhóm (Groupby).

---

## 1. Numpy - Cỗ máy tính toán siêu tốc
Numpy (Numerical Python) là thư viện tính toán toán học. Khác với mảng (List) bình thường của Python, Numpy array được viết bằng ngôn ngữ C ở bên dưới, nên tốc độ tính toán nhanh hơn gấp hàng chục đến hàng trăm lần.

Trong AI (đặc biệt là khi làm việc với RAG, Embedding, Vector Search), dữ liệu của bạn thực chất là các ma trận số khổng lồ. Numpy sinh ra là để tối ưu hóa việc xử lý các ma trận này.

## 2. Pandas - "Excel" của lập trình viên AI
Nếu Numpy là cốt lõi tính toán, thì Pandas là lớp áo giúp bạn thao tác với dữ liệu cực kì trực quan. Pandas chia dữ liệu làm 2 dạng chính:
- **Series:** Một cột dữ liệu (như mảng 1 chiều).
- **DataFrame:** Bảng dữ liệu có nhiều dòng và nhiều cột (tương tự như 1 sheet trong phần mềm Excel).

### Các thao tác "kinh điển" cần thuộc lòng với Pandas:
1. **Đọc dữ liệu:** `df = pd.read_csv("data.csv")` hoặc `pd.read_json("data.json")`
2. **Xem nhanh dữ liệu:** `df.head(5)` (xem 5 dòng đầu tiên), `df.info()` (kiểm tra kiểu dữ liệu các cột xem có bị lỗi định dạng không).
3. **Lọc dữ liệu:** `df[df['age'] > 18]` (Giữ lại những người trên 18 tuổi).
4. **Xử lý dữ liệu hỏng:** Trong thực tế, dữ liệu thu thập được thường xuyên bị trống. Bạn có thể dùng `df.dropna()` (Xóa các dòng chứa giá trị rỗng - NaN) hoặc `df.fillna(0)` (Điền số 0/hoặc giá trị trung bình vào các ô rỗng).
5. **Gom nhóm (Groupby):** Tương tự như công cụ Pivot Table của Excel. `df.groupby('department')['salary'].mean()` (Tính lương trung bình của từng phòng ban).

> 👉 **Hành động:** Hãy mở file `VD/01_data_processing.py` để chạy thử và tự tay xem các lệnh biến đổi một bảng dữ liệu giả lập diễn ra như thế nào!
