# CLO 2: Trực quan hóa dữ liệu với Matplotlib & Seaborn

## Mục tiêu học tập
Bạn KHÔNG CẦN phải học thuộc lòng toàn bộ các hàm vẽ biểu đồ (vì trong thực tế làm việc AI sẽ viết code giúp bạn), nhưng bạn BẮT BUỘC phải hiểu các nguyên lý sau:
1. Khái niệm cơ bản về `Figure` và `Axes` trong một bức ảnh biểu đồ.
2. Biết ý nghĩa của từng loại biểu đồ để yêu cầu AI vẽ cho đúng: khi nào dùng biểu đồ đường (Line), cột (Bar), điểm (Scatter) hay biểu đồ tròn (Pie).
3. Thấy được sức mạnh khi tích hợp DataFrame của Pandas với Seaborn.

---

## 1. Matplotlib - Nền tảng cốt lõi của mọi biểu đồ
Matplotlib là thư viện vẽ biểu đồ lâu đời và cho phép tùy biến chi tiết nhất của Python. Nó cho phép bạn can thiệp vào từng pixel của bức ảnh (như đổi màu từng vạch chia, đổi font chữ, tọa độ).
- **Figure:** Khung tranh (tượng trưng cho toàn bộ bức ảnh tổng thể).
- **Axes:** Bức tranh con nằm trong khung tranh (một biểu đồ cụ thể). Một Figure có thể chứa nhiều Axes (nhiều biểu đồ xếp cạnh nhau).

## 2. Seaborn - Nghệ thuật vẽ biểu đồ
Nếu Matplotlib giống như việc bạn tự pha màu và vẽ tay, thì Seaborn giống như một phần mềm áp sẵn "filter" cực đẹp. Seaborn được xây dựng dựa trên nền của Matplotlib nhưng làm mọi thứ tự động hóa và có tính thẩm mỹ cao hơn rất nhiều. 

Đặc biệt, Seaborn sinh ra để chơi thân với `Pandas DataFrame`. Nếu bạn truyền một bảng dữ liệu Pandas vào Seaborn, nó sẽ tự động tính toán thống kê và vẽ ra những biểu đồ rực rỡ chỉ với 1 dòng code.

> 👉 **Lưu ý thực chiến (Quan trọng):** 
> Trong vai trò một AI Application Engineer, bạn hiếm khi phải tự gõ code Matplotlib từ con số 0. Thường bạn sẽ ra lệnh cho AI (như ChatGPT hoặc Github Copilot): *"Tôi có DataFrame df với cột A là Tên, cột B là Doanh Thu. Hãy vẽ cho tôi một biểu đồ Bar Chart bằng Seaborn, hiển thị số trên đỉnh cột, phối màu theo tone Xanh Đậm"*. 
> 
> Tuy nhiên, bạn phải có kiến thức nền tảng ở môn học này để đọc hiểu đoạn code mà AI tạo ra. Nếu màu sắc chưa vừa ý, hoặc chữ bị lệch, bạn phải biết chỗ nào để vào tinh chỉnh lại.

> 👉 **Hành động:** Mở `VD/02_data_visualization.py` lên và ấn nút Run. Code sẽ tự động chạy và lưu lại 2 bức ảnh biểu đồ (`.png`) siêu đẹp vào thẳng thư mục hiện tại để bạn chiêm ngưỡng thành quả!
