# Báo cáo cá nhân — Trương Văn Thông-2A202603560

## 1. Thông tin thành viên

- Họ tên: Trương Văn Thông
- MSSV: 2A202603560
- Email: thongthong2k41306@gmail.com
- GitHub: thongthong2k41306-beep
- Vai trong nhóm: viết code và kiểm số cho nhiệm vụ A.

## 2. Phần việc phụ trách

CP1, nhiệm vụ A. Kiểm tra công thức chạy lại, tính chi phí từ trace và so sánh theo loại yêu cầu, rồi cộng chi phí cố định trong phạm vi pilot.

## 3. Đóng góp cụ thể

- A1 và A2: ba phép thử đạt **1,20 · 1,25 · 1,25**. Mô hình tính **4.472 đ/việc thành công** (`simulated`) trên **978** yêu cầu thành công.
- A3: nhóm quốc tế thành công **27,3%**, với chi phí **22.515 đ/việc thành công** (`simulated`). Đây là loại cần loại khỏi phạm vi pilot theo kết quả chi phí.
- A4: với hai loại nội địa và hàng nặng, chi phí sau khi cộng cố định là **4.599 đ** ở quy mô 45.000 yêu cầu/tháng và **5.784 đ** ở quy mô 22.500 yêu cầu/tháng (`simulated`).

## 4. Bằng chứng

- [Code và phép thử A1](../../src/lab13.py)
- [Bảng và kết luận A1–A4](bang_chi_phi.md)

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc yêu cầu, triển khai code Python và soạn bảng từ kết quả chạy trên hai file CSV của lab. Codex đã chạy `python lab13.py` trong thư mục `src/`.

Tôi đã chạy lại `python lab13.py` trong thư mục `src/`. Chương trình báo cả ba phép thử A1 đều đạt (**1,20 · 1,25 · 1,25**). Kết quả chạy khớp với bảng chi phí A1–A4, gồm **978** việc thành công và **4.472 đ/việc thành công** (`simulated`) ở A2.

## 6. Tự đánh giá

Cần tự giải thích được vì sao chi phí tính cả lượt thất bại, còn số việc ở mẫu số chỉ đếm yêu cầu thành công. Có thể kiểm tra tay phép thử A1 với `p = 0,8` và tối đa hai lượt: lượt đầu luôn diễn ra, lượt thứ hai xảy ra với xác suất `0,2`, nên kỳ vọng là `1 + 0,2 = 1,20` lượt.
