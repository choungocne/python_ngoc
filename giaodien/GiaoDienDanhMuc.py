# app_danhmuc.py
import tkinter as tk
from tkinter import ttk, messagebox
from mysql.connector import Error, errorcode
from ketnoidb.ketnoi_mysql import connect_mysql

APP_TITLE = "Quản lý Danh mục (Tkinter + MySQL)"
APP_WIDTH, APP_HEIGHT = 880, 540

class DanhMucApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.minsize(APP_WIDTH, APP_HEIGHT)

        # ====== UI: Form nhập ======
        frm_form = ttk.LabelFrame(self, text="Thông tin danh mục")
        frm_form.pack(side="top", fill="x", padx=10, pady=(10, 6))

        ttk.Label(frm_form, text="Mã DM (madm):").grid(row=0, column=0, sticky="w", padx=8, pady=6)
        self.ent_madm = ttk.Entry(frm_form, width=15, state="readonly")
        self.ent_madm.grid(row=0, column=1, sticky="w", padx=8, pady=6)

        ttk.Label(frm_form, text="Tên danh mục (tendm):").grid(row=0, column=2, sticky="w", padx=8, pady=6)
        self.ent_tendm = ttk.Entry(frm_form, width=40)
        self.ent_tendm.grid(row=0, column=3, sticky="w", padx=8, pady=6)

        ttk.Label(frm_form, text="Mô tả (mota):").grid(row=1, column=0, sticky="w", padx=8, pady=6)
        self.txt_mota = tk.Text(frm_form, width=60, height=4)
        self.txt_mota.grid(row=1, column=1, columnspan=3, sticky="we", padx=8, pady=6)

        for i in range(4):
            frm_form.grid_columnconfigure(i, weight=1)

        # ====== UI: Nút chức năng ======
        frm_actions = ttk.Frame(self)
        frm_actions.pack(side="top", fill="x", padx=10, pady=(0, 8))

        self.btn_add = ttk.Button(frm_actions, text="➕ Thêm", command=self.on_add)
        self.btn_add.pack(side="left", padx=5)

        self.btn_update = ttk.Button(frm_actions, text="📝 Sửa", command=self.on_update)
        self.btn_update.pack(side="left", padx=5)

        self.btn_delete = ttk.Button(frm_actions, text="🗑️ Xóa", command=self.on_delete)
        self.btn_delete.pack(side="left", padx=5)

        self.btn_clear = ttk.Button(frm_actions, text="✦ Mới/Clear", command=self.clear_form)
        self.btn_clear.pack(side="left", padx=5)

        self.btn_refresh = ttk.Button(frm_actions, text="⟳ Tải lại", command=self.load_data)
        self.btn_refresh.pack(side="left", padx=5)

        # ====== UI: Bảng hiển thị ======
        frm_table = ttk.Frame(self)
        frm_table.pack(side="top", fill="both", expand=True, padx=10, pady=(0, 10))

        columns = ("madm", "tendm", "mota")
        self.tree = ttk.Treeview(frm_table, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("madm", text="Mã")
        self.tree.heading("tendm", text="Tên danh mục")
        self.tree.heading("mota", text="Mô tả")

        self.tree.column("madm", width=80, anchor="center")
        self.tree.column("tendm", width=260, anchor="w")
        self.tree.column("mota", width=420, anchor="w")

        vsb = ttk.Scrollbar(frm_table, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(frm_table, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        frm_table.grid_rowconfigure(0, weight=1)
        frm_table.grid_columnconfigure(0, weight=1)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Nạp dữ liệu ban đầu
        self.load_data()

    # ===================== DB helpers =====================
    def query_all(self):
        conn = connect_mysql()
        if not conn:
            messagebox.showerror("Lỗi", "Không kết nối được CSDL.")
            return []
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT madm, tendm, mota FROM danhmuc ORDER BY madm;")
            rows = cur.fetchall()
            return rows or []
        except Error as e:
            messagebox.showerror("Lỗi truy vấn", str(e))
            return []
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def insert_dm(self, tendm: str, mota: str | None):
        conn = connect_mysql()
        if not conn:
            messagebox.showerror("Lỗi", "Không kết nối được CSDL.")
            return None
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)", (tendm, mota))
            new_id = cur.lastrowid
            return new_id
        except Error as e:
            messagebox.showerror("Lỗi thêm danh mục", str(e))
            return None
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def update_dm(self, madm: int, tendm: str, mota: str | None):
        conn = connect_mysql()
        if not conn:
            messagebox.showerror("Lỗi", "Không kết nối được CSDL.")
            return False
        try:
            cur = conn.cursor()
            cur.execute("UPDATE danhmuc SET tendm=%s, mota=%s WHERE madm=%s", (tendm, mota, madm))
            return cur.rowcount > 0
        except Error as e:
            messagebox.showerror("Lỗi cập nhật", str(e))
            return False
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def delete_dm(self, madm: int):
        conn = connect_mysql()
        if not conn:
            messagebox.showerror("Lỗi", "Không kết nối được CSDL.")
            return False
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM danhmuc WHERE madm=%s", (madm,))
            return cur.rowcount > 0
        except Error as e:
            # Nếu dính ràng buộc FK (1451)
            if getattr(e, "errno", None) == errorcode.ER_ROW_IS_REFERENCED_2:
                messagebox.showwarning("Không thể xóa",
                                       "Danh mục còn sản phẩm tham chiếu.\n"
                                       "Chuyển/xóa sản phẩm trước hoặc bật ON DELETE CASCADE.")
            else:
                messagebox.showerror("Lỗi xóa", str(e))
            return False
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    # ===================== UI actions =====================
    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        rows = self.query_all()
        for r in rows:
            self.tree.insert("", "end", iid=str(r["madm"]),
                             values=(r["madm"], r["tendm"], r.get("mota") or ""))

    def clear_form(self):
        self.ent_madm.configure(state="normal")
        self.ent_madm.delete(0, "end")
        self.ent_madm.configure(state="readonly")
        self.ent_tendm.delete(0, "end")
        self.txt_mota.delete("1.0", "end")
        self.tree.selection_remove(self.tree.selection())

    def on_tree_select(self, _event):
        sel = self.tree.selection()
        if not sel:
            return
        item_id = sel[0]
        madm, tendm, mota = self.tree.item(item_id, "values")

        self.ent_madm.configure(state="normal")
        self.ent_madm.delete(0, "end")
        self.ent_madm.insert(0, madm)
        self.ent_madm.configure(state="readonly")

        self.ent_tendm.delete(0, "end")
        self.ent_tendm.insert(0, tendm)

        self.txt_mota.delete("1.0", "end")
        self.txt_mota.insert("1.0", mota or "")

    def on_add(self):
        tendm = self.ent_tendm.get().strip()
        mota = self.txt_mota.get("1.0", "end").strip() or None
        if not tendm:
            messagebox.showwarning("Thiếu dữ liệu", "Tên danh mục không được rỗng.")
            return
        new_id = self.insert_dm(tendm, mota)
        if new_id:
            messagebox.showinfo("Thành công", f"Đã thêm danh mục (madm={new_id}).")
            self.clear_form()
            self.load_data()

    def on_update(self):
        madm_txt = self.ent_madm.get().strip()
        if not madm_txt:
            messagebox.showwarning("Chưa chọn", "Hãy chọn một danh mục ở bảng để sửa.")
            return
        tendm = self.ent_tendm.get().strip()
        mota = self.txt_mota.get("1.0", "end").strip() or None
        if not tendm:
            messagebox.showwarning("Thiếu dữ liệu", "Tên danh mục không được rỗng.")
            return

        if self.update_dm(int(madm_txt), tendm, mota):
            messagebox.showinfo("Thành công", "Đã cập nhật danh mục.")
            self.load_data()
        else:
            messagebox.showwarning("Không thay đổi", "Không có dòng nào được cập nhật.")

    def on_delete(self):
        madm_txt = self.ent_madm.get().strip()
        if not madm_txt:
            messagebox.showwarning("Chưa chọn", "Hãy chọn một danh mục ở bảng để xóa.")
            return
        if not messagebox.askyesno("Xác nhận xóa", f"Bạn chắc chắn xóa madm={madm_txt}?"):
            return
        if self.delete_dm(int(madm_txt)):
            messagebox.showinfo("Thành công", "Đã xóa danh mục.")
            self.clear_form()
            self.load_data()

if __name__ == "__main__":
    app = DanhMucApp()
    app.mainloop()
