# Напишите функцию is_correct_bracket(text),
# которая принимает в качестве аргумента непустую строку text,
# состоящую из символов ( и )
# и возвращает значение True если
# поступившая на вход строка является правильной скобочной последовательностью
# и False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка,
# состоящая только из символов ( и ),
# где каждой открывающей скобке найдется парная закрывающая скобка

# объявление функции
def is_correct_bracket(text):
    sp = []
    flag = False
    for i in range(len(text)):
        if text[i] == '(':
            sp.append(text[i])
        elif text[i] == ')' and len(sp) == 0:
            flag = True
            break
        elif text[i] == ')' and sp[-1] == '(':
            del sp[-1]
    if len(sp) == 0 and not flag:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))