# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая определяет количество чисел,
# которые есть как в первой строке, так и во второй.

set_nums_one = set([int(i) for i in input().split()])
set_nums_two = set([int(i) for i in input().split()])
print(len(set_nums_one.intersection(set_nums_two)))

# Sample Input 1:
#
# 1 3 2
# 4 3 2
# Sample Output 1:
#
# 2
