# объявление функции
def is_palindrome(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] not in [' ', ',', '.', '!', '?', '-']:
            new_text += text[i].lower()
    if new_text == new_text[::-1]:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
