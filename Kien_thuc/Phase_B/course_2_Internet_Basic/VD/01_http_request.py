import requests
import json

print("--- DEMO GỌI API INTERNET (HTTP GET) ---")

# Chúng ta sẽ gọi một API công khai (Public API) có sẵn trên mạng để lấy danh sách Users giả
url = "https://jsonplaceholder.typicode.com/users/1"

print(f"Đang gửi HTTP GET Request tới: {url} ...")
response = requests.get(url)

# In ra Status Code để xem có thành công không
print(f"📌 Status Code: {response.status_code}")

if response.status_code == 200:
    print("✅ Kết nối thành công!")
    
    # Ép kiểu dữ liệu trả về thành dạng Dictionary của Python (từ chuỗi JSON)
    data = response.json()
    
    print("\n📌 Dữ liệu nhận được (Đã chuyển thành định dạng JSON dễ nhìn):")
    print(json.dumps(data, indent=4, ensure_ascii=False))
    
    print("\n📌 Trích xuất một số trường:")
    print(f"👤 Tên người dùng: {data['name']}")
    print(f"📧 Email: {data['email']}")
    print(f"🏢 Tên công ty: {data['company']['name']}")
else:
    print("❌ Có lỗi xảy ra khi kết nối tới API.")
