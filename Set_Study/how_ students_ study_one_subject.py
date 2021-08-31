# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику,
# либо информатику, либо оба этих предмета. У руководителя школы есть списки учеников,
# изучающих каждый предмет. Случайно списки всех учеников перемешались.
#
# Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.
#
# Формат входных данных
# На вход программе в первых двух строках подаются числа
# m и n – количества учеников, изучающих математику и информатику соответственно.
# Далее идут m+nm+n строк — фамилии учеников, изучающих математику и информатику, в произвольном порядке.
#
# Формат выходных данных
# Программа должна вывести количество учеников, которые изучают только один предмет.
# Если таких учеников не окажется, то необходимо вывести NO.
#
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

matan, inform = int(input()), int(input())
sp1 = []
sp2 = []

for i in range(matan+inform):
    fio = input()
    if fio in sp1:
        sp2.append(fio)
    else:
        sp1.append(fio)

sp = abs(len(sp1) - len(sp2))

if sp == 0:
    print('NO')
else:
    print(sp)