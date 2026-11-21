# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): NhomTTBH, lớp L3A.
- Nhóm được chấm: NhomCDEF, lớp L3A.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **5** | Đề xuất Go có điều kiện khớp số liệu, nêu đủ số bất lợi về kinh tế: xem lại 100% lên 11.743–12.415 đ = 0,98–1,03×, nửa khối lượng cố định lên 2.370 đ, power ≈ 0,64 ở mức +5 điểm. Tuy nhiên Mục 5 (Bảng lỗi) đang ở trạng thái "Chưa" do thiếu phiếu độc lập thứ hai nhưng danh sách 4 điều kiện trước ngày khởi động 2026-12-07 chưa có điều kiện đóng Mục 5; điều kiện kiểm tra bật 13 event ghi phút thật lại đặt ngày 2026-12-14, sau ngày chạy 1 tuần. Có thể đạt 10/10 nếu bổ sung điều kiện đóng Mục 5. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Gắn nhãn `simulated` đầy đủ trên mọi file, trạng thái Giả lập đúng cho Mục 1, 2, 3, 7; không dùng từ cấm và không ghi "cả đội". Thu hẹp phạm vi về `noi_dia` (2.696 đ = 0,22×) + `hang_nang` (8.221 đ = 0,69×), loại `quoc_te` (22.515 đ = 1,88×, thành công 27,3%) và `doi_tac` (10.215 đ = 0,85×) có lý do bằng số rõ ràng. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | `pilot_plan.yaml` đọc hợp lệ bằng `yaml.safe_load`, 0 dấu `?`; chia ngẫu nhiên 20+20 nhân viên trên 12 depot, có đối chứng đồng thời, kiểm soát tràn tác động theo `staff_id`; tính đúng 5 câu D1 (1.251, DE=2,48, m≥299, DE=6,96, n hiệu dụng 859, nêu rõ power 0,642 ở +5 điểm); đủ 4 luật dừng chuẩn 4 vế NẾU–TRONG–THÌ–KHÔNG THÌ dựa trên tỷ lệ mở lại thực tế 4,25% (3,97% trong phạm vi), rollback 30 phút của Giám đốc vận hành. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện.

**Lý do:** Cần bổ sung điều kiện hoàn tất phiếu độc lập Mục 5 và kiểm tra bật đủ 13 event thành cổng chặn bắt buộc trước ngày khởi động pilot 2026-12-07.

**Một câu hỏi cho đội trình:** Mục 5 (Bảng lỗi) trong hồ sơ đang ở trạng thái "Chưa" do thiếu phiếu gắn nhãn độc lập thứ hai, nhưng danh sách 4 điều kiện trước ngày chạy 2026-12-07 lại không có điều kiện đóng Mục 5; đồng thời điều kiện kiểm tra bật 13 event ghi phút thật đặt ngày 2026-12-14 (sau khi chạy 1 tuần). Nhóm có bổ sung hai điều kiện này thành cổng chặn bắt buộc trước ngày khởi động pilot không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Có. Nhóm CDEF thống nhất bổ sung hai điều kiện sau thành cổng chặn bắt buộc trước ngày khởi động pilot 2026-12-07:

1. Hoàn tất phiếu gắn nhãn độc lập thứ hai cho Mục 5 (Bảng lỗi), đối chiếu hai phiếu, xử lý các nhãn bất đồng và lưu bằng chứng trước khi xác nhận đóng Mục 5.
2. Chuyển kiểm tra bật đủ 13 event và ghi nhận số phút thực tế từ ngày 2026-12-14 lên trước ngày 2026-12-07. Chạy thử để xác nhận từng event được ghi nhận và dữ liệu thời gian được lưu đầy đủ; lưu kết quả kiểm tra để hội đồng đối chiếu. Mốc 2026-12-14 chỉ dùng để rà soát dữ liệu sau tuần chạy đầu tiên.

Nhóm sẽ cập nhật hai điều kiện vào danh sách điều kiện trước khi chạy và trình Giám đốc vận hành xác nhận bằng chứng. Nếu còn thiếu bất kỳ điều kiện nào, pilot chưa được khởi động; nhóm sẽ lùi lịch và chỉ bắt đầu sau khi cả hai điều kiện được xác nhận hoàn tất. Câu trả lời này là cam kết bổ sung điều kiện, chưa phải bằng chứng đã hoàn tất; điểm hiện tại giữ ở 25/30 cho đến khi hội đồng kiểm tra lại hồ sơ.
