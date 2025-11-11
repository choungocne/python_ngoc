from ketnoidb.ketnoi_mysql import connect_mysql

def get_all_danhmuc() -> list[dict]:
    """
    Trả về danh sách danh mục dạng list[dict] với các field:
    madm, tendm, mota. Trả về [] nếu lỗi/kết nối thất bại.
    """
    conn = connect_mysql()
    if not conn:
        return []
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT madm, tendm, mota FROM danhmuc ORDER BY madm;")
        rows = cur.fetchall()
        return rows or []
    finally:
        try:
            cur.close()
        except Exception:
            pass
        conn.close()


def print_danhmuc(rows: list[dict]) -> None:
    """In bảng danh mục gọn gàng ra console."""
    if not rows:
        print("⚠️  Không có dữ liệu danh mục.")
        return

    # Tính độ rộng cột đơn giản
    w_id   = max(4, max(len(str(r["madm"]))   for r in rows))
    w_ten  = max(6, max(len(str(r["tendm"]))  for r in rows))
    w_mota = max(6, max(len(str(r.get("mota","") or "")) for r in rows))

    # Header
    print(f"{'madm'.ljust(w_id)} | {'tendm'.ljust(w_ten)} | {'mota'.ljust(w_mota)}")
    print("-" * (w_id + w_ten + w_mota + 6))

    # Rows
    for r in rows:
        madm = str(r["madm"]).ljust(w_id)
        ten  = (r["tendm"] or "").ljust(w_ten)
        mota = (r.get("mota","") or "").ljust(w_mota)
        print(f"{madm} | {ten} | {mota}")
