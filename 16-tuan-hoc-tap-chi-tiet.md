# Lịch trình Học tập 16 tuần (Cường độ cao: 8-10h/ngày)

> [!IMPORTANT]
> **Đây là lộ trình được tùy biến riêng cho người hổng nền tảng Software & Data Engineering, nhưng có quỹ thời gian rất lớn (56-70h/tuần).**
> Tuyệt đối không nhảy cóc qua Phase 1. Nếu bạn không rành Python và SQL, AI của bạn sẽ không bao giờ chạy ổn định trên môi trường thực tế (Production).

> [!TIP]
> **Khung giờ sinh hoạt khuyến nghị (Thứ 2 - Thứ 7, Chủ nhật nghỉ ngơi hoàn toàn):**
> - **Sáng (8h00 - 11h00):** Học lý thuyết, đọc tài liệu chính hãng (Docs), vẽ sơ đồ tư duy. Đầu óc minh mẫn nhất để nạp kiến thức khó.
> - **Chiều ca 1 (13h30 - 16h30):** Code Lab, thực hành gõ code, và **Gỡ lỗi (Debug)**. Đừng nản khi lỗi đỏ rực màn hình.
> - **Chiều ca 2 (17h00 - 19h00):** Tích hợp code thành Project nhỏ, hoặc làm bài tập SQL/Thuật toán trên LeetCode/HackerRank để luyện tư duy logic.
> - **Tối (20h30 - 21h30):** Review ngày học, cập nhật file nhật ký, đẩy code lên Github (commit), viết tài liệu (README). Lên danh sách việc ngày mai.

---

## Phase 1: Xây móng Lập trình và Data (Tuần 1 - Tuần 4)
*Đây là chặng quan trọng nhất. Nếu móng vững, học AI rất dễ.*

### Tuần 1: Lập trình Python Chuẩn Sản Phẩm (Production Python)
- **Ngày 1 (Type Hints & Pydantic):** Cài đặt môi trường (`venv` hoặc `uv`). Học cách khai báo kiểu dữ liệu khắt khe trong Python. Dùng Pydantic ép kiểu. *Lab:* Viết các data class quản lý người dùng không cho phép dữ liệu rác.
- **Ngày 2 (OOP - Hướng đối tượng):** Nắm vững Kế thừa, Đa hình, Đóng gói. *Lab:* Code một hệ thống Thư viện Sách (chỉ dùng OOP, không dùng database).
- **Ngày 3 (Xử lý Ngoại lệ - Exceptions):** Đừng bao giờ dùng `try/except Exception`. *Lab:* Tạo ra các class Lỗi riêng biệt (Custom Exceptions) và xử lý lỗi thanh lịch.
- **Ngày 4 (Decorators & Testing):** *Lab:* Viết Decorator đo thời gian chạy của hàm, hoặc tự retry khi hàm lỗi. Bắt đầu viết Unit Test bằng thư viện `pytest`.
- **Ngày 5 (Git & Code Quality):** Cài đặt `Ruff` hoặc `Flake8`. Học luồng commit code. *Lab:* Chạy test trên toàn bộ bài của Ngày 1-4, đảm bảo code sạch.
- **Ngày 6 (Project Tuần):** Tạo "Hệ thống Quản lý Thư viện Console" có Unit test bao phủ 80% code, gán kiểu dữ liệu 100%.

### Tuần 2: Database & Tư duy Dữ liệu (SQL)
- **Ngày 1 (SQL Cơ bản):** SELECT, JOIN, GROUP BY, HAVING. *Lab:* Cày 20 bài Easy/Medium trên HackerRank (mục SQL).
- **Ngày 2 (SQL Nâng cao):** CTE (WITH), Window Functions, Indexing. *Lab:* Cày tiếp 10 bài Medium/Hard HackerRank. Hiểu tại sao có Index thì query lại nhanh.
- **Ngày 3 (PostgreSQL & ACID):** Cài Postgres (có thể qua Docker). Tìm hiểu Transaction (Commit/Rollback). *Lab:* Thực hiện thao tác chuyển tiền ngân hàng đảm bảo tính toàn vẹn dữ liệu.
- **Ngày 4 (Tương tác DB qua ORM):** Dùng `SQLAlchemy` hoặc `SQLModel`. *Lab:* Ánh xạ bảng Postgres thành class Python. Thực hiện CRUD (Thêm/Sửa/Xóa).
- **Ngày 5 (Database Migration):** Dùng `Alembic` để theo dõi sự thay đổi cấu trúc bảng (Schema versioning). 
- **Ngày 6 (Project Tuần):** Thiết kế Database Schema cho app Quản lý nhân sự. Viết các truy vấn xuất báo cáo lương phức tạp.

### Tuần 3: Xây dựng API và Bất đồng bộ
- **Ngày 1 (HTTP Protocols & FastAPI):** RESTful API là gì, mã trạng thái HTTP (200, 400, 401, 500). *Lab:* Dựng API CRUD người dùng cơ bản bằng FastAPI.
- **Ngày 2 (Bất đồng bộ - Async/Await):** *Lab:* Viết script gửi 100 request giả lập. So sánh tốc độ giữa viết kiểu Sync (chờ tuần tự) và Async (chạy đồng thời).
- **Ngày 3 (Middleware & Rate Limiting):** *Lab:* Viết cơ chế giới hạn 1 user chỉ được gọi API 5 lần/phút để tránh bị spam.
- **Ngày 4 (Dependency Injection):** Cách tiêm Database Session vào FastAPI Route. *Lab:* Cấu trúc lại file code cho sạch sẽ, dễ viết test.
- **Ngày 5 (Pagination & Streaming):** Phân trang dữ liệu. Trả dữ liệu dạng dòng chảy (SSE - Server-Sent Events) - nền tảng cho việc chữ AI hiện ra từ từ sau này.
- **Ngày 6 (Project Tuần):** Backend API hoàn chỉnh cho app Quản lý nhân sự ở Tuần 2 (kết hợp FastAPI + Postgres + Async).

### Tuần 4: Chạy Ngầm (Background Jobs) & Đóng gói (Docker)
- **Ngày 1 (Message Queue & Redis):** Kiến trúc Queue - Worker. Cài đặt Redis.
- **Ngày 2 (Background Tasks):** Dùng Celery hoặc ARQ. *Lab:* Viết API bấm gửi báo cáo -> Đẩy task vào Queue -> Báo cho user "Đang xử lý" -> Worker chạy ngầm 10s rồi xuất file.
- **Ngày 3 (Retry & Observability):** Dead-letter queue (Lỗi quá nhiều thì bỏ đi đâu). *Lab:* Ghi Log JSON chuẩn mực, gắn Track-ID cho mỗi request.
- **Ngày 4 & 5 (Docker & Docker Compose):** *Lab:* Viết Dockerfile cho FastAPI. Viết `docker-compose.yml` để nhấc bổng cả API, Redis, Postgres lên chỉ bằng 1 câu lệnh `docker-compose up`.
- **Ngày 6 (Gate P1 - Đạt chuẩn Backend):** Tích hợp tất cả từ Tuần 1 đến 4. Phải có file `README.md` chỉ dẫn cách chạy qua Docker.

---

## Phase 2: Lõi Ứng Dụng LLM (Tuần 5 - Tuần 7)
*Nắm vững giao tiếp với các Model ngôn ngữ lớn.*

### Tuần 5: LLM Foundations & Giao tiếp API
- **Ngày 1 (Tokenization & Params):** Tìm hiểu Temperature, Top_p. *Lab:* Dùng thư viện `tiktoken` đếm số token của một đoạn văn tiếng Việt vs Tiếng Anh. Tính ra chi phí thật.
- **Ngày 2 (Provider Abstraction):** *Lab:* Viết 1 class trừu tượng để gọi OpenAI, Anthropic, Gemini mà không phải viết lại logic API, chỉ cần đổi tên Model trong cấu hình.
- **Ngày 3 (Structured Output):** AI thường ba hoa. *Lab:* Ép AI chỉ trả về một object JSON đúng chuẩn Pydantic (Ví dụ: trích xuất Tên, Tuổi, Ngày sinh từ 1 đoạn văn thô).
- **Ngày 4 (Tool Calling):** *Lab:* Cung cấp hàm lấy thời tiết cho AI, bắt AI tự hiểu khi nào nên gọi hàm, khi nào tự trả lời.
- **Ngày 5 (Lỗi và Fallback):** *Lab:* Giả lập mạng chậm (Timeout). Bắt hệ thống tự retry 2 lần, nếu vẫn lỗi thì tự động switch sang một Model rẻ hơn làm phương án dự phòng.
- **Ngày 6 (Project Tuần):** Dịch vụ Trích xuất Thông tin thông minh (có retry, validate chuẩn JSON, đóng gói).

### Tuần 6: Kỹ thuật Prompt & Tối ưu Context
- **Ngày 1 (System Prompt & Roles):** Cấu trúc chuẩn: Vai trò, Nhiệm vụ, Ràng buộc. *Lab:* Tối ưu 3 phiên bản prompt cho cùng 1 tác vụ.
- **Ngày 2 (Few-shot & Chain-of-Thought):** *Lab:* Cung cấp ví dụ để AI học theo; ép AI phải suy luận "Step-by-step" trước khi đưa ra kết luận.
- **Ngày 3 (Context Budgeting):** *Lab:* Viết thuật toán quản lý lịch sử hội thoại: Giới hạn 4000 token, nếu dài hơn thì xóa tin nhắn cũ hoặc tự tóm tắt lại lịch sử cũ.
- **Ngày 4 (Versioning & Tracing):** Coi prompt là code. *Lab:* Lưu prompt ra file riêng có phiên bản.
- **Ngày 5 (Prompt Injection - Bảo mật):** *Lab:* Thử dùng câu lệnh bẻ khóa (đóng vai hacker) để lừa chatbot của bạn văng tục hoặc lộ dữ liệu nhạy cảm. Thêm filter phòng thủ.
- **Ngày 6 (Project Tuần):** Bot hội thoại có trí nhớ dài hạn (cắt context thông minh) và bảo mật tốt.

### Tuần 7: Tối ưu Kiến trúc AI Service
- **Ngày 1 (Streaming & UI):** *Lab:* Dùng SSE ở Tuần 3, trả chữ từ AI về một giao diện Web đơn giản (có thể dùng file HTML tĩnh).
- **Ngày 2 (Semantic Caching):** Hỏi 2 câu ý nghĩa giống nhau không nên tốn tiền gọi AI 2 lần. *Lab:* Tích hợp Cache vào hệ thống.
- **Ngày 3 - 6 (Project Gate P2 - AI Chat Service):** Hoàn thiện dịch vụ Chat hỗ trợ Streaming, lưu trữ Postgres, quản trị Cost (Tiền) cho mỗi lượt chat, đóng gói chạy Docker.

---

## Phase 3: Kỹ Sư RAG & Tri thức (Tuần 8 - Tuần 11)
*Đưa dữ liệu công ty vào AI.*

### Tuần 8: Ingestion & Tìm kiếm Vector
- **Ngày 1 (Parsing):** *Lab:* Đọc PDF, Word, HTML bóc chữ.
- **Ngày 2 (Chunking):** Đây là khâu quyết định RAG khôn hay ngu. *Lab:* Test cắt theo ngữ nghĩa (thấy dấu chấm thì cắt, hoặc gom theo header).
- **Ngày 3 (Embeddings):** Biến chữ thành vector số. *Lab:* Chạy embedding và lưu vào `pgvector` (trong Postgres).
- **Ngày 4 (Vector Search):** *Lab:* Dùng Cosine Similarity tìm top 5 đoạn văn bản gần nghĩa nhất với câu hỏi.
- **Ngày 5 - 6 (Project Tuần):** Hệ thống "Naive RAG" (RAG Ngây thơ) - Code chay từ A-Z, từ lúc đọc file tới lúc AI trả lời dựa trên file.

### Tuần 9: RAG Nâng cao & Phân quyền
- **Ngày 1 (Hybrid Search):** Vector đôi lúc tìm mã số lỗi. *Lab:* Kết hợp BM25 (tìm theo từ khóa) + Vector Search.
- **Ngày 2 (Reranking):** Lấy 20 kết quả lên, nhờ AI nhỏ chấm điểm lại để chọn ra 5 kết quả tinh túy nhất.
- **Ngày 3 (Citations & Metadata):** *Lab:* Bắt AI phải chèn link/dòng trích dẫn để chứng minh nó không bịa chuyện.
- **Ngày 4 (Phân quyền ACL):** *Lab:* Chặn ở tầng truy vấn: Giám đốc mới search ra file lương, nhân viên search thì hệ thống báo không tìm thấy.
- **Ngày 5 - 6 (Project Tuần):** Hệ thống RAG có phân quyền, có trích dẫn.

### Tuần 10: Xây dựng Bộ Đánh giá (Evals - Bắt buộc)
*Sự khác biệt giữa thợ gõ code và Kỹ sư (Engineer).*
- **Ngày 1 (Golden Dataset):** Tạo thủ công 50-100 câu hỏi chất lượng + đáp án chuẩn làm thước đo.
- **Ngày 2 (Retrieval Metrics):** Học các chỉ số Recall@k, MRR. *Lab:* Code tự động đo xem thuật toán tìm kiếm lấy đúng tài liệu được bao nhiêu %.
- **Ngày 3 (LLM-as-judge):** Dùng AI thông minh nhất (GPT-4/Claude Opus) để chấm điểm AI của bạn.
- **Ngày 4 (AI Observability):** *Lab:* Tích hợp Langfuse (hoặc tương tự) để nhìn thấu toàn bộ luồng suy nghĩ, chi phí, tốc độ của hệ thống.
- **Ngày 5 - 6:** Tinh chỉnh RAG của Tuần 9 sao cho điểm đánh giá (Recall) đạt > 85%.

### Tuần 11: Dự án giữa khóa (KMS System)
- **Ngày 1 - 6:** Hoàn thiện Knowledge Management System kết hợp các Tuần 8, 9, 10. (Có Job chạy ngầm băm tài liệu, lưu Vector DB, tìm kiếm lai, báo cáo chất lượng tự động).

---

## Phase 4: Tác Tử (Agents) & Đưa ra Sản phẩm (Tuần 12 - Tuần 16)

### Tuần 12: Tool & Luồng Agent
- **Ngày 1 (Agent Loop):** Code chay vòng lặp: Nghĩ -> Hành động (gọi tool) -> Đọc kết quả -> Kết luận. Không dùng framework.
- **Ngày 2 (LangGraph):** Bắt đầu dùng Framework tốt nhất hiện tại. *Lab:* Vẽ quy trình xử lý công việc bằng Nodes và Edges.
- **Ngày 3 (Memory & HITL):** Bắt Agent dừng lại xin phép con người duyệt mới được đi tiếp (Ví dụ: tool xóa database).
- **Ngày 4-6 (Project Tuần):** Agent tự động đọc Log hệ thống, tìm lỗi và đề xuất file code cần sửa.

### Tuần 13: Giao thức MCP
- **Ngày 1-2:** Hiểu chuẩn MCP (Model Context Protocol). *Lab:* Tự viết 1 Server MCP (ví dụ kết nối với Hệ thống quản lý thẻ Trello/Jira).
- **Ngày 3-4:** Biến Agent thành Client, tự do gọi Tool từ MCP Server vừa viết.
- **Ngày 5-6:** Tích hợp KMS (Tuần 11) thành 1 Tool trên MCP Server để Agent truy vấn kiến thức công ty.

### Tuần 14: Triển khai (Deploy) & Bảo vệ
- **Ngày 1 (Container Registry & Cloud):** Đẩy Docker Image lên mạng (AWS ECR hoặc Docker Hub). Deploy lên Cloud (VPS, Vercel, hoặc Cloud Run).
- **Ngày 2 (Bảo vệ Token & Cost):** Alert khi chi phí tiêu thụ quá mức. Giới hạn ngắt mạch (Circuit breaker) nếu tiền tăng vọt.
- **Ngày 3 (Load Test):** Dùng công cụ test đập thử 1000 requests vào API của bạn xem hệ thống sập ở đâu.
- **Ngày 4-6 (CI/CD):** Viết Github Action: Cứ push code lên là tự động chạy Test, tự động chạy Đánh giá RAG (Eval), pass hết mới được merge.

### Tuần 15 - 16: Đồ án Tốt nghiệp (Capstone)
- Chọn làm dự án **Enterprise Data & Knowledge Copilot**
- Cần có: 
  1. Frontend Giao diện mượt mà (Có thể dùng template).
  2. Backend vững chắc, API tài liệu đầy đủ.
  3. Hệ thống RAG thông minh (Phân quyền, Citation).
  4. Agent tự hành (MCP Tools, duyệt lệnh bởi con người).
  5. Bảng theo dõi giám sát chất lượng và chi phí (Langfuse).
- 3 ngày cuối: Viết README thật đẹp để làm Portfolio xin việc. Quay Video Demo (Giọng nói + Phụ đề). Đẩy code lên Github ở chế độ Public.
