# Câu 1a: Tính số Fibonacci thứ n
n = int(input())
if n == 0:
	print(0)
elif n == 1:
	print(1)
else:
	a, b = 0, 1
	for _ in range(n - 1):
		a, b = b, a + b
	print(b)
