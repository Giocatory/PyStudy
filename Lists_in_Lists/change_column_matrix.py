n, m = int(input()), int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]
column_change = [int(i) for i in input().split()]

for i in range(n):
    for j in range(m):
        if j == column_change[1]:
            matrix[i][j], matrix[i][column_change[0]] = matrix[i][column_change[0]], matrix[i][j]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
