# CLO 1: Tính năng Python nâng cao (Advanced Python Features)

## Mục tiêu học tập (Course Learning Outcome 1)
Sau khi học xong tài liệu này và chạy thử code, bạn cần đạt được các kỹ năng:
1. **Type Hinting:** Biết cách khai báo kiểu dữ liệu rõ ràng để code an toàn, dễ bảo trì (chuẩn bị cho việc làm team lớn).
2. **Decorators:** Biết cách viết decorator để thêm tính năng (ví dụ: đo thời gian chạy, ghi log) vào một hàm mà không cần sửa code bên trong hàm đó.
3. **Generators (`yield`):** Biết cách xử lý dữ liệu siêu lớn (ví dụ đọc file vài GB) mà không bị tràn RAM.
4. **Context Managers:** Viết class sử dụng `__enter__` và `__exit__` (cú pháp `with`) để tự động đóng kết nối cơ sở dữ liệu hoặc đóng file.

---

## 1. Type Hinting (Khai báo kiểu dữ liệu)
Python là ngôn ngữ kiểu động (dynamic typing), nhưng trong dự án AI/Backend thực tế, chúng ta BẮT BUỘC phải dùng Type Hinting để IDE có thể gợi ý code và tránh bug ngớ ngẩn.

```python
from typing import List, Dict, Optional

# Nhìn vào hàm này, ta biết ngay đầu vào là list các chuỗi, đầu ra là một dictionary.
def process_data(users: List[str], age_limit: Optional[int] = None) -> Dict[str, bool]:
    pass
```

## 2. Decorators
Trong Python, hàm cũng là một object. Bạn có thể truyền hàm này vào hàm khác. Decorator dùng kí hiệu `@` để "bọc" một hàm, giúp bạn thực thi một số logic TRƯỚC và SAU khi hàm chính chạy.

Thường dùng cho: Kiểm tra quyền (Authorization), Logging, hoặc Retry tự động nếu gọi API thất bại.

## 3. Generators (Từ khóa `yield`)
Thay vì dùng `return` trả về toàn bộ mảng data, `yield` sẽ trả về *từng phần tử một*, sau đó tạm dừng hàm lại. 
Rất hữu ích khi bạn parse file log hàng triệu dòng, vì nó chỉ tốn vài MB RAM thay vì lưu toàn bộ vào RAM.

## 4. Context Managers
Bạn thường thấy `with open('file.txt') as f:`. Tại sao không dùng `f = open()`? Vì `with` đảm bảo file LUÔN ĐƯỢC ĐÓNG dù cho code bên trong có bị lỗi văng Exception đi chăng nữa. Bạn hoàn toàn có thể tự viết ra cú pháp `with` của riêng mình.

> 👉 **Hành động tiếp theo:** Hãy mở file `VD/01_advanced_features.py` và chạy thử để xem tận mắt cách các dòng code này hoạt động!
