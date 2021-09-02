arr = {}
for i in range(int(input())):
    name, m = input().split()
    name = name.lower()
    m = m.lower()
    if m.lower() not in arr:
        arr[m.lower()] = arr.get(m.lower(), [])
    arr[m.lower()].append(name.lower())
for j in range(int(input())):
    s = input().lower()
    if s in arr:
        print(*arr[s])
    else:
        print("абонент не найден")
#######################################################################################################
n = int(input())
phonebook = {}

for _ in range(n):
    phone, name = input().lower().split()
    phonebook[name] = phonebook.get(name, []) + [phone]

m = int(input())

for _ in range(m):
    name = input().lower()
    print(*phonebook.get(name, ['абонент не найден']))
