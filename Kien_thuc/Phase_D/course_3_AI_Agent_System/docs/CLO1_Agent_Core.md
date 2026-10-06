# CLO 1: Trợ lý AI tự chủ (AI Agent Core)

## Mục tiêu học tập
Hiểu sự khác biệt mang tính cách mạng giữa RAG truyền thống và AI Agent. Nắm được cơ chế ReAct (Reasoning and Acting).

---

## 1. RAG vs AI Agent
- **RAG (Thụ động):** Vòng đời 1 chiều. (Người dùng hỏi -> Rút tài liệu -> Trả lời). Nếu tài liệu không đủ, RAG sẽ bó tay hoặc nói "Tôi không biết".
- **AI Agent (Chủ động):** Vòng đời tuần hoàn có tư duy. (Người dùng giao việc -> AI tự Suy nghĩ -> AI quyết định lấy Công cụ (Tool) ra dùng -> AI quan sát kết quả -> Nếu chưa xong việc, AI tiếp tục suy nghĩ và gọi Tool khác).

## 2. Cơ chế ReAct (Reasoning + Acting)
Một Agent thông minh hoạt động dựa trên vòng lặp ReAct do các nhà nghiên cứu tạo ra:

**Ví dụ thực tế:** Người dùng ra lệnh: *"Thời tiết Hà Nội nay thế nào, và cho tôi biết giá cổ phiếu VCB."*
* Hệ thống RAG sẽ gục ngã vì không có tài liệu về cổ phiếu.
* Nhưng hệ thống AI Agent sẽ tư duy theo các bước sau:

1. **Thought (Suy nghĩ 1):** "Người dùng hỏi thời tiết và chứng khoán. Mình không biết thông tin realtime. Mình cần tra thời tiết Hà Nội trước."
2. **Action (Hành động 1):** Kích hoạt Tool `get_weather_api(location="Hà Nội")`.
3. **Observation (Quan sát 1):** Tool trả về dữ liệu "Trời mưa, 25 độ".
4. **Thought (Suy nghĩ 2):** "Đã có thời tiết. Giờ cần tra chứng khoán mã VCB."
5. **Action (Hành động 2):** Kích hoạt Tool `get_stock_price(symbol="VCB")`.
6. **Observation (Quan sát 2):** Tool trả về dữ liệu "Giá 90.000đ".
7. **Final Answer (Trả lời cuối):** "Hôm nay Hà Nội trời mưa 25 độ. Giá cổ phiếu VCB đang là 90.000đ nhé."

> 🚀 **Nhận định:** AI Agent chính là tương lai của mọi phần mềm! Nó biến AI từ chỗ chỉ "giải đáp thắc mắc" thành "tự động hóa công việc".
