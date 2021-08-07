# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, которая по заданным числам строит столбчатую диаграмму.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.
#
# Формат выходных данных
# Программа должна вывести столбчатую диаграмму.
#
# Sample Input 1:
# 1 2 3 4 5
# Sample Output 1:
# +
# ++
# +++
# ++++
# +++++

s = input().split()
for i in s:
    for j in range(int(i)):
        print('+', end='')
    print()
