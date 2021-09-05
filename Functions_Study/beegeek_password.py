# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы
# с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c,
# где a, b и c – натуральные числа.
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password),
# которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является действительным паролем
# False в противном случае.

# объявление функции
def is_valid_password(password):
    password = password.split(':')
    if len(password) > 3 or len(password) < 3:
        return False
    count = 0
    temp_count = 0
    if password[0] == password[0][::-1]:
        count += 1
    for i in range(1, int(password[1])+1):
        if int(password[1]) % i == 0:
            temp_count += 1
    if temp_count == 2:
        count += 1
    if int(password[2]) % 2 == 0:
        count += 1
    return count == 3


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))