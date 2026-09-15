# T05 — Algorithms & Data Structures

Mục tiêu: chọn cấu trúc dữ liệu, phân tích time/space complexity và dùng thuật toán phù hợp với AI Application Engineer; không thi competitive programming thuần túy.

## Part 1 — Complexity and data-structure selection

Mode: `CLOSED_BOOK`  
Thời gian: 40 phút

### T05-P1-Q0 — MCQ calibration

Average-case lookup theo key trong hash map thường là:

A. O(1)  
B. O(log n)  
C. O(n log n)  
D. O(2^n)

Chọn và nêu assumption.

### T05-P1-Q1 — Big-O reading

Phân tích time và extra-space complexity:

```python
def has_duplicate(values):
    seen = set()
    for value in values:
        if value in seen:
            return True
        seen.add(value)
    return False
```

Nêu average/worst-case assumptions cần thiết.

### T05-P1-Q2 — Nested loops

```python
for i in range(n):
    j = 1
    while j < n:
        j *= 2
```

Time complexity là gì? Giải thích thay vì chỉ ghi ký hiệu.

### T05-P1-Q3 — Structure choice

Chọn array/list, stack, queue, hashmap, hashset hoặc heap cho:

1. phát hiện request ID trùng;
2. lấy job ưu tiên cao nhất;
3. undo thao tác gần nhất;
4. BFS qua dependency graph;
5. ánh xạ document ID → metadata.

Nêu operation quan trọng và complexity kỳ vọng.

### T05-P1-Q4 — Space trade-off

Để dedupe 100 triệu IDs, `set` nhanh nhưng tốn memory. Đưa ít nhất ba phương án khi memory không đủ và trade-off về correctness/speed.

### T05-P1-Q5 — Recursion

Recursive traversal có thể gặp vấn đề gì với cây/dependency sâu? Khi nào chuyển sang explicit stack?

## Part 2 — Core algorithms

Mode: `DOCS_ALLOWED`  
Thời gian: 55 phút

### T05-P2-Q1 — Binary search

Implement binary search trả index đầu tiên của target trong sorted list có duplicate. Phân tích time/space và test empty/not-found/boundaries.

### T05-P2-Q2 — Two pointers

Cho sorted array và target, trả cặp index có tổng bằng target hoặc `None`. Không dùng nested loop. Giải thích invariant.

### T05-P2-Q3 — Sliding window

Tìm độ dài nhỏ nhất của subarray liên tiếp có tổng ≥ target, giả định số dương. Sau đó giải thích vì sao cách này có thể sai nếu có số âm.

### T05-P2-Q4 — Sorting

Bạn cần sort 10 triệu records theo timestamp nhưng memory hạn chế. So sánh in-memory sort và external sort; nêu stability và I/O concerns.

## Part 3 — Trees, heaps and graphs

Mode: `DOCS_ALLOWED`  
Thời gian: 55 phút

### T05-P3-Q1 — Top-k

Tìm top-k chunks có score cao nhất khi stream rất lớn. So sánh sort toàn bộ với min-heap size k.

### T05-P3-Q2 — BFS/DFS

Một tool dependency graph có cycle. Thiết kế cycle detection và traversal; chọn BFS/DFS và giải thích.

### T05-P3-Q3 — Tree traversal

Parse document headings thành tree. Viết traversal tạo path `Section/Subsection/...` cho mỗi leaf; phân tích stack/recursion risk.

### T05-P3-Q4 — Graph shortest path

Workflow có edge cost là latency. Khi nào BFS đủ, khi nào cần Dijkstra, và negative edge có ý nghĩa gì trong bối cảnh này?

## Part 4 — Applied/adaptive challenge

Mode: `DOCS_ALLOWED`  
Thời gian: 50 phút  
Người chấm chọn 2/4 câu.

### T05-P4-Q1 — Complexity regression

Một retrieval post-processor chạy tốt với 1.000 chunks nhưng chậm với 100.000. Code so sánh mọi cặp chunks để dedupe similarity. Phân tích O(n²), đề xuất cải tiến và rủi ro false positive/negative.

### T05-P4-Q2 — LRU cache

Mô tả hoặc implement LRU cache O(1) cho get/put. Nêu concurrency, memory limit và tenant-aware key.

### T05-P4-Q3 — Basic dynamic programming

Chọn các chunks có tổng độ dài ≤ context budget để tối đa tổng relevance score. Mô hình hóa như bài toán nào? Đưa giải pháp exact cơ bản và heuristic thực tế; phân tích trade-off.

### T05-P4-Q4 — Streaming percentile

Không thể giữ mọi latency sample. Đề xuất cấu trúc/thuật toán ước lượng p95 và giải thích accuracy-memory trade-off.
