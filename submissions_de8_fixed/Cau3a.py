# Câu 3a: In các ký tự chung của hai chuỗi
s1 = input().strip()
s2 = input().strip()
common = set(s1) & set(s2)
if common:
    for c in sorted(common):
        print(c)
