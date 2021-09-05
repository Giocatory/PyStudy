n = int(input())
h = ''
matrix = [[int(j) for j in input().split()] for i in range(n)]

for k in range(0, n - 1):
    for l in range(k + 1, n):
        if matrix[k][l] != matrix[l][k]:
            h = 'False'
            break
if h != 'False':
    print('YES')
else:
    print('NO')
