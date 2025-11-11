# file: dm_repo.py
import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql   # hoặc copy trực tiếp hàm connect_mysql vào file này

def insert_danhmuc(tendm: str, mota: str | None = None, conn=None) -> int | None:
    """
    Thêm 1 danh mục vào bảng `danhmuc`.
    Trả về madm (INT) nếu thành công, ngược lại trả về None.
    """
    assert tendm and isinstance(tendm, str), "tendm không được rỗng"

    close_conn = False
    if conn is None:
        conn = connect_mysql()
        if conn is None:
            return None
        close_conn = True

    try:
        cur = conn.cursor()
        sql = "INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)"
        cur.execute(sql, (tendm, mota))
        new_id = cur.lastrowid
        # nếu autocommit=False thì cần: conn.commit()
        print(f"✅ Đã thêm danh mục '{tendm}' với madm={new_id}")
        return new_id
    except Error as e:
        print("❌ Lỗi khi insert danh mục:", e)
        return None
    finally:
        try:
            cur.close()
        except Exception:
            pass
        if close_conn:
            conn.close()
