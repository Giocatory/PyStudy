# На вход программе подается одно слово, записанное в нижнем регистре.
# Напишите программу, которая определяет является ли оно палиндромом.
#
# Формат входных данных
# На вход программе подается одно слово в нижнем регистре.
#
# Формат выходных данных
# Программа должна вывести «YES», если слово является палиндромом и «NO» в противном случае.
#
# Примечание. Палиндром читается одинаково в обоих направлениях, например слово «потоп».


def wal(s):
    if len(s) % 2 == 0:
        return True
    else:
        return False


def palindrome(s):
    if wal(s):
        n = len(s) // 2
        if s[0:n] == s[-1:-n - 1:-1]:
            print('palindrome')
        else:
            print('not palindrome')
    else:
        n = len(s) // 2
        if s[0:n + 1] == s[-1:-n - 2:-1]:
            print('palindrome')
        else:
            print('not palindrome')


palindrome(input('write word: '))
