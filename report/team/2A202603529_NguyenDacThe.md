# Báo cáo cá nhân — Nguyễn Đắc Thể

## 1. Thông tin thành viên

- **Họ tên:** Nguyễn Đắc Thể
- **MSSV:** 2A202603529
- **Email:** dacthebn@gmail.com
- **GitHub:** NguyenDacThe
- **Vai trò:** Người 2, kiểm số CP1–CP2, phụ trách pilot CP4 và tiếp quản code sau bàn giao.

## 2. Phần việc phụ trách

- Kiểm tra kết quả A1–A4 và B1–B4, ghi phép đối chiếu và điền bảng chi phí.
- Tính cỡ mẫu D1, đề xuất thiết kế D2, ngưỡng dừng và phương án quay về luồng thủ công.
- Đối chiếu bảng A/B với bản code nhóm sau bàn giao và ghép phần in D1 vào lệnh chạy chung.

## 3. Đóng góp cụ thể

- Bảng A/B được tính lại từ hai CSV. Ví dụ, lấy chi phí **4.373.585 đ** chia **978** việc thành công cho **4.472 đ/việc** (simulated). Tử số cộng phí của toàn bộ lượt chạy, kể cả lượt lỗi.
- Theo B3, giới hạn **2 lần** có chi phí toàn hệ thống thấp nhất là **6.901.220 đ** (simulated). Chi phí **4.111 đ/việc** với giới hạn **1 lần** (simulated) không phản ánh phần chi phí xử lý thêm **85** yêu cầu chuyển nhân viên.
- CP4 đề xuất chia ngẫu nhiên **20 nhân viên mỗi nhóm**, cần ít nhất **299 yêu cầu mỗi người** để đạt khoảng **859 yêu cầu hiệu dụng mỗi nhóm** ở MDE **6 điểm phần trăm**. Nếu tác động thật chỉ **5 điểm**, power xấp xỉ **0,64**.

## 4. Bằng chứng

- [Bảng chi phí A/B](bang_chi_phi.md) có công thức, nguồn và kết quả đã tính độc lập.
- [Code tính cỡ mẫu CP4](../../src/lab13_cp4.py) in D1 và tỉ lệ mở lại **51/1.200 = 4,25%** toàn mẫu, **39/982 = 3,97%** trong phạm vi.
- [Kế hoạch pilot](pilot_plan.yaml) có đối chứng đồng thời, cỡ mẫu, ngưỡng dừng và rollback. Ngày và ngưỡng trong file là đề xuất để nhóm duyệt.

Sau khi gộp nhánh, `python lab13.py` đã in A, B và D1 từ cùng bộ dữ liệu. Lệnh `python lab13.py --cp4` kiểm tra riêng cỡ mẫu và tỉ lệ mở lại.

## 5. Công cụ AI đã dùng

Dùng ChatGPT (Codex) hỗ trợ đọc đề, viết mã tính CP4, tính lại A/B bằng Python trên dữ liệu gốc và soạn bản nháp các báo cáo. Các phép tính tiêu biểu được ghi trong bảng chi phí. Codex đã chạy và đối chiếu A/B và D1 trên bản code đã gộp. Thành viên cần tự xác nhận kết quả trước khi nộp.

## 6. Tự đánh giá

Điểm làm tốt của tôi là trình bày phép tính và nguồn số liệu để nhóm có thể kiểm lại bảng A/B từ hai CSV. Kết quả B3 cho thấy giới hạn 1 lượt có chi phí thấp nhất trên mỗi việc trợ lý làm xong, còn giới hạn 2 lượt rẻ nhất cho cả hệ thống khi tính cả phần nhân viên làm thay (simulated). Đây là hai thước đo tôi cần phân biệt khi giải thích đề xuất với hội đồng.

Điểm tôi cần cải thiện là trình bày rõ hơn ảnh hưởng của việc chia nhóm theo nhân viên. Cỡ mẫu hiệu dụng có thể giảm khi lượng yêu cầu giữa các nhân viên chênh lệch, và thiết kế để phát hiện mức chênh 6 điểm phần trăm có power khoảng 0,64 nếu tác động thật là 5 điểm. Khi pilot có dữ liệu, tôi sẽ đối chiếu lại cỡ mẫu theo từng nhân viên và dùng phút xem lại, làm lại đo thực tế để kiểm tra ngưỡng chi phí.
