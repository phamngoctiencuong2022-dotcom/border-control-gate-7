# Câu 2b: Thay thế tất cả các số trong chuỗi bằng dấu *
s = input().strip()
result = ''.join('*' if c.isdigit() else c for c in s)
print(result)
