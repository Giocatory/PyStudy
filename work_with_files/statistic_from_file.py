# Вам доступен текстовый файл file.txt, набранный латиницей.
# Напишите программу, которая выводит
# количество букв латинского алфавита, слов и строк.

import string

file = open('file.txt', 'r', encoding='UTF-8')
text = file.read()
letters = 0

for i in text:
    if i in string.ascii_letters:
        letters += 1
    if i in string.punctuation:
        text = text.replace(i, '')
    # if i in string.digits:
    #     text = text.replace(i, '')

words = len(text.strip().split())
print('Input file contains:')
print(letters, 'letters')
print(words, 'words')
file.seek(0)
print(len(file.readlines()), 'lines')
file.close()