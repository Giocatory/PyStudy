import math


# объявление функции
def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    if a != 0:
        if D < 0:
            return False, False
        elif D == 0:
            x = -b / (2 * a)
            return x, x
        else:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            if x1 > x2:
                return x2, x1
            elif x2 > x1:
                return x1, x2


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
