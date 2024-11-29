import turtle
import math

t = turtle.Turtle()
t.speed(3)
t.color("red")
turtle.bgcolor("black")

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

for i in range(15):
    x, y = corazon(i)
    t.goto(x, y)
    t.pendown()
    for n in range(8, 100, 2):
        x, y = corazon(n/10)
        t.goto(x, y)
    t.penup()

t.penup()
t.hideturtle()
turtle.done()


