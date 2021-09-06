import turtle
from random import randrange

def random_color():
  return randrange(256), randrange(256), randrange(256)

def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    color = random_color()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.speed(0)

def left_mouse_click(x, y):
    draw_circle(x, y, 10)

turtle.hideturtle()

turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()
input()