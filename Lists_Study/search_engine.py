# На вход программе подается натуральное число n,
# затем n строк,
# затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
#
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречается поисковый запрос.
#
# Примечание. Поиск не должен быть чувствителен к регистру символов.
# # Sample Input:
# # 5
# Язык Python прекрасен
# C# - отличный язык программирования
# Stepic - отличная платформа
# BEEGEEK FOREVER!
# язык Python появился 20 февраля 1991
# язык
#
# Sample Output:
# Язык Python прекрасен
# C# - отличный язык программирования
# язык Python появился 20 февраля 1991

n = int(input())
texts_list = []
for i in range(n):
    texts_list.append(input())
search_word = input()
for wd in texts_list:
    if search_word.lower() in wd.lower():
        print(wd)
