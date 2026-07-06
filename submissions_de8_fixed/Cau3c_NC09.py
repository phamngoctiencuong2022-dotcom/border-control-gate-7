# Câu 3c: In ra hai danh sách kết quả theo thứ tự tăng dần
nums = list(map(int, input().split()))
result = sorted(nums)
print(' '.join(map(str, result)))
