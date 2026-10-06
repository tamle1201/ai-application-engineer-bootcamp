import numpy as np
import pandas as pd
import time

# ==========================================
# 1. NUMPY DEMO - TỐC ĐỘ TÍNH TOÁN
# ==========================================
print("--- 1. NUMPY TÍNH TOÁN SIÊU TỐC ---")

# Đo thời gian tính toán với List bình thường của Python
python_list = list(range(10000000)) # Mảng 10 triệu phần tử
start = time.time()
sum_list = sum(python_list)
end = time.time()
print(f"Dùng Python List mất: {end - start:.4f} giây")

# Đo thời gian tính toán với Numpy
numpy_array = np.arange(10000000)
start2 = time.time()
sum_numpy = np.sum(numpy_array)
end2 = time.time()
print(f"Dùng Numpy array mất: {end2 - start2:.4f} giây (Nhanh hơn rất nhiều!)\n")


# ==========================================
# 2. PANDAS DEMO - THAO TÁC VỚI BẢNG (Như Excel)
# ==========================================
print("--- 2. PANDAS DATA MANIPULATION ---")

# Tạo một DataFrame (Bảng dữ liệu) giả lập
data = {
    'Name': ['Tâm', 'Hải', 'Linh', 'Minh', 'Hoa'],
    'Age': [25, np.nan, 22, 28, 25], # Có 1 người bị thiếu tuổi (NaN)
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'IT'],
    'Salary': [1500, 1200, 1400, 1600, np.nan] # Có 1 người thiếu thông tin lương
}
df = pd.DataFrame(data)

print("📌 BẢNG DỮ LIỆU GỐC TRƯỚC KHI XỬ LÝ:")
print(df)
print("-" * 40)

# Xử lý dữ liệu hỏng: Điền dữ liệu bị thiếu (NaN)
print("📌 SAU KHI ĐIỀN THIẾU DỮ LIỆU:")
df['Age'] = df['Age'].fillna(df['Age'].mean()) # Lấy tuổi trung bình đắp vào chỗ trống
df['Salary'] = df['Salary'].fillna(1000)       # Điền lương mặc định là 1000
print(df)
print("-" * 40)

# Lọc dữ liệu: Chỉ lấy nhân viên thuộc phòng IT và trên 24 tuổi
print("📌 LỌC NHÂN SỰ IT VÀ LỚN HƠN 24 TUỔI:")
it_staff = df[(df['Department'] == 'IT') & (df['Age'] > 24)]
print(it_staff)
print("-" * 40)

# Gom nhóm (Groupby): Thống kê tổng tiền lương phải trả cho từng phòng ban
print("📌 TỔNG LƯƠNG TỪNG PHÒNG BAN:")
department_salary = df.groupby('Department')['Salary'].sum().reset_index()
print(department_salary)
