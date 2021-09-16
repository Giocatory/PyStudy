# Вам доступен текстовый файл nums.txt.
# В файле записано два целых числа, они могут быть разделены символами пробела и конца строки.
# Напишите программу, выводящую на экран сумму этих чисел.
file = open('txt_files/nums.txt')
text_in_file = list(map(int, list(filter(lambda x: x != '', [line.strip() for line in file]))))
print(sum(text_in_file))
file.close()
