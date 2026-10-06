# AI Application Engineer Roadmap

Dự án này chứa lộ trình học tập và phát triển để trở thành một AI Application Engineer, bao gồm từ việc củng cố nền tảng lập trình, xây dựng web, đến tích hợp AI và triển khai hệ thống (DevOps/MLOps).

Lộ trình được chia thành **7 Phase (A đến G)**. Trong đó 4 Phase đầu (6 tuần) tập trung vào việc học kiến thức nền tảng, và 3 Phase sau dành cho việc làm dự án thực tế.

---

## 1. Bức Tranh Tổng Quan (7 Phases)

* **Phase A: Python Programming** (Thời gian học: 1 tuần)
  * Nắm vững kiến thức Advanced Python Concepts.
* **Phase B: Web Development with Python & FastAPI & ReactJS/NextJS** (Thời gian học: 2 tuần)
  * Nắm vững Internet Basic (OS, Network, HTTP), Database (SQL, No-SQL), Web API Framework (FastAPI, GraphQL, Restful API), Frontend (ReactJS Core, NextJS, Tailwind CSS) và sử dụng framework xây dựng web.
* **Phase C: Ứng dụng AI trong Phát triển phần mềm** (Thời gian học: 1 tuần)
  * Tìm hiểu Nền tảng AI (Instruction, Prompt, Context, Memory, Skill, Hook) và Software Development Lifecycle (CICD, Spec Driven Development, Agile Scrum).
* **Phase D: RAG System & AI Application Architecture** (Thời gian học: 2 tuần)
  * Đi sâu vào hệ thống RAG (Ingestion, Chunking, Embedding, Indexing, Retrieval), Kiến trúc ứng dụng AI và LLM Architecture.
* **Phase E: Nghiên cứu làm dự án**
  * Bước vào giai đoạn áp dụng kiến thức để lên ý tưởng, nghiên cứu khả thi dự án.
* **Phase F: Xây dựng sản phẩm**
  * Trực tiếp code, kết nối các phần Frontend, Backend, và RAG/AI Agent thành sản phẩm.
* **Phase G: Triển khai**
  * Tìm hiểu và ứng dụng DevOps cơ bản (Docker, Compose, CI/CD, Kubernetes, Observability) và Triển khai LLMOps/MLOps.

---

## 2. Cấu Trúc Thư Mục Chuẩn (Mô hình Program - Course)

Dự án này được thiết kế theo cấu trúc sau để đảm bảo lưu trữ kiến thức có hệ thống:

```text
ai-application-engineer-roadmap/
├── Kien_thuc/                         # Nơi chứa kiến thức theo từng Phase (Phase A, B, C, D)
│   ├── Phase_A...                     # Bên trong mỗi Phase là các Program học tập
│   │   ├── course_1...                # Mỗi Program chia thành nhiều Course
│   │   │   ├── docs/                  # Tài liệu học tập, lý thuyết
│   │   │   └── VD/                    # Code ví dụ, thực hành theo các Learning Outcomes (CLO)
│   │   └── running_project/           # Project thực hành gắn liền với Phase đó
│   └── ...
├── learning-path/                     # Các tài liệu tổng hợp định hướng học tập
├── docs/                              # Lưu trữ các file tài liệu hướng dẫn
│   ├── roadmap/                       # Nơi lưu lộ trình chi tiết
│   └── tai_lieu_khi_trien_khai/       # Tài liệu tham khảo cho Phase G
├── README.md                          # Hướng dẫn tổng quan (File bạn đang đọc)
└── roadmap-tong-hop-khoa-luan-20-tuan.md  # File Roadmap chi tiết theo Phase
```

## 3. Cách Sử Dụng

1. Đọc file `roadmap-tong-hop-khoa-luan-20-tuan.md` để nắm rõ mục tiêu chi tiết của từng Course trong các Phase.
2. Với mỗi tuần học, đi vào thư mục `Kien_thuc/` tương ứng, đọc tài liệu trong `docs/`, chạy thử code trong `VD/`.
3. Khi hoàn thành lý thuyết một Phase, bắt tay vào làm `running_project/` của Phase đó.
4. Sau khi kết thúc 4 Phase đầu (6 tuần), bắt tay vào Phase E, F, G để làm và đưa dự án thực tế lên môi trường Production.
