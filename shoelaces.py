# Обувная фабрика собирается начать выпуск элитной модели ботинок.
# Дырочки для шнуровки будут расположены в два ряда,
# расстояние между рядами равно a,
# расстояние между дырочками в ряду b.
# Количество дырочек в каждом ряду равно N.
# Шнуровка должна происходить элитным способом “наверх,
# по горизонтали в другой ряд, наверх, по горизонтали и т.д.”.
# Кроме того, чтобы шнурки можно было завязать элитным бантиком,
# длина свободного конца шнурка должна быть l.
# Какова должна быть длина шнурка для этих ботинок?

# Программа получает на вход четыре натуральных числа a, b, l и N
# — именно в таком порядке
# — и должна вывести одно число
# — искомую длину шнурка.

distance_in_a_row = int(input('Расстояние между рядами: '))
distance_between_holes = int(input('Расстояние между дырочками в ряду: '))
length_of_the_free_end_of_the_lace = int(input('Длина свободного конца шнурка: '))
Number_of_holes = int(input('Количество дырочек в каждом ряду: '))
lace_length_for_these_shoes = (2 * length_of_the_free_end_of_the_lace
                               + (2 * Number_of_holes - 1) * distance_in_a_row
                               + 2 * (Number_of_holes - 1) * distance_between_holes)
print(f"Длина шнурка для этих ботинок: {lace_length_for_these_shoes}")
