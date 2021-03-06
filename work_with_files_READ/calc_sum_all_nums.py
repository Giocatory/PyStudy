# Вам доступен текстовый файл nums1.txt.
# В файле могут быть записаны целые неотрицательные числа и все, что угодно.
# Числом назовем последовательность одной и более цифр, идущих подряд
# (число всегда неотрицательно).
#
# Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.
import re

with open('txt_files/nums1.txt') as file:
    nums = [line.strip() for line in file]
    total = []
    for i in range(len(nums)):
        nums[i] = sum(list(map(int, re.sub('\D', ' ', nums[i]).strip().split())))
    print(sum(nums))

#  123   jhjk           => 123
# bhjip456qwerty        => 456
# 1x2y3 4 5 6           => 1 2 3 4 5 6
# sfsd 0 dfgfd          => 0
# 10abc20de30pop5 5 5   => 10 20 30 5 5 5
# 123+456+1+2+3+4+5+6+0+10+20+30+5+5+5 = 675
# то результатом было бы:
# 675