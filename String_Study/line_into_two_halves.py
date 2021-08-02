# На вход программе подается строка текста. Напишите программу,
# которая разрежет ее на две равные части, переставит их местами и выведет на экран.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание.
# Если длина строки нечетная,
# то длина первой части должна быть на один символ больше.

s = input()
if len(s) == 1:
    print(s)
elif len(s) == 2:
    print(s[1] + s[0])
elif len(s) % 2 == 0 and len(s) != 2:
    n = len(s) // 2
    print(s[n:] + s[0:n])
else:
    n = len(s) // 2
    print(s[-n:] + s[0:n + 1])