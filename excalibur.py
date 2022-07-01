import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

t.hideturtle()
t.pencolor("#03f8fc")
t.pensize(3)
s.bgcolor("black")

#frame right side
t.penup()
t.fillcolor("#03f8fc")
t.begin_fill()
t.goto(0,-110)
t.pendown()
t.left(50)
t.forward(475)
t.goto(0,254)
t.setheading(0)

#frame right side
t.penup()
t.goto(0,-110)
t.pendown()
t.left(130)
t.forward(475)
t.goto(0,254)
t.end_fill()
t.setheading(0)


#outside right side
t.penup()
t.begin_fill()
t.fillcolor("black")
t.goto(0,-110)
t.pendown()
t.pencolor("black")
t.left(65)
t.forward(280)
t.right(35)
t.forward(150)
t.setheading(0)
t.left(180)
t.goto(0,219)
t.setheading(0)

#outside left side
t.penup()
t.goto(0,-110)
t.pendown()
t.left(115)
t.forward(280)
t.left(35)
t.forward(150)
t.setheading(0)
t.goto(0,219)
t.end_fill()


#inside right side
t.penup()
t.goto(0,-110)
t.pencolor("#03f8fc")
t.pendown()
t.begin_fill()
t.fillcolor("#03f8fc")
t.left(82.5)
t.forward(250)
t.goto(0,115)
t.setheading(0)

#inside left side
t.penup()
t.goto(0,-110)
t.pendown()
t.left(97.5)
t.forward(250)
t.goto(0,115)
t.end_fill()
t.setheading(0)

logo = "EXCALIBUR"
a = -300
#Part of Bottom
for i in range(0,9):
    t.setheading(0)
    t.penup()
    t.goto(a,-225)
    t.pendown()
    t.write(logo[i],font=("Verdana",50,"bold"))
    t.penup()
    time.sleep(0.50)
    a += 75

turtle.done()