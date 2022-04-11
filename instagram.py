import turtle

def köşe():
    for i in range(30):
        t.right(3)
        t.forward(3)

t = turtle.Turtle()
s = turtle.Screen()

s.bgpic("ins.gif")
t.hideturtle()
t.color("white")
t.penup()
t.goto(0,-135)
t.speed(3)
t.pendown()
t.pensize(20)
t.circle(125,360)
t.penup()
t.goto(-200,225)
t.pendown()
t.forward(400)
köşe()
t.forward(350)
köşe()
t.forward(400)
köşe()
t.forward(350)
köşe()
t.penup()
t.goto(175,125)
t.pendown()
t.begin_fill()
t.fillcolor("white")
t.pensize(10)
t.circle(30)
t.end_fill()
turtle.done()


def mini():
    t.color("red")
    t.begin_fill()
    t.fillcolor("red")
    t.right(90)
    t.forward(22)
    for i in range(9):
        t.right(20)
        t.forward(3)
    t.forward(3)
    t.right(225)
    for i in range(9):
        t.right(20)
        t.forward(3)
    t.right(42)
    t.forward(27)
    t.end_fill()