# Câu 2a: Sắp xếp danh sách bằng bubble sort
data = list(map(int, input().split()))
n = len(data)
for i in range(n):
    for j in range(n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print(' '.join(map(str, data)))
