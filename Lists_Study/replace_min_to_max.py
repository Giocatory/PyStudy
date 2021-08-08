s = input().split()
num_list = []
for i in s:
    num_list.append(int(i))

min_num = min(num_list)
max_num = max(num_list)
index_min = num_list.index(min_num)
index_max = num_list.index(max_num)
del num_list[index_min]
num_list.insert(index_min, max_num)
del num_list[index_max]
num_list.insert(index_max, min_num)
print(*num_list)
