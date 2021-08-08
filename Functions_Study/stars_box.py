# объявление функции
def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            print('*'*10)
        else:
            print('*'+' '*8 + '*')


# основная программа
draw_box()  # вызов функции
