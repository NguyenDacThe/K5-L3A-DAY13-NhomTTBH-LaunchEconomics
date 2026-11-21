# Source code

Code khởi đầu và dữ liệu giả lập của Lab 13. **Mọi lệnh chạy trong thư mục `src/`.**

- File bắt đầu chạy: `lab13.py` (file nộp). `lab13_starter.py` là khung ban đầu để đối chiếu.
- Cách chạy: `python3 lab13.py`.
- Input: `logix_runs.csv`, `logix_requests.csv` cùng thư mục, file yêu cầu đọc bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)`.
- Output: ba phép thử A1, kết quả A2–A4, bảng độ nhạy B1–B4, cỡ mẫu D1 và số tính thử E1 để đối chiếu với `report/team/`.
- Kiểm tra riêng D1 và tỉ lệ mở lại bằng `python lab13.py --cp4`. Lệnh này dùng thư viện chuẩn Python và chạy độc lập với phần A–B.
- File học viên được sửa: `lab13.py`. Không sửa hai file CSV.

## Cài đặt

Cần Python 3.10 trở lên. Lab không cần khoá API và không cần mạng trong lúc làm.

macOS / Linux:

```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py
```

Windows PowerShell:

```powershell
cd src
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py
```

Lệnh `python -c` kiểm tra thư viện phải in ra `san sang`.

## File trong thư mục

| File | Nội dung |
| --- | --- |
| `lab13.py` | Bài làm của nhóm, in A, B, D1 và E1 từ dữ liệu gốc |
| `lab13_cp4.py` | Tính cỡ mẫu, power và tỷ lệ mở lại cho CP4 |
| `lab13_starter.py` | Bản gốc của `lab13.py`, giữ nguyên để đối chiếu. Tài liệu trong `docs/` gọi file này là "file khởi đầu" |
| `logix_runs.csv` | 1.624 lần chạy của agent |
| `logix_requests.csv` | 1.200 yêu cầu hoàn phí |
| `requirements.txt` | Thư viện cần cài |

Ý nghĩa từng cột và các công thức: [docs/du_lieu_va_cong_thuc.md](../docs/du_lieu_va_cong_thuc.md).

## Đọc dữ liệu đúng cách

```python
import pandas as pd
runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
```

Thiếu `keep_default_na=False`, ô trống trong cột `quyet_dinh_xem_lai` bị đọc thành `NaN` và các phép so sánh phía sau sai.
