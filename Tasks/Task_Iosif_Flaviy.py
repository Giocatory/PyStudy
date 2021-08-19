n = int(input())
k = int(input())
p = 0
for i in range(1, n+1):
    p = (p + k) % i
print(p+1)
