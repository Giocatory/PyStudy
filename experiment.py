n = int(input())
l = []
nl = []
chl = []
nulll = []
for _ in range(n):
    j = int(input())
    if j < 0:
        nl.append(j)
    elif j == 0:
        nulll.append(j)
    else:
        chl.append(j)
l.extend(nl)
l.extend(nulll)
l.extend(chl)
print(*l, sep='\n')
