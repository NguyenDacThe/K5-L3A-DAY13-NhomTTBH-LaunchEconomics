# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Đối chiếu phiếu của Bảo với bản đề xuất

Người gắn nhãn 1: Phan Gia Bảo. Cột nhãn người 1 giữ nguyên đủ 20 nhãn Bảo đã ghi.

Người gắn nhãn 2: Nguyễn Quốc Hưng.

| Ca | Nhãn gốc của Bảo | Nhãn từ bản đề xuất có AI hỗ trợ | Trùng? | Nhãn đề xuất sau đối chiếu |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngầm | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ trùng khi đối chiếu bản đề xuất:** 18/20 = 90%. Hai ca khác nhãn là 3 và 8. Tỉ lệ đồng thuận giữa hai người gắn nhãn độc lập vẫn chưa xác định.

## Quy tắc phân biệt cho các ca không trùng

- **Ca 3 → Ngữ cảnh.** Khoản hoàn về ví LogiX đúng thiết kế, còn khách chờ tiền về tài khoản ngân hàng. Điểm lệch nằm ở kỳ vọng về nơi nhận tiền.
- **Ca 8 → Hệ thống.** Điều khoản sai xuất hiện ngay trong câu trả lời và có thể kiểm tra trực tiếp. Dùng nhãn Ngầm khi sai sót chỉ lộ ra qua kiểm tra hoặc đối soát về sau.

Hai nhãn đề xuất được rà theo [hướng dẫn nhiệm vụ C](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhiệm-vụ-c--bảng-lỗi-và-cách-khắc-phục-30-phút).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

Năm ca dưới đây có nhãn trùng khớp trong cả hai cột đối chiếu và đại diện đủ năm loại lỗi.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Mỗi ngày, chia số `request_id` duy nhất có `input_validation_failed` với `reason = ma_khong_hop_le` cho số yêu cầu tạo trong ngày. Cảnh báo khi vượt 2% | Nhận diện mẫu mã đơn của sàn TMĐT và tra sang mã vận đơn. Nếu tra chưa được, hiện hướng dẫn tìm mã vận đơn kèm ảnh minh họa | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: `refund_notification_sent` trạng thái `da_hoan` phải có `refund_ledger_write` trạng thái `ok` trước đó cho cùng `request_id`. Cảnh báo từ 1 ca sai | Chỉ báo "đã hoàn" khi sổ cái xác nhận. Nếu vẫn gặp lỗi 503 khi hết số lượt cho phép, báo khách "đang xử lý" và tạo `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Mỗi tuần, đếm yêu cầu mở lại vì số tiền bị hiểu sai dù đối soát xác nhận khoản hoàn đúng. Chia cho số yêu cầu hoàn tiền đã đóng và đủ 7 ngày theo dõi. Cảnh báo khi vượt 1% | Mẫu tin nhắn hoàn tiền luôn ghi cách tính, ví dụ "30.000 đ × 50% = 15.000 đ", kèm điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Mỗi ngày, nối `refund_request_created` với `agent_run_completed` theo `request_id`. Cảnh báo từ 1 yêu cầu `quoc_te` bị đưa vào agent của pilot. Nếu agent thiếu dữ liệu, kiểm tra có `handoff_to_staff` với lý do `thieu_du_lieu` | Định tuyến `quoc_te` về luồng thủ công ngay từ đầu. Khi phát hiện thiếu dữ liệu, nói rõ giới hạn và chuyển nhân viên kèm tóm tắt | PM trợ lý hoàn phí |
| 17 | Ngầm | Mỗi tuần, dùng `audit_sample_checked` để so tiền thực hoàn với tiền đúng theo phiên bản bảng giá áp dụng. Cảnh báo từ 1 đơn lệch trong mẫu 100 đơn | Xóa bộ nhớ đệm khi có bảng giá mới và ghi phiên bản bảng giá vào trace của mỗi lần chạy | Kế toán trưởng |
