# Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем
# интернет-магазина.
#
# Формат входных данных На вход программе подается число nn — количество строк в базе данных о продажах
# интернет-магазина. Далее следует nn строк с записями вида покупатель товар количество, где покупатель — имя
# покупателя (строка без пробелов), товар — название товара (строка без пробелов), количество — количество
# приобретенных единиц товара (натуральное число).
#
# Формат выходных данных Программа должна вывести список всех покупателей в лексикографическом порядке, после имени
# каждого покупателя — двоеточие, затем список названий всех приобретенных им товаров в лексикографическом порядке,
# после названия каждого товара — количество единиц товара. Информация о каждом товаре выводится на отдельной строке.
#
# Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список попадает
# суммарное количество товара по данной позиции. .

data = {}

for _ in range(int(input())):
    name, product, count = input().split()
    data.setdefault(name, {})
    data[name][product] = data[name].get(product, 0) + int(count)

for person, products in sorted(data.items()):
    print(f'{person}:')
    for product, count in sorted(products.items()):
        print(product, count)
