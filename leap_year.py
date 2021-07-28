# Дано натуральное число.
# Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES,
# иначе выведите NO.
# Год является високосным, если
# его номер кратен 4, но не кратен 100,
# а также если он кратен 400.

leap_year = int(input("Введите год: "))

if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    print('Високосный год')
else:
    print('Простой год')
