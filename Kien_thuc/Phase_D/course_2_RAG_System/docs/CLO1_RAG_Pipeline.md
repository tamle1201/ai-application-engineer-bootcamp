# CLO 1: Hệ thống RAG (Retrieval-Augmented Generation)

## Mục tiêu học tập
Nắm vững 5 bước cốt lõi để biến một con AI công cộng (ChatGPT) thành một "Chuyên gia đọc tài liệu nội bộ của công ty".

## Tại sao cần RAG?
ChatGPT được huấn luyện trên dữ liệu Internet, nó KHÔNG BIẾT báo cáo tài chính nội bộ công ty bạn. Nếu bạn cố tình hỏi, nó sẽ "ảo giác" và bịa chuyện (Hallucination). 
**Giải pháp (RAG):** Rút trích (Retrieve) đoạn tài liệu nội bộ có liên quan nhất, nhét nó vào (Augment) trong Prompt, rồi mới bảo AI sinh ra (Generation) câu trả lời dựa trên đoạn tài liệu đó.

## 5 Bước của RAG Pipeline:
1. **Ingestion (Nuốt dữ liệu):** Đọc các loại file PDF, Word, Excel, Website...
2. **Chunking (Băm nhỏ):** Cắt file PDF dài 1000 trang thành từng đoạn văn nhỏ (khoảng 500 - 1000 chữ/đoạn). 
   - *Tại sao?* Vì AI bị giới hạn số lượng chữ đọc vào mỗi lần (Context window), và nhét cả 1000 trang vào sẽ tốn cực kỳ nhiều tiền API.
3. **Embedding (Nhúng):** Dùng toán học (Embedding Model) biến mỗi đoạn văn (Chunk) thành một dãy số dài (Vector). Các đoạn văn có ý nghĩa tương đồng nhau thì dãy số của chúng sẽ nằm gần nhau trong không gian toán học.
4. **Indexing (Lưu trữ):** Đẩy tất cả các Vector này vào Vector Database chuyên dụng.
5. **Retrieval (Truy xuất):** Khi người dùng đặt câu hỏi, ta cũng biến câu hỏi thành Vector -> Tìm các đoạn văn có Vector gần giống với câu hỏi nhất trong Database -> Bốc các đoạn văn đó ra, ghép vào Prompt cho LLM đọc và trả lời.

> 👉 **Hành động:** Chạy file `VD/01_rag_pseudo_code.py` để xem toàn bộ quá trình RAG này được mô phỏng bằng code Python như thế nào!
