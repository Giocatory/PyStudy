# На вход программе подается натуральное число
# n≥2, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список,
# состоящий из сумм соседних чисел (00 и 11, 11 и 22, 22 и 33 и т.д.).
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из сумм соседних чисел.

n = int(input())
l = []
nl = []
for i in range(n):
    l.append(int(input()))
for i in range(1, len(l)):
    nl.append(l[i]+l[i-1])
print(nl)