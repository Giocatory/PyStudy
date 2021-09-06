import turtle

size = int(input())  # Размер головы (радиус большого круга)
pensize = size * 0.1  # Размер пера
turtle.Screen().setup(600, 1000)
turtle.hideturtle()
turtle.pensize(pensize)
turtle.speed(0)

parts = {1: {"pos": (0, 0), "size": size,  # Голова
             "circle": True, "color": "brown"},
         2: {"pos": (0, 0), "size": size * 0.6,  # Нос
             "circle": True, "color": "orange"},
         3: {"pos": (0, size * 0.3), "size": size * 0.3,  # Ноздри
             "circle": False, "color": "gray"},
         4: {"pos": (0, size * 0.6), "size": size * 0.1,  # Кончик
             "circle": True, "color": "yellow"},  # носа
         5: {"pos": (size * -0.5, size * 1.2), "size": size * 0.1,  # Левый
             "circle": True, "color": "black"},  # глаз
         6: {"pos": (size * 0.5, size * 1.2), "size": size * 0.1,  # Правый
             "circle": True, "color": "black"},  # глаз
         7: {"pos": (size * -0.85, size * 1.8), "size": size * 0.3,  # Левое
             "circle": True, "color": "red"},  # ухо
         8: {"pos": (size * 0.85, size * 1.8), "size": size * 0.3,  # Правое
             "circle": True, "color": "red"}}  # ухо


def bear(pos, size, circle, color):
    turtle.penup()
    turtle.goto(pos)
    turtle.pencolor(color)
    turtle.pendown()
    if circle:
        turtle.setheading(0)
        ycor = pos[1]
        while (size > 0):
            turtle.circle(size)
            size -= pensize - 1
            ycor += pensize - 1
            turtle.goto(pos[0], ycor)
    else:
        turtle.setheading(90)
        turtle.forward(size)


for i in range(1, 9):
    bear(parts[i]["pos"], parts[i]["size"], parts[i]["circle"], parts[i]["color"])

input()