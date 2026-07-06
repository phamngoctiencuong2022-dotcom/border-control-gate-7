# Câu 3b: In ký tự chỉ xuất hiện trong chuỗi thứ nhất
s1 = input().strip()
s2 = input().strip()
unique = set(s1) - set(s2)
for c in sorted(unique):
	print(c)
