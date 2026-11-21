# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NhomTTBH · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ trên toàn mẫu (simulated), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); phạm vi `noi_dia` + `hang_nang`: 3.414 đ, cộng chi phí cố định thành 4.599 đ (simulated) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (gấp đôi: +51,8%) · 2. Tỉ lệ xem lại (gấp đôi: +40,7%) · 3. Lương nhân viên (+25%: +23,1%); giá token gấp đôi chỉ +5,6% (simulated) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ (đã cộng 222 ca nhân viên làm thay); theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` 1,88×; xem lại 100% thì 0,98×–1,03× (simulated) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200; 3,97% trong phạm vi); 10 event có `trace_id` trong `chi_so.md` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; tỉ lệ đồng thuận: chờ người gắn nhãn 2; bảng khắc phục 5 ca (9, 7, 18, 4, 17), mỗi dòng có event, ngưỡng và vai trò phụ trách | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên 20 + 20 cụm, đối chứng cùng thời gian; MDE 6 điểm cần 859 yêu cầu hiệu dụng mỗi nhóm, ≥ 299 yêu cầu mỗi nhân viên (DE 6,96); nếu tác động thật chỉ 5 điểm thì power ≈ 0,64; 4 luật dừng; quyết định 2027-01-12 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | 3 dòng trong `chi_so.md`: làm lại gấp đôi lên 6.787 đ; xem lại 100% lên 11.743–12.415 đ (0,98×–1,03×); khối lượng giảm một nửa làm chi phí cố định thành 2.370 đ/việc (simulated) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện cho pilot chỉ gồm `noi_dia` + `hang_nang`; loại `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×, có điều khoản riêng) (simulated).

- Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu pilot · Kỹ sư trưởng agent · ngày kiểm tra: 2026-12-04
- Bật đủ 10 event có `trace_id`; thay phút simulated bằng phút đo thật sau tuần 1 · PM trợ lý hoàn phí · ngày kiểm tra: 2026-12-14
- Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% thì không tiết kiệm (0,98×–1,03×, simulated) · Trưởng nhóm CSKH · ngày kiểm tra: 2026-12-21
- Ký chấp nhận mức chênh 6 điểm (power chỉ ≈ 0,64 nếu tác động thật là 5 điểm) và chốt seed, danh sách phân nhóm, luật dừng trước ngày bắt đầu 2026-12-07 · Giám đốc vận hành LogiX-VN · ngày kiểm tra: 2026-12-04
