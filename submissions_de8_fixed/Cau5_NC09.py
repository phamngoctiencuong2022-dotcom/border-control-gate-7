# Câu 5: Xây dựng lớp NhanVienBanHang
class NhanVien:
    def __init__(self, ten, luong_cb):
        self.ten = ten
        self.luong_cb = luong_cb
    
    def tinh_luong(self):
        return self.luong_cb

class NhanVienBanHang(NhanVien):
    def __init__(self, ten, luong_cb, doanh_thu):
        super().__init__(ten, luong_cb)
        self.doanh_thu = doanh_thu
    
    def tinh_luong(self):
        # Lương cơ bản + 5% doanh thu
        return self.luong_cb + (self.doanh_thu * 0.05)
    
    def in_thong_tin(self):
        print(f"Tên: {self.ten}")
        print(f"Lương cơ bản: {self.luong_cb}")
        print(f"Doanh thu: {self.doanh_thu}")
        print(f"Lương tổng: {self.tinh_luong()}")

# Test
nv = NhanVienBanHang("Nguyễn Văn A", 5000000, 10000000)
nv.in_thong_tin()
