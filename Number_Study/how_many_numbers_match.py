# Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает)
# или 0 (если все числа различны).
one = int(input('Введите первое число: '))
two = int(input('Введите второе число: '))
three = int(input('Введите третье число: '))
if one == two == three:
    print('Все числа одинаковы')
elif one == two or one == three or two == three:
    print('2 числа одинаковы')
else:
    print('Все числа разные')
