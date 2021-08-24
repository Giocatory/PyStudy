my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = max(row)
    minimum = min(row)

print(maximum + minimum)