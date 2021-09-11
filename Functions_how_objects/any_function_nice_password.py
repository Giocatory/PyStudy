# Хороший пароль по условиям этой задачи состоит как минимум из 7 символов,
# содержит хотя бы одну цифру, заглавную и строчную букву.
# Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.
import string

#1
password = input()
low_let = [i for i in password if i.islower()]
upp_let = [i for i in password if i.isupper()]
dig_nums = [i for i in password if i in string.digits]
print('YES' if len(low_let)>0 and len(upp_let)>0 and len(dig_nums)>0 else 'NO')

#2
s = list(input())
f = all([any(map(lambda c: c in string.ascii_uppercase, s)),
         any(map(lambda c: c in string.ascii_lowercase, s)),
         any(map(lambda c: c in string.digits, s)),
         len(s) >= 7
         ])
print("YES" if f else "NO")