s = input().split()
p = [i[1:] + i[0] + 'ки ' for i in s]
# for i in s:
#     p += i[1:] + i[0] + 'ки '
print(*p)
