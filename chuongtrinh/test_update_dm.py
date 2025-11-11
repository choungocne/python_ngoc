from common.update_danhmuc import update_danhmuc

while True:
    try:
        madm = int(input("Nhập mã danh mục (madm) cần cập nhật: ").strip())
    except ValueError:
        print("⚠️  Vui lòng nhập số nguyên!")
        continue

    ten  = input("Nhập tên danh mục mới: ").strip()
    mota = input("Nhập mô tả mới (có thể bỏ trống): ").strip() or None

    update_danhmuc(madm, ten, mota)

    con = input("TIẾP TỤC (y) / THOÁT (phím bất kỳ): ").strip().lower()
    if con != "y":
        break
