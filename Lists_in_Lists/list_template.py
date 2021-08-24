n = int(input())  # How many rows and columns will there be?
lists = [[j for j in range(1, n+1)] for i in range(n)]
# for i in range(n):
#     new_list = []
#     for j in range(1, n+1):
#         new_list.append(j)
#     lists.append(new_list)

for rows in lists:
    print(rows)

