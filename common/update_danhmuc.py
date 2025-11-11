import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def update_danhmuc(madm: int, tendm: str, mota: str | None = None) -> bool:
    """Cập nhật tên/mô tả cho danh mục theo madm. Trả về True nếu cập nhật được."""
    if not isinstance(madm, int):
        raise ValueError("madm phải là số nguyên")
    if not tendm:
        raise ValueError("tendm không được rỗng")

    try:
        conn = connect_mysql()
        if not conn:
            return False
        cur = conn.cursor()
        sql = "UPDATE danhmuc SET tendm=%s, mota=%s WHERE madm=%s"
        cur.execute(sql, (tendm, mota, madm))
        ok = cur.rowcount > 0
        if ok:
            print(f"📝 Đã cập nhật madm={madm} -> tendm='{tendm}'")
        else:
            print(f"ℹ️  Không tìm thấy madm={madm}")
        cur.close()
        conn.close()
        return ok
    except Error as e:
        print("❌ Lỗi cập nhật danh mục:", e)
        return False
