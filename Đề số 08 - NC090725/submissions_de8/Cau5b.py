# Câu 5b: HinhTru - tính chu vi
import math

class HinhTru:
	def __init__(self, r, h):
		self.r = r
		self.h = h
	
	def chu_vi(self):
		return 2 * math.pi * self.r

ht = HinhTru(5, 10)
print(round(ht.chu_vi(), 1))
