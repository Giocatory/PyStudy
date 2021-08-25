# Sample Input 1:
# a b c d e f
# 2
# Sample Output 1:
# [['a', 'b'], ['c', 'd'], ['e', 'f']]
# Sample Input 2:
# a b c d e f
# 3
# Sample Output 2:
# [['a', 'b', 'c'], ['d', 'e', 'f']]
# Sample Input 3:
# a b c d e f
# 6
# Sample Output 3:
# [['a', 'b', 'c', 'd', 'e', 'f']]
# Sample Input 4:
# a b c d e f r g b
# 2
# Sample Output 4:
# [['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
# Sample Input 5:
# a b
# 3
# Sample Output 5:
# [['a', 'b']]

s = input().split()
count = 0
temp = []
result = []
n = int(input())
for i in s:
    if n > len(s):
        result.append(s)
        break
    temp.append(i)
    count += 1
    if count == n:
        result.append(temp)
        temp = []
        count = 0
if len(s) % 2 != 0 and n % 2 == 0:
    result.append([s[-1]])

print(result)
