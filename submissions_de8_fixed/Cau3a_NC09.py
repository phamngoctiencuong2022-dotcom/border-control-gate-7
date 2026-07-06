# Câu 3a: Tạo hai danh sách mới, một chứa sô lẻ và một chứa số chẵn tự danh sách ban đầu
nums = list(map(int, input().split()))
odd = [x for x in nums if x % 2 != 0]
even = [x for x in nums if x % 2 == 0]
print(' '.join(map(str, odd)))
print(' '.join(map(str, even)))
