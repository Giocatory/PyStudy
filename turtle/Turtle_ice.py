import turtle, random

# Глобальные переменные ------------------------------------------------------------
SCREEN_SIZE = 400  # Размер квадратного холста
ACCESS_X = set(range(-SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 1))  # Доступные точки
ACCESS_Y = set(range(-SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 1))  # по "x" и "y"
# ----------------------------------------------------------------------------------

# Общие настройки черепашки --------------------------------------------------------
turtle.Screen().setup(SCREEN_SIZE, SCREEN_SIZE)  # Размер холста
turtle.Screen().bgcolor("cyan")  # Цвет холста
turtle.pencolor("blue")  # Цвет пера
turtle.speed(0)  # Скорость анимации черепашки
turtle.hideturtle()  # Видимость черепашки выключена


# ----------------------------------------------------------------------------------

# Функция для рисования случайной снежинки -----------------------------------------
def star():
    global ACCESS_X, ACCESS_Y

    max_size = 0.4  # Макс. значение интервала для выбора размера снежинки
    while (max_size >= 0.2):
        size = random.uniform(SCREEN_SIZE * 0.02, SCREEN_SIZE * max_size)
        x0 = random.choice(tuple(ACCESS_X))  # Выбор коор. "x" из доступных точек
        y0 = random.choice(tuple(ACCESS_Y))  # Выбор коор. "y" из доступных точек
        xcors = set(range(int(x0 - size / 2), int(x0 + size / 2)))  # Множества занятых
        ycors = set(range(int(y0 - size / 2), int(y0 + size / 2)))  # точек "x" и "y"

        # Если область свободна, приступаем к рисованию
        if (len(xcors - ACCESS_X) == 0 and len(ycors - ACCESS_Y) == 0):
            turtle.penup()
            turtle.goto(x0, y0)  # Центр снежинки с выбранными выше координатами
            turtle.pendown()

            quarter = size / 2 / 4  # Четвертая часть луча снежинки
            for _ in range(8):  # Цикл для рисования восьми лучей
                for _ in range(4):  # Цикл для рисования четырех веточек на данном луче
                    turtle.left(30)
                    turtle.forward(quarter)
                    turtle.backward(quarter)
                    turtle.right(60)
                    turtle.forward(quarter)
                    turtle.backward(quarter)
                    turtle.left(30)
                    turtle.forward(quarter)
                turtle.backward(size / 2)
                turtle.left(45)

            ACCESS_X -= xcors  # Занятые снежинкой точки
            ACCESS_Y -= ycors  # убираем из доступных
            print(len(ACCESS_X), len(ACCESS_Y))  # Кол-во доступных точек
            break
        else:  # Если область занята, то уменьшаем макс. значение
            max_size -= 0.1  # интервала для выбора размера снежинки


# ----------------------------------------------------------------------------------

# Вызов функции до тех пор, пока есть доступные точки ------------------------------
while (len(ACCESS_X) > SCREEN_SIZE * 0.2 and
       len(ACCESS_Y) > SCREEN_SIZE * 0.2):
    star()
# ----------------------------------------------------------------------------------

print("DONE!")
input()