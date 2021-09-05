# Напишите функцию convert_to_python_case(text),
# которая принимает в качестве аргумента строку в «верблюжьем регистре»
# и преобразует его в «змеиный регистр».

import string


# объявление функции
def to_snake_case(value, delimiter='_'):
    value = value[0].lower() + value[1:]
    for x in string.ascii_uppercase:
        value = value.replace(x, delimiter + x.lower())
    return value


# считываем данные
txt = input()

# вызываем функцию
print(to_snake_case(txt))
