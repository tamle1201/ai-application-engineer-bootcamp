# T04 — OOP & Software Engineering

Mục tiêu: OOP, SOLID, design patterns, UML, SDLC, requirements, architecture, Git, CI/CD, documentation và technical debt.

## Part 1 — OOP foundations

Mode: `CLOSED_BOOK`  
Thời gian: 35 phút

### T04-P1-Q0 — MCQ calibration

Muốn thay đổi model provider mà service chính không phụ thuộc SDK cụ thể, lựa chọn phù hợp nhất thường là:

A. Global variables.  
B. Interface/Protocol cùng dependency injection.  
C. Copy service cho từng provider.  
D. Một chuỗi `if` ở mọi function.

Chọn và giải thích trade-off.

### T04-P1-Q1 — Class design

Thiết kế class cho `Document`, `Chunk` và `Retriever`. Chỉ ra invariant, public behavior và dữ liệu không nên expose để mutate tùy ý.

### T04-P1-Q2 — Relationship

Phân biệt association, aggregation, composition và dependency bằng bốn quan hệ trong một AI document system. Không chỉ viết định nghĩa.

### T04-P1-Q3 — Inheritance vs composition

Bạn có `OpenAIClient`, `AnthropicClient`, `FakeClient`. Đề xuất interface và giải thích khi composition tốt hơn inheritance sâu.

### T04-P1-Q4 — Polymorphism

Viết pseudocode cho service dùng bất kỳ model client nào mà không dùng chuỗi `if provider == ...` rải rác.

### T04-P1-Q5 — Encapsulation

Model API key đang là public field và được log trong `__repr__`. Nêu rủi ro và thiết kế lại.

## Part 2 — SOLID and patterns

Mode: `CLOSED_BOOK`  
Thời gian: 50 phút

### T04-P2-Q1 — SRP/DIP review

Class `ChatService` đang parse PDF, chunk, embed, retrieve, prompt, call model, save DB và send email. Chỉ ra vấn đề và chia boundary; tránh tách thành quá nhiều class vô nghĩa.

### T04-P2-Q2 — LSP

Interface `ModelClient.generate()` hứa trả text hoặc raise `ModelError`. Một implementation trả `None`, implementation khác thoát process khi timeout. Phân tích substitutability.

### T04-P2-Q3 — Strategy/Factory/Adapter

Chọn pattern phù hợp cho:

1. đổi chunking algorithm runtime;
2. tạo provider client từ config;
3. bọc SDK bên thứ ba thành interface nội bộ.

Nêu khi pattern tạo overhead không cần thiết.

### T04-P2-Q4 — Repository and Singleton

Repository abstraction có lợi/hại gì? Singleton database client có vấn đề gì với test, lifecycle và concurrency? Đề xuất cách đơn giản hơn nếu app nhỏ.

## Part 3 — UML and delivery

Mode: `DOCS_ALLOWED`  
Thời gian: 65 phút

### T04-P3-Q1 — Diagrams

Với “user hỏi tài liệu, hệ thống retrieve rồi trả citation”, tạo:

- một use-case diagram hoặc mô tả tương đương;
- một class diagram;
- một sequence diagram cho happy path và model timeout;
- một state diagram cho ingestion job.

### T04-P3-Q2 — Requirements

Tách yêu cầu “chatbot nhanh, chính xác, an toàn” thành functional requirements, measurable non-functional requirements, assumptions và acceptance criteria.

### T04-P3-Q3 — SDLC

Lập kế hoạch từ discovery đến maintenance cho MVP 2 tuần. Bao gồm review, test, release, rollback, documentation và ownership.

## Part 4 — Git, CI/CD and engineering judgment

Mode: `WORK_SIMULATION`  
Thời gian: 70 phút

### T04-P4-Q1 — Git workflow

Thiết kế branch/PR/review strategy cho team 5 người. Xử lý migration, secret bị commit nhầm và hotfix production.

### T04-P4-Q2 — CI/CD

Thiết kế pipeline cho Python AI service: lint, type, unit, integration, eval smoke, security scan, build, deploy staging, approval/canary/rollback.

### T04-P4-Q3 — Technical debt

Deadline ngắn khiến team hard-code prompt, thiếu tests và log PII. Lập debt register, ưu tiên và rule chặn release. Phân biệt debt chấp nhận được với risk không được phép.

### T04-P4-Q4 — Architecture decision

Viết ADR ngắn cho quyết định “bắt đầu monolith modular hay microservices”. Nêu context, options, decision, consequences và trigger để xem lại.
