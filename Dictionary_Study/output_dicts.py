capitals = {'Россия': 'Москва',
            'Франция': 'Париж',
            'Чехия': 'Прага'}

for keys, values in capitals.items():
    print(f"{keys} - {values}")

print()

for key in capitals:
    print(key + ' - ' + capitals[key])

print()

capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}

for key in capitals.keys():
    print(key)

print()

capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}

for value in capitals.values():
    print(value)
