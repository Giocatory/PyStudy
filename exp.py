from fractions import Fraction as f
from math import factorial as fack

n = int(input())
list_results = []
for i in range(1, n+1):
    for j in range(n, 0, -1):
        if i + j == n and i < j:
            list_results.append(f"{i}/{j}")
res = [f(i) for i in list_results]
max_num = res[0].numerator  # числитель
max_den = res[0].denominator  # знаменатель
for i in res:
    if i.numerator >= max_num and i.denominator >= max_den:
        max_num = i.numerator
        max_den = i.denominator
print(f"{max_num}/{max_den}")

