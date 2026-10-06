import sqlite3

print("--- DEMO SQLITE DATABASE (TÍCH HỢP SẴN TRONG PYTHON) ---")

# 1. Kết nối DB (Nó sẽ tự tạo ra 1 file my_database.db trong thư mục này)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# 2. Tạo Bảng (Table)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')
print("✅ Đã khởi tạo bảng 'users'")

# 3. Thêm dữ liệu (INSERT) - Chỉ thêm nếu bảng đang trống để khỏi lặp dữ liệu
cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO users (name, role) VALUES ('Tâm', 'AI Engineer')")
    cursor.execute("INSERT INTO users (name, role) VALUES ('Hải', 'Backend')")
    conn.commit() # Bắt buộc phải commit để lưu vào đĩa
    print("✅ Đã thêm 2 User vào Database")

# 4. Đọc dữ liệu (SELECT)
print("\n📌 DANH SÁCH USER TRONG DATABASE:")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    # row là một tuple (id, name, role)
    print(f"ID: {row[0]} | Tên: {row[1]} | Chức vụ: {row[2]}")

# 5. Đóng kết nối
conn.close()
print("\n✅ Đã ngắt kết nối an toàn. (Bạn sẽ thấy 1 file 'my_database.db' sinh ra ở thư mục này)")
