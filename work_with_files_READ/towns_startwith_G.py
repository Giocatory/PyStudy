# Вам доступен текстовый файл population.txt
# с названиями стран и численностью их населения, разделенными символом табуляции '\t'.
#
# Напишите программу выводящую все страны,
# название которых начинается с буквы 'G',
# численность населения которых больше чем 500000 человек, не меняя их порядок.

with open('txt_files/population.txt') as file:
    all_info = [line.strip().split('\t') for line in file]
    g_towns = [town for town in all_info if town[0][0] == 'G' and int(town[1]) > 500_000]
    for i in g_towns:
        print(i[0])
