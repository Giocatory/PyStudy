t = [int(i) for i in input().split()]
n = t[0]
m = t[1]
count = 1
mat, temp = [], []
for i in range(n):
    for j in range(m):
        temp.append(count)
        count += 1
    mat.append(temp)
    temp = []
    if i % 2 != 0:
        mat[i] = mat[i][::-1]

for i in range(n):
    for j in range(m):
        print(str(mat[i][j]).ljust(3, ' '), end='')
    print()
