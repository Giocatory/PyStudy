import random

with open('txt_files/first_names.txt') as f_name, open('txt_files/last_names.txt') as l_name:
    f_names = [line.strip() for line in f_name if line != '']
    l_names = [line.strip() for line in l_name if line != '']
    for _ in range(3):
        name = random.choice(f_names)
        lastName = random.choice(l_names)
        print(name, lastName)
