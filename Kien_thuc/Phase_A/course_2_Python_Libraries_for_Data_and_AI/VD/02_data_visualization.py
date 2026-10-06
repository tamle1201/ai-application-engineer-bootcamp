import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# CHUẨN BỊ DỮ LIỆU (BẰNG PANDAS)
# ==========================================
data = {
    'Tháng': ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5'],
    'Doanh_thu': [150, 200, 180, 250, 300],
    'Lợi_nhuận': [50, 70, 60, 90, 120]
}
df = pd.DataFrame(data)


# ==========================================
# 1. VẼ BIỂU ĐỒ BẰNG MATPLOTLIB (Biểu đồ đường)
# ==========================================
print("Đang vẽ biểu đồ đường bằng Matplotlib...")
plt.figure(figsize=(8, 5)) # Đặt kích thước khung tranh (Figure)

# Vẽ 2 đường doanh thu và lợi nhuận
plt.plot(df['Tháng'], df['Doanh_thu'], marker='o', label='Doanh thu', color='blue')
plt.plot(df['Tháng'], df['Lợi_nhuận'], marker='s', label='Lợi nhuận', color='green')

# Trang trí biểu đồ
plt.title('Biểu Đồ Doanh Thu & Lợi Nhuận (Matplotlib)')
plt.xlabel('Thời gian')
plt.ylabel('Triệu VNĐ')
plt.legend() # Hiển thị chú thích
plt.grid(True) # Hiện lưới cho dễ nhìn

# Lưu thành file ảnh (Thay vì bật cửa sổ Pop-up)
matplotlib_file = '01_matplotlib_chart.png'
plt.savefig(matplotlib_file)
plt.close()
print(f"✅ Đã lưu file: {os.path.abspath(matplotlib_file)}\n")


# ==========================================
# 2. VẼ BIỂU ĐỒ BẰNG SEABORN (Biểu đồ cột)
# ==========================================
print("Đang vẽ biểu đồ cột bằng Seaborn...")
plt.figure(figsize=(8, 5))

# Seaborn tự động phối màu bảng 'viridis' cực kì đẹp mắt
# Chỉ cần ném dataframe df vào và chỉ định cột x, y
sns.barplot(x='Tháng', y='Doanh_thu', data=df, palette='viridis')

# Vẫn dùng Matplotlib để cấu hình thêm title
plt.title('Biểu Đồ Cột Doanh Thu (Seaborn)')
plt.ylabel('Triệu VNĐ')

seaborn_file = '02_seaborn_chart.png'
plt.savefig(seaborn_file)
plt.close()
print(f"✅ Đã lưu file: {os.path.abspath(seaborn_file)}\n")

print("🎉 Hoàn tất! Hãy mở 2 file ảnh .png vừa được tạo ra ở thư mục hiện tại để xem kết quả nhé.")
