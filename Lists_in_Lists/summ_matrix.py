t = [int(i) for i in input().split()]  # rows cols
n, m = t[0], t[1]
# init matrix 1 2 3 4 ... m
mat_one = [[int(j) for j in input().split()] for i in range(n)]
input()
mat_two = [[int(j) for j in input().split()] for i in range(n)]
# sum matrix
mat_result = [[mat_one[i][j] + mat_two[i][j] for j in range(m)] for i in range(n)]
# print result
for i in mat_result:
    print(*i)
