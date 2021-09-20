# Находим множество слов, каждое из которых состоит из букв нашего слова, но в разных регистрах
# 'wow' -> {'WOW', 'WOw', 'WoW', 'Wow', 'wOW', 'wOw', 'woW', 'wow'}
def all_words(word):
    l = [word[0], word[0].swapcase()]
    for char in word[1:]:
        l = [chars + char for chars in l] + [chars + char.swapcase() for chars in l]
    return set(l)


# По каждому слову из (запрещенного) списка слово в тексте запикиваем звездочками,
# если оно в множестве полученных из запрещенного
def replace_all(text, lst):
    for word in lst:
        for comb in all_words(word):
            text = text.replace(comb, '*' * len(word))
    return text


# Читаем список запрещенных слов
with open('forbidden_words.txt', 'r', encoding='utf-8') as f:
    fs = [l.strip().split() for l in f.readlines()][0]

# Читаем текст и заменяем запрещенные слова
with open(input(), 'r', encoding='utf-8') as f:
    print(replace_all(f.read(), fs))