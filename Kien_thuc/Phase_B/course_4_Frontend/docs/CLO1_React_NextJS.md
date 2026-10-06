# CLO 1: Frontend (ReactJS & NextJS)

## Mục tiêu học tập
1. Hiểu khái niệm Component trong React.
2. Quản lý trạng thái bằng `useState`.
3. Tích hợp Tailwind CSS để làm đẹp giao diện.

---

## 1. Bản chất của ReactJS (Component)
Lập trình web ngày xưa (HTML thuần) là viết một cục code khổng lồ. 
ReactJS thay đổi tư duy này: Mọi thứ trên trang web đều là những mảnh ghép Lego (gọi là Component).
- Thanh điều hướng (Navbar) là 1 mảnh lego.
- Nút bấm (Button) là 1 mảnh lego.
- Bạn ghép chúng lại với nhau thành 1 trang web hoàn chỉnh.

## 2. Tại sao lại dùng NextJS?
NextJS là một "Bộ khung" (Framework) bọc ngoài ReactJS. 
- Mặc định ReactJS chỉ chạy trên máy khách (Client). Nó rất tệ cho SEO (Search Engine) vì Google Bot không đọc được nội dung lúc trang vừa load.
- NextJS hỗ trợ **Server-Side Rendering (SSR)**. Nó biên dịch sẵn trang web ở máy chủ rồi mới gửi về, giúp web load siêu nhanh và SEO đỉnh cao.
- NextJS có chuẩn **App Router**, tự động tạo đường dẫn (URL) bằng thư mục, không cần tự tay viết file routing cực nhọc.

## 3. Tailwind CSS
Tailwind là thư viện CSS dạng "Utility-first". Thay vì phải mở file `style.css` và viết code CSS riêng cho từng thành phần. Bạn gõ trực tiếp thuộc tính CSS vào thẳng thẻ HTML qua class.
Ví dụ: Nút màu xanh, viền cong, chữ trắng.
- Cũ: `<button class="btn-primary">` rồi sang file css viết `background: blue; border-radius: 5px; color: white;`
- Tailwind: `<button class="bg-blue-500 rounded-md text-white">` 

> 💡 **Với Frontend:** Chúng ta sẽ không viết script mẫu bằng file Python như các phần trước. Ở giai đoạn Running Project của Phase B, bạn sẽ tự tay dùng lệnh `npx create-next-app` để dựng 1 project Frontend thực tế và kết nối nó với FastAPI backend.
