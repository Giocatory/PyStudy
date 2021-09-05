from itertools import groupby

s = input()
res = [list(v) for k, v in groupby(s.split())]
print(res)