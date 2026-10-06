# CLO 1: Kiến trúc Ứng dụng AI (AI Application Architecture)

## Mục tiêu học tập
Hiểu cách thiết kế một hệ thống phần mềm có tích hợp AI sao cho chuẩn chỉnh, dễ bảo trì, dễ thay đổi mô hình AI và chịu tải tốt.

## Các thành phần của Kiến trúc AI
Thay vì nhét toàn bộ code gọi OpenAI vào chung một đống lộn xộn, kiến trúc AI chuẩn (Industry Standard) chia hệ thống thành nhiều tầng (Layers) tách biệt:

1. **Frontend Layer (Giao diện):** 
   - Thường viết bằng React/NextJS. Là nơi người dùng nhắn tin (như giao diện của ChatGPT).
2. **Gateway/API Layer:** 
   - Thường viết bằng FastAPI. Làm nhiệm vụ tiếp nhận yêu cầu từ Frontend, kiểm tra quyền truy cập (Login/Token).
3. **Orchestration Layer (Trái tim của hệ thống):** 
   - Nơi chứa logic điều phối AI. Thường sử dụng các framework như `LangChain` hoặc `LlamaIndex` để kết nối các thành phần lại với nhau.
4. **Data & Retrieval Layer (RAG/Vector DB):** 
   - Nơi xử lý và lưu trữ tài liệu đã được nhúng (Embedding) vào Vector Database (ChromaDB, Pinecone, Qdrant).
5. **Model Layer (Đáy tầng):** 
   - Nơi thực hiện lời gọi API tới các mô hình LLM (OpenAI GPT-4, Anthropic Claude 3.5, Google Gemini).

> 👉 **Triết lý thiết kế (Design Philosophy):** 
> "LLM chỉ là cái bóng đèn, Orchestration Layer mới là mạng điện". Đừng bao giờ phụ thuộc 100% vào một mô hình LLM duy nhất (ví dụ OpenAI). Hãy thiết kế kiến trúc sao cho hôm nay dùng OpenAI, ngày mai OpenAI sập, bạn chỉ mất 1 dòng code để đổi sang dùng Claude!
