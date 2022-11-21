import turtle

t = turtle.Turtle()
s = turtle.Screen()

#sağ alt
t.begin_fill()
t.fillcolor("black")
s.bgcolor("#9146ff")
t.hideturtle()
t.pensize(3)
t.penup()

t.goto(-100,-200)
t.pendown()
t.left(45)
t.forward(150)

t.setheading(0)
t.forward(100)

#sağ kenar ve üst
t.left(45)
t.forward(225)
t.setheading(0)
t.left(90)
t.forward(225)
t.goto(-130,290)

#sol üst köşe
t.setheading(0)
t.left(225)
t.forward(100)

#sol kenar
t.goto(-201,-93.93)
t.setheading(0)
t.forward(101)
t.goto(-100,-200)
t.end_fill()

#iç kısım

t.begin_fill()
t.fillcolor("white")
t.pencolor("white")
t.penup()
t.goto(6.07,-50)
t.pendown()
t.left(45)
t.forward(75)


t.setheading(0)
t.forward(95)

t.left(45)
t.forward(95)

t.left(45)
t.forward(175)

t.left(90)
t.goto(-100,245)

t.goto(-100,3.03)

t.setheading(0)
t.forward(106)

t.goto(6.07,-50)
t.end_fill()

#sol göz

t.begin_fill()
t.fillcolor("black")
t.penup()
t.pencolor("black")
t.goto(10,85)
t.pendown()
t.forward(35)

t.left(90)
t.forward(115)
t.left(90)
t.forward(35)
t.left(90)
t.forward(115)
t.end_fill()

#sağ göz

t.setheading(0)
t.begin_fill()
t.fillcolor("black")
t.penup()
t.pencolor("black")
t.goto(125,85)
t.pendown()
t.forward(35)

t.left(90)
t.forward(115)
t.left(90)
t.forward(35)
t.left(90)
t.forward(115)
t.end_fill()



turtle.done()