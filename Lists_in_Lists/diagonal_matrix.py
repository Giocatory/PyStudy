def diagonal_matrix(x, y):
    k = [[] for i in range(x)]
    k[0].append(1)
    mi = min(x, y)
    ma = max(x, y)
    co = int(-1)
    le_main_d = int(ma - (ma - mi))
    for i in range(mi - 1):
        k[0].append(k[0][-1] + i + 1)
    for i in range(y - x):
        k[0].append(k[0][-1] + x)
    for i in range(x - y):
        k[0].append(k[0][-1] + (le_main_d - 1))
        co += 1
    for i in range((x - 1) - (((x - y) > 0) * (x - y))):
        if x < y:
            k[0].append(k[0][-1] + (((le_main_d - i) + co) - (co + 1)))
            co += 1
        else:
            k[0].append(k[0][-1] + ((le_main_d - 1) - i))
    for i in range(x - 1):
        for j in range(len(k[i]) - 1):
            k[i + 1].append(k[i][j + 1] + 1)
    for i in range(len(k)):
        k[i] = k[i][0:y]
    return k


t = [int(i) for i in input().split()]
n = t[0]
m = t[1]
for i in diagonal_matrix(n, m):
    print(*i)
