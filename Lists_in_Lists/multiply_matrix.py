import numpy as np

t = [int(i) for i in input().split()]  # rows cols
n, m = t[0], t[1]
# init matrix 1 2 3 4 ... m
mat_one = [[int(j) for j in input().split()] for i in range(n)]

input()

t = [int(i) for i in input().split()]  # rows cols
n, m = t[0], t[1]
mat_two = [[int(j) for j in input().split()] for i in range(n)]

mat_res = np.dot(mat_one, mat_two)

for i in mat_res:
    print(*i)



####################### OR ###########################

# n, m = map(int, input().split())
# matr1 = [list(map(int, input().split())) for _ in range(n)]
# empty_string = input()
# m, k = map(int, input().split())
# matr2 = [list(map(int, input().split())) for _ in range(m)]
# matr3 = [[0] * k for _ in range(n)]
#
# for i in range(n):  # по строкам первой матрицы
#     for j in range(k):  # по столбцам второй матрицы
#         for l in range(m):  # по столбцам первой и строкам второй матрицы
#             matr3[i][j] = matr3[i][j] + (matr1[i][l] * matr2[l][j])
#
# [print(*s, sep=' ') for s in matr3]
