# common/deletedanhmuc.py
import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql   # dùng hàm connect_mysql bạn đã có

def delete_danhmuc(madm: int) -> bool:
    """Xóa 1 danh mục theo madm. Trả về True nếu xóa được, False nếu không."""
    try:
        conn = connect_mysql()
        if not conn:
            return False

        cur = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE madm = %s"
        cur.execute(sql, (madm,))
        ok = cur.rowcount > 0

        if ok:
            print(f"🗑️  Đã xóa danh mục madm = {madm}")
        else:
            print(f"ℹ️  Không tìm thấy danh mục madm = {madm}")

        cur.close()
        conn.close()
        return ok

    except Error as e:
        print("❌ Lỗi xóa danh mục:", e)
        return False
