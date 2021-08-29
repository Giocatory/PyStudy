# На вход программе подается строка текста, содержащая числа.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO,
# если не встречалось.

numbers = [int(i) for i in input().split()]
set_nums = set()

for i in numbers:
    if i in set_nums:
        print('YES')
    else:
        print('NO')
    set_nums.add(i)
