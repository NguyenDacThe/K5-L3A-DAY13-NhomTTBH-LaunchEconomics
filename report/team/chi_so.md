# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: tỉ lệ yêu cầu đủ điều kiện trong nhóm can thiệp thực sự nhận được gợi ý | Số yêu cầu có `agent_suggestion_shown`, chia số yêu cầu đủ điều kiện có `refund_request_created`, cùng `arm = tro_ly`. Đếm theo `request_id` duy nhất | Không cần tính |
| An toàn | Nhóm tự đề xuất: tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 12, 17) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra mẫu | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng.

Tính bằng: `chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)).mean()`; `bo_qua = reqs[reqs.duoc_xem_lai == 1].quyet_dinh_xem_lai.isin(['sua', 'bo']).mean()`; `an_toan = (reqs.mo_lai_trong_7_ngay == 1).mean()`. Trong phạm vi pilot (`noi_dia` + `hang_nang`), tỉ lệ mở lại 7 ngày là 3,97%.

## Danh sách event

13 event. Mỗi event có `request_id`, `trace_id` và thời điểm ghi nhận. Nối theo `request_id` ở cấp yêu cầu, dùng `trace_id` khi đối soát từng lượt chạy.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, created_at, loai, so_tien, depot, staff_id, arm, trace_id | Khi khách gửi yêu cầu |
| `input_validation_failed` | Agent | request_id, reason (ví dụ ma_khong_hop_le), truong_loi, trace_id | Khi đầu vào của khách không hợp lệ |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, phien_ban_bang_gia, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, arm, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok/loi), trace_id | Khi ghi hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | reason (ví dụ thieu_du_lieu, ngoai_pham_vi, loi_he_thong), tom_tat, trace_id | Khi chuyển cho nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `refund_notification_sent` | Dịch vụ thông báo | message_status (da_hoan/dang_xu_ly), trace_id | Khi gửi thông báo cho khách |
| `refund_outcome_recorded` | Hệ thống ticket và sổ cái | ket_qua (thanh_cong/lam_lai/chuyen_nhan_vien), so_tien_hoan, so_tien_duyet, trace_id | Khi có đủ dữ liệu đóng, mở lại và đối soát số tiền để xác nhận kết quả |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:**

- Chỉ số chính: số yêu cầu có `ticket_closed` trong 24 giờ kể từ `refund_request_created` và không có `ticket_reopened` trong 7 ngày sau khi đóng, chia toàn bộ yêu cầu đủ điều kiện đã qua cửa sổ theo dõi.
- Tỉ lệ bỏ qua gợi ý: lấy `staff_review_decision` cuối cùng của mỗi yêu cầu đã xem lại. Chia số quyết định `sua` hoặc `bo` cho tổng số yêu cầu đã xem lại.
- Tỉ lệ mở lại: đếm mỗi yêu cầu tối đa một lần nếu có `ticket_reopened` trong 7 ngày sau đóng. Mẫu số là toàn bộ yêu cầu đủ điều kiện đã qua cửa sổ theo dõi, theo từng nhóm pilot.
- Tỉ lệ nhận gợi ý (tự đề xuất): đếm `request_id` duy nhất từ `agent_suggestion_shown` và `refund_request_created`, cùng nhóm can thiệp và phạm vi.
- Tỉ lệ hoàn sai tiền qua kiểm tra mẫu (tự đề xuất): `audit_sample_checked`.
- Chi phí mỗi việc thành công: cộng token và tool từ mọi `agent_run_completed`, cùng phút thực đo từ `staff_review_decision` và `staff_rework_completed`. Chia cho số yêu cầu có `refund_outcome_recorded` với kết quả `thanh_cong`.
- Kiểm tra thông báo hoàn tiền sớm ở CP3: đối chiếu `refund_notification_sent` có trạng thái `da_hoan` với lần ghi `refund_ledger_write` thành công trước thông báo.

Cả năm chỉ số đều tính được từ danh sách event trên.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy và A4 (`bang_chi_phi.md`). Mọi số chi phí dưới đây là simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ trên toàn mẫu B1 (simulated) | Tỉ lệ yêu cầu có `staff_rework_completed` theo tuần > 7% (đợt chạy thử: 48/982, tức 4,9% trong phạm vi) | Thu hẹp về `noi_dia`, rà 20 trace làm lại để tìm nguyên nhân | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu mỗi ca làm lại mất 15,3 phút như dữ liệu (simulated) | % yêu cầu có `staff_review_decision` còn > 50% ở cuối bước rollout 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; mục tiêu mỗi lần xem lại ≤ 5 phút | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) (simulated) | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
