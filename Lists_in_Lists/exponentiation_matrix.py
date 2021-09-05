import numpy as np

n = int(input())
mat = [[int(j) for j in input().split()] for i in range(n)]
exponent = int(input())

res_mat = np.linalg.matrix_power(mat, exponent)

for i in res_mat:
    print(*i)
