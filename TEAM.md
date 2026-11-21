# Team

## Thông tin nhóm

- Tên nhóm: NhomTTBH
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-NhomTTBH-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/NguyenDacThe/K5-L3A-DAY13-NhomTTBH-LaunchEconomics.git
- Nhánh nộp: `main`
- Commit chốt: ghi mã commit sau khi nhóm chốt hồ sơ và push.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trương Văn Thông | 2A202603560 | thongthong2k41306@gmail.com | thongthong2k41306-beep | Viết code và kiểm số nhiệm vụ A |
|   2 | Nguyễn Đắc Thể | 2A202603529 | dacthebn@gmail.com | NguyenDacThe | Người 2 · Kiểm số CP1–CP2, phụ trách pilot CP4 và tiếp quản code sau bàn giao |
|   3 | Phan Gia Bảo | 2A202603562 | pgb4work@gmail.com | pgb4work-ai-vinuni | Người gắn nhãn 1 · Phụ trách nhiệm vụ C (bảng lỗi) và E (chỉ số, event, rủi ro, nháp hồ sơ) |
|   4 | Nguyễn Quốc Hưng | 2A202603553 | Chờ xác nhận | hung309911 | Bổ sung code và kế hoạch CP4, phụ trách phiếu thứ hai của CP3 |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Trương Văn Thông-2A202603560

### Phần việc phụ trách

- Nhiệm vụ A (CP1), mô hình chi phí mỗi việc thành công.

### Đóng góp cụ thể

- Phụ trách phần code A1–A4 và đối chiếu bảng chi phí với kết quả chạy từ CSV. Xem báo cáo cá nhân để biết phần hỗ trợ của Codex.

### Bằng chứng

- [Code nhiệm vụ A](src/lab13.py), [bảng chi phí A1–A4](report/team/bang_chi_phi.md) và [báo cáo cá nhân](report/team/2A202603560_TruongVanThong.md).

## Nguyễn Đắc Thể-2A202603529

### Phần việc phụ trách

- Kiểm số A/B, tính cỡ mẫu và đề xuất kế hoạch pilot CP4.

### Đóng góp cụ thể

- Đối chiếu chi phí từ hai CSV, lập bảng độ nhạy và bổ sung thiết kế thí nghiệm, ngưỡng dừng và phương án quay về luồng thủ công.

### Bằng chứng

- [Bảng chi phí](report/team/bang_chi_phi.md), [kế hoạch pilot](report/team/pilot_plan.yaml) và [báo cáo cá nhân](report/team/2A202603529_NguyenDacThe.md).

## PhanGiaBao-2A202603562

### Phần việc phụ trách

- Nhiệm vụ C: gắn nhãn độc lập 20 ca (người gắn nhãn 1), bảng khắc phục 5 ca.
- Nhiệm vụ E: `chi_so.md` (ba chỉ số, hai chỉ số tự đề xuất, danh sách event và ba dòng rủi ro kinh tế), cùng bản nháp `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Ba chỉ số trong đợt chạy thử: 82,83% (994/1.200) · 27,12% (48/177) · 4,25% (51/1.200).
- Bảng khắc phục ca 9, 7, 18, 4, 17, mỗi dòng có event, ngưỡng và vai trò phụ trách.
- Rủi ro kinh tế lấy số từ bảng độ nhạy: 6.787 đ, 11.743–12.415 đ, 2.370 đ/việc (simulated).

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/2A202603562_PhanGiaBao.md`.

## Nguyễn Quốc Hưng-2A202603553

### Phần việc phụ trách

- CP3 và CP4, gồm phiếu cá nhân, cỡ mẫu và quy tắc vận hành pilot.

### Đóng góp cụ thể

- Bổ sung lệnh chạy riêng CP4, phép kiểm power và tiêu chí đủ mẫu khi số yêu cầu giữa các nhân viên không đều. Phiếu CP3 hiện là bản đề xuất có AI hỗ trợ, chờ xác nhận nhãn độc lập.

### Bằng chứng

- [Mã CP4](src/lab13_cp4.py), [kế hoạch pilot](report/team/pilot_plan.yaml) và [báo cáo cá nhân](report/team/2A202603553_NguyenQuocHung.md).
