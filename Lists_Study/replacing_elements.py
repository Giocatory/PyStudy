rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
item_green = rainbow.index('Green')
item_violet = rainbow.index('Violet')

rainbow[item_green] = 'Зеленый'
rainbow[item_violet] = 'Фиолетовый'
print(rainbow)
