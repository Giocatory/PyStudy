# Напишите программу для определения общего количества различных слов в строке текста.

import re

words = set((re.sub(r'[.,;:-?-!]', '', input().lower())).split())

# print(words)
print(len(words))
