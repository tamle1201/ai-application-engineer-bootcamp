print("--- MÔ PHỎNG QUÁ TRÌNH RAG (RETRIEVAL-AUGMENTED GENERATION) ---")

# 1. Chunking: Cắt tài liệu lớn thành các đoạn nhỏ
# (Giả sử ta đã đọc 1 cuốn sổ tay nhân sự và cắt nó ra)
document_chunks = [
    "Quy định công ty: Nhân viên phải đi làm lúc 8h sáng.",
    "Công ty có trụ sở chính tại tòa nhà Keangnam, Hà Nội.",
    "Tiền lương được thanh toán vào mùng 5 hàng tháng qua thẻ Vietcombank."
]
print("📚 Bước 1 & 2: Tài liệu nội bộ đã được cắt thành 3 phần (Chunks).")
print("📚 Bước 3 & 4: (Giả lập) Đã nhúng (Embedding) và lưu vào Vector Database.\n")


# 2. Người dùng đặt câu hỏi
user_query = "Mùng mấy thì công ty phát lương vậy bạn?"
print(f"👤 Câu hỏi của User: {user_query}")


# 3. Retrieval (Truy xuất)
# Trong thực tế, AI sẽ dùng Toán học (Cosine Similarity) để so sánh vector của câu hỏi
# với vector của 3 chunk kia để tìm ra đoạn liên quan nhất.
# Ở đoạn code giả lập này, hệ thống sẽ trả về đoạn số 3 (Index = 2):
retrieved_chunk = document_chunks[2]
print(f"\n🔍 Bước 5 - Retrieval: Hệ thống VectorDB tìm thấy đoạn liên quan nhất:")
print(f"   => '{retrieved_chunk}'")


# 4. Augmentation & Generation: Trộn câu hỏi và tài liệu gửi cho AI
final_prompt = f"""
Bạn là một AI hỗ trợ nhân sự. Chỉ sử dụng thông tin trong phần 'Tài liệu' dưới đây để trả lời câu hỏi. Không được bịaa chuyện.

[Tài liệu]: 
{retrieved_chunk}

[Câu hỏi]: 
{user_query}
"""

print("\n🚀 PROMPT CHUẨN BỊ GỬI CHO OPENAI (ĐÃ ĐƯỢC BƠM THÔNG TIN RAG):")
print("-" * 50)
print(final_prompt)
print("-" * 50)

print("🤖 Kết quả AI trả lời (Dự kiến): Công ty sẽ thanh toán tiền lương vào mùng 5 hàng tháng qua thẻ Vietcombank.")
