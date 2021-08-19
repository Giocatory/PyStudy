animals = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц',
           'Дракон', 'Змея', 'Лошадь', 'Овца']

year = int(input())
animals_year = year % 12
while animals_year >= 12:
    animals_year -= 12
print(animals[animals_year])
