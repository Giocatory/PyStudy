# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
# больших среднего арифметического элементов данной строки.

n = int(input())
matrix = []
temp = []
total = 0
counter = 0

for rows in range(n):
    temp.extend([int(i) for i in input().split()])
    matrix.append(temp)
    temp = []

for rows in range(n):
    for cols in range(n):
        total += matrix[rows][cols]
    total /= n
    for cols in range(n):
        if cols > total:
            counter += 1
    print(counter)
    total = 0
    counter = 0
