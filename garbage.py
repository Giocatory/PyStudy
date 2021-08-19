# объявление функции
import math


def compute_binom(n, k):
    nf = math.factorial(n)
    kf = math.factorial(k)
    nmk = math.factorial(n-k)
    return nf / (kf*nmk)


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))


