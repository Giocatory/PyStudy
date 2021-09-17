# Вам доступен текстовый файл logfile.txt с информацией о времени
# входа пользователя в систему и выхода из нее.
# Каждая строка файла содержит три значения, разделенные запятыми
# и символом пробела:
# имя пользователя, время входа, время выхода,
# где время указано в 24-часовом формате.
#
# Напишите программу, которая создает файл output.txt и выводит в него
# имена всех пользователей (не меняя порядка следования),
# которые были в сети не менее часа.
from datetime import datetime, timedelta

with open('txt_files/logfile.txt') as log, open('txt_files/output.txt', 'w') as logout:
    full_log =  [line.strip().split(', ') for line in log]
    log_in = timedelta(hours=1)
    for i in full_log:
        signin = timedelta(hours=int(i[1][0:2]), minutes=int(i[1][3:]))
        signout = timedelta(hours=int(i[2][0:2]), minutes=int(i[2][3:]))
        if signout - signin >= log_in:
            print(i[0], file=logout)

# a = timedelta(hours=14, minutes=10)
# b = timedelta(hours=15, minutes=50)