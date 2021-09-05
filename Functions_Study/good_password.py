# Напишите функцию is_password_good(password),
# которая принимает в качестве аргумента строковое значение пароля
# и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
# 1) его длина не менее 88 символов;
# 2) он содержит как минимум одну заглавную букву (верхний регистр);
# 3) он содержит как минимум одну строчную букву (нижний регистр);
# 4) он содержит хотя бы одну цифру.

# объявление функции
def is_password_good(password):
    numbers = [i for i in range(48, 58)]
    count_nums = 0
    small_letters = [i for i in range(97, 123)]
    count_small = 0
    big_letters = [i for i in range(65, 91)]
    count_big = 0
    for i in range(len(password)):
        if ord(password[i]) in numbers:
            count_nums += 1
            break
    for i in range(len(password)):
        if ord(password[i]) in small_letters:
            count_small += 1
            break
    for i in range(len(password)):
        if ord(password[i]) in big_letters:
            count_big += 1
            break
    if count_big != 0 and count_small != 0 and count_nums != 0 and len(password) >= 8:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
