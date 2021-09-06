import turtle
from random import randrange

def move_turtles(turtles, dist, angle):
    for turtle in turtles:    # все черепашки из списка делают одни и те же действия
        turtle.forward(dist)
        turtle.right(angle)


turtles = []                   # список черепашек
head = 0
num_turtles = 10               # количество череашек
for i in range(num_turtles):
    turt = turtle.Turtle()     # создаем черепашку и устанавливаем ее свойства
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(5)
    turt.tracer(25, 0)
    turtles.append(turt)       # добавляем черепашку в список
    head = head + 360/num_turtles

for i in range(70):
    move_turtles(turtles, 10, i)
input()