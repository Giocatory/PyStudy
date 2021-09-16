# Вам доступен текстовый файл lines.txt, в котором записаны строки текста.
# Напишите программу, которая выводит все строки наибольшей длины из файла,
# не меняя их порядок.

all_text = []
with open('txt_files/lines.txt') as file:
    for line in file:
        all_text.append(line.strip())
all_text.sort(key=len, reverse=True)
print(all_text[0])
for i in range(1, len(all_text)):
    if len(all_text[i]) >= len(all_text[0]):
        print(all_text[i])
