# Напишите функцию get_next_prime(num),
# которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num.

def get_next_prime(num):
    number = num + 1
    count = 0
    while True:
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1
        if count == 2:
            break
        else:
            count = 0
            number += 1
    return number


n = int(input())
print(get_next_prime(n))
