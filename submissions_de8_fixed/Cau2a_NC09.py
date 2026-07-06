# Câu 2a: Đếm số tất cả chữa ký tự số
s = input().strip()
count = sum(1 for c in s if c.isdigit())
print(count)
