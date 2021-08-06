n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
print(*num_list, sep='\n')
for i in num_list:
    print(i**2 + 2*i + 1)
