n = int(input())  # How many rows and columns will there be?
# lists = [[j for j in range(i)] for i in range(1, n+1)]
lists = []
for i in range(n):
    new_list = []
    for j in range(i):
        new_list.append(j)
    lists.append(new_list)

for rows in lists:
    print(rows)

