# Câu 1b: Viết hàm trả về tổng các chữ số của số n
def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

n = int(input())
print(sum_digits(n))
