# T09 — AI Fundamentals

Mục tiêu: mathematics, probability/statistics, ML, evaluation và neural-network foundations ở mức cần cho AI Application Engineer.

## Part 1 — Math and statistics

Mode: `CLOSED_BOOK`  
Thời gian: 45 phút

### T09-P1-Q0 — MCQ calibration

Trong bài toán bỏ sót positive gây hậu quả lớn, metric thường cần được ưu tiên quan sát là:

A. Recall  
B. File size  
C. Epoch count  
D. Mean feature value

Chọn và giải thích; không khẳng định chỉ một metric là đủ.

### T09-P1-Q1 — Vector/dot product

Cho `a = [1, 2]`, `b = [3, 4]`. Tính dot product và giải thích trực giác của giá trị này.

### T09-P1-Q2 — Cosine similarity

Hai vector cùng hướng nhưng độ lớn khác nhau có cosine similarity thế nào? Nêu khi cosine không đủ để quyết định relevance.

### T09-P1-Q3 — Mean/variance/outlier

Latency: `[100, 105, 110, 115, 2000]` ms. Mean có đại diện tốt không? Đề xuất median/percentile và giải thích variance/outlier.

### T09-P1-Q4 — Correlation

Token count tương quan cao với latency. Có thể kết luận token gây ra toàn bộ latency không? Nêu confounder và thí nghiệm.

### T09-P1-Q5 — Probability

Một classifier flag 100 cases, 20 thật sự positive. Tính precision. Nếu tổng positive thật trong dataset là 25 và classifier tìm đúng 20, tính recall.

### T09-P1-Q6 — Distribution shift

Training data chủ yếu tiếng Anh, production chủ yếu tiếng Việt. Nêu rủi ro, cách đo và mitigation.

## Part 2 — Machine learning

Mode: `CLOSED_BOOK`  
Thời gian: 50 phút

### T09-P2-Q1 — Task formulation

Phân loại supervised/unsupervised và classification/regression/clustering cho bốn bài toán: spam, dự đoán latency, nhóm feedback, phát hiện anomaly không nhãn.

### T09-P2-Q2 — Data split

Thiết kế train/validation/test split cho user events theo thời gian. Nêu data leakage nếu cùng user hoặc future data xuất hiện sai split.

### T09-P2-Q3 — Overfit/underfit

Model train accuracy 99%, validation 72%. Đưa hypothesis và hành động. Trường hợp cả hai 60% thì sao?

### T09-P2-Q4 — Feature engineering

Cho bài toán dự đoán ticket escalation. Đề xuất feature, kiểm tra leakage, missing values và fairness risk.

### T09-P2-Q5 — Regularization

Giải thích mục đích regularization bằng trực giác; nêu trade-off khi quá mạnh.

## Part 3 — Evaluation and decision

Mode: `DOCS_ALLOWED`  
Thời gian: 55 phút

### T09-P3-Q1 — Confusion matrix

Từ `TP=40, FP=10, FN=20, TN=930`, tính accuracy, precision, recall, F1 và giải thích metric nào bị class imbalance che giấu.

### T09-P3-Q2 — Business trade-off

Model A accuracy cao hơn nhưng recall thấp hơn B. Chọn model cho phát hiện giao dịch gian lận và cho lọc email quảng cáo; phải nêu cost của FP/FN.

### T09-P3-Q3 — Threshold

Giải thích thay đổi threshold ảnh hưởng precision/recall. Thiết kế cách chọn threshold theo business cost và review capacity.

### T09-P3-Q4 — ROC-AUC limits

ROC-AUC cao có đủ để launch không? Nêu calibration, slice, base rate, latency và operational constraints còn cần.

### T09-P3-Q5 — Experiment validity

Hai model được test trên hai dataset khác nhau. Có thể so score trực tiếp không? Thiết kế comparison công bằng.

## Part 4 — Neural networks and applied judgment

Mode: `DOCS_ALLOWED`  
Thời gian: 70 phút

### T09-P4-Q1 — Forward/loss/backprop

Giải thích bằng lời luồng input → neuron/layer → activation → prediction → loss → gradient → optimizer update.

### T09-P4-Q2 — Learning rate

Loss dao động mạnh hoặc giảm cực chậm. Nêu vai trò learning rate và evidence cần trước khi chỉnh.

### T09-P4-Q3 — Batch/epoch

Phân biệt batch, iteration và epoch; trade-off batch size về memory, noise và throughput.

### T09-P4-Q4 — Fine-tuning decision

Một team muốn fine-tune ngay khi prompt chưa ổn và chưa có eval set. Phân tích quyết định; nêu điều kiện khi fine-tuning có ROI.

### T09-P4-Q5 — Applied AI boundary

Cho ba vấn đề: knowledge mới, format output không ổn định, domain style đặc thù. So sánh retrieval, structured validation, prompting và fine-tuning; không chọn một kỹ thuật cho tất cả.

### T09-P4-Q6 — Metric implementation

Viết function hoặc pseudocode nhận `tp`, `fp`, `fn`, `tn`, trả accuracy/precision/recall/F1 và xử lý denominator bằng 0. Viết tối thiểu ba tests.
