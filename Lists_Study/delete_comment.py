# #12
# print("Введите своё имя")
# name = input()
# print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
# password = input()
# if password == "hoover":
#     print("Здравствуйте, рыцарь", name)         #долой Макнамару
# elif password == "noncr":
#     print("Здравствуйте, паладин", name)
# elif password == "gelios":
#     print("Здравствуйте, старейшина", name)          #Элайджа вперёд
# else:
#     print("Здравствуйте, послушник", name)

n = input()
n = int(n[1:])
for i in range(n):
    line = input()
    if '#' not in line:
        print(line)
    else:
        find_hash = line.rfind('#')
        print(line[0:find_hash].rstrip())
