# объявление функции
def print_digit_sum(num):
    number = []
    while num != 0:
        number.append(num % 10)
        num //= 10
    print(sum(number))


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
