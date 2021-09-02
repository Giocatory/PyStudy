n = int(input())
my_dic = {}
for _ in range(n):
    s = input().split()
    my_dic[s[0]] = s[1::]
m = int(input())
for _ in range(m):
    s = input()
    for key, val in my_dic.items():
        if s in val:
            print(key)
