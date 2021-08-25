n = int(input())
matrix = []
top, right, left, bottom = [], [], [], []

for rows in range(n):
    temp.extend([int(i) for i in input().split()])
    matrix.append(temp)
    temp = []

for i in range(n):
    for j in range(n):
        if j == i and i + j + 1 == n:
            continue
        if i > j and i < n - 1 - j:
            left.append(matrix[i][j])
        if i < j and i > n - 1 - j:
            right.append(matrix[i][j])
        if i > j and i > n - 1 - j:
            bottom.append(matrix[i][j])
        if i < j and i < n - 1 - j:
            top.append(matrix[i][j])

print(f"Верхняя четверть: {sum(top)}\n"
      f"Правая четверть: {sum(right)}\n"
      f"Нижняя четверть: {sum(bottom)}\n"
      f"Левая четверть: {sum(left)}"
      )
