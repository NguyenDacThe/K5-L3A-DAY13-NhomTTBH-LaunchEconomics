# Báo cáo cá nhân — Phan Gia Bảo

## 1. Thông tin thành viên

- **Họ tên:** Phan Gia Bảo
- **MSSV:** 2A202603562
- **Email:** pgb4work@gmail.com
- **GitHub:** [giabao-vinuni-ai20k](https://github.com/pgb4work-ai-vinuni)
- **Vai trò:** Người gắn nhãn 1; phụ trách nhiệm vụ C (bảng lỗi) và nhiệm vụ E (chỉ số, event, rủi ro kinh tế, nháp hồ sơ launch v0).

## 2. Phần việc phụ trách

- Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR (cột "Nhãn người 1"); chọn 5 ca, mỗi loại một ca, và điền bảng khắc phục.
- Nhiệm vụ E1: tính thử ba chỉ số trên 1.200 yêu cầu, đề xuất thêm một chỉ số dùng và một chỉ số an toàn, lập danh sách event và kiểm tra chéo chỉ số với event.
- Nhiệm vụ E2: viết ba dòng rủi ro kinh tế, số lấy từ bảng độ nhạy và A4.
- Nháp `ho_so_launch_v0.md`: điền các mục 1–4, 6 và 7 từ số đã có; mục 5 chờ đồng thuận phần C.

## 3. Đóng góp cụ thể

- Gắn nhãn đủ 20 ca, không trao đổi với người gắn nhãn 2, trước khi so nhãn. Theo nhãn của tôi: Do người dùng 4 ca (1, 6, 9, 14), Hệ thống 4 ca (2, 7, 15, 20), Ngữ cảnh 3 ca (10, 16, 18), Giới hạn hệ thống 4 ca (4, 11, 13, 19), Ngầm 5 ca (3, 5, 8, 12, 17).
- Bảng khắc phục 5 ca: ca 9 (Do người dùng), 7 (Hệ thống), 18 (Ngữ cảnh), 4 (Giới hạn hệ thống), 17 (Ngầm). Mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách. Ví dụ ca 7: đối soát mỗi giờ tin nhắn "đã hoàn" không có `refund_ledger_write` ok cùng `trace_id`, ngưỡng 0 ca, Kỹ sư trưởng agent phụ trách.
- Ba chỉ số trong đợt chạy thử: chỉ số chính **82,83%** (994/1.200), tỉ lệ bỏ qua gợi ý **27,12%** (48/177), tỉ lệ mở lại 7 ngày **4,25%** (51/1.200; 3,97% trong phạm vi `noi_dia` + `hang_nang`).
- Danh sách **10 event** có `trace_id`; cả năm chỉ số trong `chi_so.md` đều tính được từ danh sách này.
- Ba dòng rủi ro kinh tế: làm lại gấp đôi lên **6.787 đ** (+51,8%); xem lại 100% lên **11.743 đ = 0,98×** hoặc **12.415 đ = 1,03×** nếu làm lại 15,3 phút; khối lượng giảm một nửa làm chi phí cố định thành **2.370 đ/việc** (tất cả simulated).

## 4. Bằng chứng

- [Bảng lỗi](bang_loi.md): cột "Nhãn người 1" và bảng khắc phục 5 ca.
- [Chỉ số, event, rủi ro](chi_so.md): bảng E1, danh sách event, kiểm tra chéo, bảng E2.
- [Hồ sơ launch v0](ho_so_launch_v0.md): bản nháp mục 1–4 và 7.
- Công thức ba chỉ số (ghi trong `chi_so.md`): `((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)).mean()`; `reqs[reqs.duoc_xem_lai == 1].quyet_dinh_xem_lai.isin(['sua', 'bo']).mean()`; `(reqs.mo_lai_trong_7_ngay == 1).mean()`.

## 5. Công cụ AI đã dùng

- **Claude:** đọc đề và tóm tắt yêu cầu; giải thích định nghĩa năm loại lỗi. Claude **không** gắn nhãn hộ; cột "Nhãn người 1" do tôi tự gắn.
- Claude nháp bảng khắc phục 5 ca dựa trên nhãn của tôi, nháp `chi_so.md` (chỉ số, event, rủi ro) và nháp hồ sơ launch v0.
- **Cách tự kiểm tra:** chạy lại công thức ba chỉ số trên `logix_requests.csv` (đọc với `keep_default_na=False`) và so với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, khớp cả ba. Các số rủi ro (6.787 đ, 11.743 đ, 1.185 đ, 2.370 đ) khớp số đối chiếu và cần so lại với output `src/lab13.py` của nhóm. Đọc lại từng event để bảo đảm mỗi chỉ số có event để tính.

## 6. Tự đánh giá

- Hoàn thành phần việc của người gắn nhãn 1 và nhiệm vụ E1, E2. Phần đồng thuận và nhãn thống nhất chờ người gắn nhãn 2.
- Điểm cần giữ: giải thích được vì sao mỗi ca thuộc loại đã chọn (theo nguyên nhân gốc) và mỗi chỉ số tính từ event nào.
- Hạn chế: bảng khắc phục chọn theo nhãn của tôi, có thể phải đổi ca nếu nhãn thống nhất khác; số chi phí là simulated, cần thay bằng phút đo thật trong pilot.
