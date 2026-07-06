# Câu 3b: Xóa các phần tử trùng nhau trong mỗi danh sách
nums = list(map(int, input().split()))
unique = list(dict.fromkeys(nums))
print(' '.join(map(str, unique)))
