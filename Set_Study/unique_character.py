# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
#
# Формат входных данных
# На вход программе в первой строке подается число nn – общее количество слов. Далее идут nn строк с словами.
#
# Формат выходных данных
# Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.

n = int(input())
texts = []
unique = []
for i in range(n):
    texts.append(input().lower())
for i in texts:
    unique.append(len(set(i)))
print(*unique, sep='\n')

############ OR ################

# print(*[len(set(input().lower())) for i in range(int(input()))], sep='\n')