from common.get_danhmuc import get_all_danhmuc, print_danhmuc

if __name__ == "__main__":
    rows = get_all_danhmuc()
    print_danhmuc(rows)
