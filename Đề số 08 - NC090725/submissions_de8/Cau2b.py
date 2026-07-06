# Câu 2b: Tìm phần tử xuất hiện nhiều nhất
from collections import Counter
data = list(map(int, input().split()))
counter = Counter(data)
most_common = counter.most_common(1)[0][0]
print(most_common)
