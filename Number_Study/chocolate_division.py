# Шоколадка имеет вид прямоугольника,
# разделенного на n×m долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки часть,
# состоящую ровно из k долек.
# Программа получает на вход три числа:
# n, m, k и должна вывести YES или NO.
import emoji

line = int(input())
column = int(input())
segment = int(input())
if segment < line * column and ((segment % line == 0) or (segment % column == 0)):
    print(emoji.emojize('YES :candy:'))
else:
    print(emoji.emojize('NO :confused_face:'))
