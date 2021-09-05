# На вход программе подается строка текста,
# содержащая целые числа.
# Напишите программу, использующую списочное выражение,
# которая выведет квадраты четных чисел, которые не оканчиваются на цифру 44.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Программу можно написать в одну строку кода.
# # Sample Input 1:
# # 1 2 3 4 5 6 7 8 9
# Sample Output 1:
# 16 36

n = [int(i)**2 for i in input().split() if int(i)**2 % 10 != 4 and int(i) % 2 == 0]
print(*n)
