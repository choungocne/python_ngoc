import mysql.connector
from mysql.connector import Error

def connect_mysql(
    host='localhost',
    user='root',
    password='',
    database='QLThuoc'
):
    """Trả về đối tượng connection nếu kết nối thành công, ngược lại trả về None."""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            autocommit=True
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi kết nối MySQL:", e)

    return None
