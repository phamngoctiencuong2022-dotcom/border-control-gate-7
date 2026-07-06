# Câu 5a: HinhTru - tính diện tích
import math

class HinhTru:
    def __init__(self, r, h):
        self.r = r
        self.h = h
    
    def dien_tich(self):
        return math.pi * self.r * self.r

ht = HinhTru(5, 10)
print(round(ht.dien_tich(), 1))
