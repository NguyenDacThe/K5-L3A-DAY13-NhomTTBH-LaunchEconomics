"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py (cần pandas).
Kiểm tra riêng nhiệm vụ D bằng python3 lab13.py --cp4.
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import argparse
import math

from lab13_cp4 import PHAM_VI_PILOT, doc_yeu_cau, in_ket_qua_cp4

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if p == 0:
        return math.inf if k is None else k
    return 1 / p if k is None else ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí theo tập yêu cầu, gồm chi phí chạy lại và hóa đơn mỗi yêu cầu.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    cot_phut = ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        reqs = reqs.copy()
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, cot_phut] = 0

    tien_token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    xem_lai = reqs[cot_phut[0]].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs[cot_phut[1]].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = reqs['ket_qua'].eq('thanh_cong').sum()
    return dict(
        token=token, tool=tool,
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai, lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else math.inf,
        hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else math.nan,
    )


def in_bang_do_nhay(runs, reqs, chi_phi_goc, pham_vi, ket_qua_pilot):
    kich_ban = (
        ('Giá token gấp đôi', dict(gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA)),
        ('Giá token giảm một nửa', dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2)),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', dict(luong_phut=1.25 * LUONG_PHUT)),
        ('Tối đa 2 lần chạy', dict(max_lan_chay=2)),
        ('Chỉ 1 lần chạy', dict(max_lan_chay=1)),
    )
    print('\nB1 · Kịch bản | chi phí mỗi việc thành công | thay đổi so với A2 [simulated]')
    thay_doi = []
    ket_qua_theo_gioi_han = {}
    for ten, tham_so in kich_ban:
        ket_qua = mo_hinh(runs, reqs, **tham_so)
        cps = ket_qua['cps']
        chenh = cps / chi_phi_goc - 1
        thay_doi.append((ten, chenh))
        if 'max_lan_chay' in tham_so:
            ket_qua_theo_gioi_han[tham_so['max_lan_chay']] = ket_qua
        print(f'{ten:28s} {cps:9,.0f} đ {chenh:+.1%}')

    cps_cap = mo_hinh(runs, reqs, gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Gấp đôi giá token và tỉ lệ xem lại: {cps_cap:,.0f} đ ({cps_cap / chi_phi_goc - 1:+.1%}) [simulated]')
    ba_yeu_to = sorted(thay_doi, key=lambda muc: muc[1], reverse=True)[:3]
    print('Ba yếu tố làm chi phí tăng mạnh nhất:', ' · '.join(f'{ten} ({chenh:+.1%})' for ten, chenh in ba_yeu_to))

    print('\nB3 · Giới hạn | trợ lý | không thành công | cả hệ thống | chi phí mỗi việc thành công [simulated]')
    ket_qua_theo_gioi_han[3] = mo_hinh(runs, reqs, max_lan_chay=3)
    chi_phi_he_thong = {}
    for gioi_han, ket_qua in sorted(ket_qua_theo_gioi_han.items()):
        ca_lam_tay = len(reqs) - ket_qua['thanh_cong']
        tong_he_thong = ket_qua['tong'] + ca_lam_tay * BASELINE
        chi_phi_he_thong[gioi_han] = tong_he_thong
        print(f"{gioi_han} lượt | {ket_qua['tong']:,.0f} đ | {ca_lam_tay} | {tong_he_thong:,.0f} đ | {ket_qua['cps']:,.0f} đ")
    re_nhat = min(chi_phi_he_thong, key=chi_phi_he_thong.get)
    cps_thap_nhat = min(ket_qua_theo_gioi_han, key=lambda k: ket_qua_theo_gioi_han[k]['cps'])
    print(f'Rẻ nhất cho cả hệ thống: {re_nhat} lượt. Chi phí mỗi việc thành công thấp nhất: {cps_thap_nhat} lượt.')

    print('\nB4 · Xem lại 100% kết quả ok trong phạm vi pilot [simulated]')
    co_ket_qua_ok = runs['request_id'].isin(pham_vi['request_id']) & runs['status'].eq('ok')
    so_xem_lai = runs.loc[co_ket_qua_ok, 'request_id'].nunique()
    so_lam_lai = pham_vi['ket_qua'].eq('lam_lai').sum()
    ha_tang = ket_qua_pilot['token'] + ket_qua_pilot['tool']
    thanh_cong = ket_qua_pilot['thanh_cong']
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean()
    print(f'{so_xem_lai} yêu cầu xem lại, {so_lam_lai} ca làm lại, {thanh_cong} việc thành công')
    for phut_lam_lai in (9, phut_lam_lai_tb):
        chi_phi_lam_lai = so_lam_lai * phut_lam_lai * LUONG_PHUT
        cps = (ha_tang + so_xem_lai * 5 * LUONG_PHUT + chi_phi_lam_lai) / thanh_cong
        phut_hoa_von = (BASELINE * thanh_cong - ha_tang - chi_phi_lam_lai) / (so_xem_lai * LUONG_PHUT)
        print(f'Làm lại {phut_lam_lai:.1f} phút/ca: {cps:,.0f} đ/việc ({cps / BASELINE:.2f}×), '
              f'hòa vốn ở {phut_hoa_von:.1f} phút xem lại/lượt')


def in_chi_so_cp5(reqs, pham_vi):
    da_dong = reqs['dong_trong_24h'].eq(1)
    mo_lai = reqs['mo_lai_trong_7_ngay'].eq(1)
    da_xem_lai = reqs[reqs['duoc_xem_lai'].eq(1)]
    bo_qua = da_xem_lai['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    print('\nE1 · Chỉ số trong đợt chạy thử')
    for ten, tu_so, mau_so in (
        ('Đóng trong 24h, không mở lại trong 7 ngày', (da_dong & ~mo_lai).sum(), len(reqs)),
        ('Sửa hoặc bỏ gợi ý', bo_qua.sum(), len(da_xem_lai)),
        ('Mở lại trong 7 ngày', mo_lai.sum(), len(reqs)),
        ('Làm lại trong phạm vi pilot', pham_vi['ket_qua'].eq('lam_lai').sum(), len(pham_vi)),
    ):
        print(f'{ten}: {tu_so}/{mau_so} ({tu_so / mau_so:.2%})')


def main():
    parser = argparse.ArgumentParser(description='Lab 13 · Kinh tế và kế hoạch pilot')
    parser.add_argument('--cp4', action='store_true', help='Chỉ in cỡ mẫu và tỉ lệ mở lại của nhiệm vụ D')
    args = parser.parse_args()
    if args.cp4:
        in_ket_qua_cp4(doc_yeu_cau())
        return

    import pandas as pd

    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print(f'A1: {so_lan_chay_ky_vong(0.8, 2):.2f} | {so_lan_chay_ky_vong(0.8):.2f} | '
          f'{he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    print('\nA2 · Chi phí từ trace')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        nhan = ' [simulated]' if ten in ('xem_lai', 'lam_lai', 'tong', 'cps') else ''
        so_le = 1 if ten == 'hoa_don_moi_yc' else 0
        print(f'{ten:17s} {gia_tri:>14,.{so_le}f}{nhan}')
    print(f"CPS / hóa đơn mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f}× [simulated]")
    print(f"Tỷ trọng làm lại: {ket_qua['lam_lai'] / ket_qua['tong']:.2%} [simulated]")
    chua_thanh_cong = len(reqs) - ket_qua['thanh_cong']
    chi_phi_he_thong = (ket_qua['tong'] + chua_thanh_cong * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống theo giả định xử lý tay {chua_thanh_cong} ca: '
          f'{chi_phi_he_thong:,.0f} đ/yêu cầu ({chi_phi_he_thong / BASELINE:.2f}×) [simulated]')

    print('\nA3 · Loại | số yêu cầu | thành công | lượt/yêu cầu | CPS và bội số [simulated]')
    for loai, nhom in reqs.groupby('loai', sort=False):
        theo_loai = mo_hinh(runs, nhom)
        cps = theo_loai['cps']
        print(f"{loai:10s} {len(nhom):4d} {theo_loai['thanh_cong'] / len(nhom):7.1%} "
              f"{nhom['so_lan_chay'].mean():6.2f} {cps:9,.0f} đ {cps / BASELINE:.2f}×")

    quoc_te = runs[runs['request_id'].isin(reqs.loc[reqs['loai'].eq('quoc_te'), 'request_id'])]
    theo_lan = quoc_te.assign(ok=quoc_te['status'].eq('ok')).groupby('attempt')['ok']
    print('Quốc tế, tỷ lệ lượt có status=ok theo từng lần thử:')
    for lan, so_lieu in theo_lan.agg(['sum', 'count']).iterrows():
        print(f"  Lần {lan}: {so_lieu['sum']}/{so_lieu['count']} ({so_lieu['sum'] / so_lieu['count']:.1%})")

    print('\nA4 · Chi phí cố định của phạm vi noi_dia + hang_nang')
    pham_vi = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    ket_qua_pilot = mo_hinh(runs, pham_vi)
    # Khối lượng tháng là tổng yêu cầu toàn hệ thống, gồm cả các loại ngoài pilot.
    ti_le_thanh_cong_pilot = ket_qua_pilot['thanh_cong'] / len(reqs)
    print(f"Tỷ lệ việc thành công trong phạm vi trên toàn mẫu: "
          f"{ket_qua_pilot['thanh_cong']}/{len(reqs)} ({ti_le_thanh_cong_pilot:.1%})")
    for khoi_luong in (45_000, 22_500):
        viec_thanh_cong = khoi_luong * ti_le_thanh_cong_pilot
        co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / viec_thanh_cong
        cps_co_dinh = ket_qua_pilot['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:,} yêu cầu/tháng | {viec_thanh_cong:,.0f} việc thành công | '
              f'{co_dinh_moi_viec:,.0f} đ cố định/việc | {cps_co_dinh:,.0f} đ/việc '
              f'({cps_co_dinh / BASELINE:.2f}×) [simulated]')

    in_bang_do_nhay(runs, reqs, ket_qua['cps'], pham_vi, ket_qua_pilot)
    print()
    in_ket_qua_cp4(reqs.to_dict(orient='records'))
    in_chi_so_cp5(reqs, pham_vi)


if __name__ == '__main__':
    main()
