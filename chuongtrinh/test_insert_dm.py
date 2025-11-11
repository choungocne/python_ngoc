from common.insert_danhmuc import insert_danhmuc

while True:
    ten = input("Nhập tên danh mục: ").strip()
    if not ten:
        print("⚠️  Tên không được rỗng!")
        continue
    mota = input("Nhập mô tả (có thể bỏ trống): ").strip() or None

    insert_danhmuc(ten, mota)

    con = input("TIẾP TỤC (y) / THOÁT (phím bất kỳ): ").strip().lower()
    if con != "y":
        break
