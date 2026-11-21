# Báo cáo nhóm

## 1. Thông tin nhóm

- Nhóm NhomTTBH, lớp L3A.
- Trương Văn Thông, Nguyễn Đắc Thể, Phan Gia Bảo và Nguyễn Quốc Hưng. Phân công và bằng chứng nằm trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí và mức độ an toàn của trợ lý hoàn phí LogiX-VN, rồi thiết kế pilot để đo tác động so với luồng thủ công. Dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lượt chạy. Nhóm tính chi phí từ mọi lượt chạy, đối chiếu các kịch bản vận hành và thiết kế đối chứng đồng thời.

## 3. Giải pháp

- **A và B:** Cộng token, tool và thời gian nhân viên cho toàn bộ lượt chạy liên quan. Tính chi phí trên mỗi việc thành công, sau đó kiểm tra độ nhạy, giới hạn lượt chạy và kịch bản xem lại 100%. [Bảng chi phí](bang_chi_phi.md)
- **C:** Đã đối chiếu 20 nhãn gốc của Bảo với bản đề xuất có AI hỗ trợ. Có 18/20 ca trùng (90%), hai ca khác nhãn có giải thích và bảng khắc phục đủ 5 loại. Đồng thuận CP3 chờ phiếu độc lập thứ hai. [Bảng lỗi](bang_loi.md)
- **D:** Đề xuất phân ngẫu nhiên 20 nhân viên mỗi nhóm, đối chứng cùng thời gian, bốn luật dừng và phương án quay về luồng thủ công. [Kế hoạch pilot](pilot_plan.yaml)
- **E:** Tính thử ba chỉ số, xác định event cần ghi và tổng hợp rủi ro kinh tế theo kết quả A/B. [Chỉ số và rủi ro](chi_so.md)

## 4. Kết quả

- Toàn mẫu có 978 việc thành công, chi phí **4.472 đ/việc** (simulated). Giới hạn 2 lượt có tổng chi phí hệ thống thấp nhất là **6.901.220 đ** trên 1.200 yêu cầu (simulated).
- Trong đợt chạy thử, **82,83%** yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày. Tỉ lệ sửa hoặc bỏ gợi ý là **27,12%**, tỉ lệ mở lại là **4,25%**. Đây là số mô tả đợt chạy thử.
- Đề xuất **Go có điều kiện** cho `noi_dia` và `hang_nang`. Điều kiện gồm đối soát hoàn tiền, ghi event, đo phút làm lại và duyệt thiết kế cỡ mẫu. [Hồ sơ launch v0](ho_so_launch_v0.md)
- Kết quả hội đồng chấm nhóm và phần hỏi đáp chưa được ghi nhận trong repo. [Phiếu nhóm dùng để chấm nhóm khác](phieu_cham.md)

## 5. Khó khăn và cách xử lý

Các nhánh cùng sửa bảng chi phí, thông tin thành viên và bảng lỗi. Bản tổng hợp giữ đóng góp của từng người, khôi phục liên kết báo cáo đã đổi tên và kiểm lại A/B, D1, E1 bằng `python lab13.py` trên hai CSV gốc. Phiếu nhãn đề xuất có AI hỗ trợ được giữ riêng trong phụ lục báo cáo cá nhân để nhóm xác nhận đúng quy trình.

## 6. Tổng hợp đóng góp

- Trương Văn Thông triển khai CP1. Nguyễn Đắc Thể đối chiếu chi phí và soạn thiết kế pilot. Phan Gia Bảo làm phiếu thứ nhất, bảng khắc phục dự thảo và phần E. Nguyễn Quốc Hưng bổ sung mã CP4, tiêu chí đủ mẫu và chuẩn bị phiếu riêng cho CP3. [Chi tiết đóng góp](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

Chi phí thời gian nhân viên là simulated. Khi xem lại 100%, chi phí biến đổi lên **11.743–12.415 đ/việc** (simulated), sát hoặc vượt mốc 12.000 đ. Pilot cần đo phút thực tế và kiểm tra giảm xem lại có an toàn. Thiết kế có power khoảng **0,64** nếu tác động thật chỉ 5 điểm phần trăm. Cần hoàn tất đồng thuận CP3, ghi nhận duyệt chéo và chạy lại trên máy của một thành viên khác trước khi nộp.

## 8. Tài liệu tham khảo

- [Đề bài Lab 13](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) và [hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
