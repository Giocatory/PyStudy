# print('Сопряженное число =', z.conjugate())

n = int(input())
z1, z2 = complex(input()), complex(input())
res = z1**n + z2**n + (z1**n).conjugate() + (z2**(n+1)).conjugate()
print(res)
