# На вход программе подается одно число n.
# Напишите программу, которая выводит список,
# состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
#
# Формат входных данных
# На вход программе подается натуральное число n, n≤26.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

num = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
new_list = []
if num == 1:
    new_list.append(alphabet[0])
    print(new_list)
else:
    for i in range(0, num):
        new_list.append(alphabet[i])
    print(new_list)
