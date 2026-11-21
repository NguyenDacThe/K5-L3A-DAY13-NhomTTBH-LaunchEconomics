# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phan Gia Bảo. Cột nhãn người 1 giữ nguyên đủ 20 nhãn Bảo đã ghi.

Người gắn nhãn 2: chờ phiếu cá nhân được xác nhận. Phiếu đề xuất có hỗ trợ AI của Nguyễn Quốc Hưng được [lưu riêng](cp3_2A202603553_NguyenQuocHung.md). Hưng cần tự gắn nhãn theo quy tắc CP3 và xác nhận phiếu cá nhân trước khi nhóm nhập cột nhãn người 2, tính đồng thuận và chốt nhãn chung.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngầm | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Ngầm | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** chờ đủ hai phiếu. Đếm số ca có hai nhãn ban đầu giống nhau, chia cho 20 và đổi sang phần trăm. Mốc 80% tương đương 16 ca trùng.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

> Bản nháp: 5 ca chọn theo nhãn của người 1. Sau khi so với người 2, nếu nhãn thống nhất của ca nào khác cột "Loại lỗi" thì đổi sang ca khác cùng loại.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` với `reason = ma_khong_hop_le`, đếm theo ngày; cảnh báo khi vượt 2% số yêu cầu/ngày | Nhận diện mẫu mã đơn của sàn TMĐT và tra sang mã vận đơn; không tra được thì hiện hướng dẫn tìm mã vận đơn kèm ảnh minh hoạ, không dừng ở "mã không hợp lệ" | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi `refund_ledger_write` trạng thái ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thử thì báo khách "đang xử lý" và chuyển nhân viên (`handoff_to_staff`) | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với lý do "sai số tiền" mà kiểm tra lại thấy số tiền đúng, theo tuần; cảnh báo khi vượt 1% số yêu cầu | Mẫu tin nhắn hoàn tiền luôn ghi cách tính, ví dụ "30.000 đ × 50% = 15.000 đ", kèm điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`, theo loại yêu cầu và theo tuần | Giữ cách nói rõ "không xác định được" và chuyển nhân viên kèm tóm tắt; đưa loại `quoc_te` ra khỏi phạm vi pilot (xem A3) | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần (`audit_sample_checked`) so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace của mỗi lần chạy | Kế toán trưởng |
