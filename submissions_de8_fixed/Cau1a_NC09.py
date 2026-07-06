# Câu 1a: In ra các số nguyên tố nằm trong đoạn [m, n]
m, n = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

primes = []
for i in range(m, n + 1):
    if is_prime(i):
        primes.append(i)

if primes:
    print(' '.join(map(str, primes)))
else:
    print("Khong co so nguyen to")
