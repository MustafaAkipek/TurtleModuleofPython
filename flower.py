import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
time.sleep(1.5)
s.bgcolor("black")
t.hideturtle()
t.speed(0)
colors = ["red","pink","purple","blue","cyan","green"]
def flower():
    for i in range(440):
        t.color(colors[i%6])
        t.circle(190-i,90)
        t.left(90)
        t.circle(190-i,90)
        t.left(18)

flower()
turtle.done()