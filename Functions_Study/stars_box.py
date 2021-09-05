# объявление функции
def draw_box(col, rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print('*' * col)
        else:
            print('*' + ' ' * (col - 2) + '*')


# основная программа
draw_box(5, 5)  # вызов функции
