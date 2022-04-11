import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.hideturtle()
s.bgcolor("red")
t.pensize(5)
t.speed(5)
t.color("white")
t.begin_fill()
t.fillcolor("white")

#sağ yüz
t.penup()
t.goto(0,-100)
t.pendown()
t.left(80)
t.forward(225)
t.right(80)
t.forward(60)
for i in range(10):
    t.right(7)
    t.forward(4)
t.left(90)

for i in range(8):
    t.left(5)
    t.forward(8)

t.left(90)
t.forward(10)

for i in range(5):
    t.left(3)
    t.forward(5)

for i in range(7):
    t.left(1.5)
    t.forward(8)

for i in range(5):
    t.left(1)
    t.forward(11)
t.goto(0,115)


#sol yüz
t.penup()
t.goto(0,-100)
t.pendown()
t.right(80)
t.forward(225)
t.left(83)
t.forward(60)
for i in range(10):
    t.left(7)
    t.forward(4)
t.right(90)

for i in range(8):
    t.right(5)
    t.forward(8)

t.right(90)
t.forward(10)

for i in range(5):
    t.right(3)
    t.forward(5)

for i in range(7):
    t.right(1.5)
    t.forward(8)

for i in range(5):
    t.right(1)
    t.forward(11)
t.goto(0,115)
t.end_fill()

#üst kısım
t.penup()
t.goto(-190,160)
t.pendown()
t.left(20)
t.begin_fill()
t.fillcolor("white")

#ilk vurgu
for i in range(7):
    t.forward(10)
    t.right(2)

#ikinci vurgu
for i in range(7):
    t.forward(10)
    t.right(1)

#düzlük
for i in range(5):
    t.forward(10)
    t.left(0.2)

#düzlük
for i in range(5):
    t.forward(10)
    t.right(1)

#üçüncü vurgu
for i in range(5):
    t.forward(10)
    t.right(0.5)

#dördüncü vurgu
for i in range(5):
    t.forward(10)
    t.right(1.5)

#beşinci vurgu
for i in range(5):
    t.forward(8)
    t.right(2)

#üst çıkış kısmı
t.setheading(0)
t.penup()
t.left(75)
t.pendown()
t.forward(15)
t.left(85)
t.forward(20)

#üst taban sağ taraf ilk vurgu
for i in range(7):
    t.forward(7)
    t.left(2)

for i in range(7):
    t.forward(10)
    t.left(0.5)

#en tepe
for i in range(7):
    t.forward(7)
    t.left(0.5)

#tepeden iniş
for i in range(7):
    t.forward(7)
    t.left(0.5)

#daha kavisli iniş
for i in range(7):
    t.forward(7)
    t.left(0.7)

#son düzlük
for i in range(7):
    t.forward(8)

t.left(5)

#en son düzlük
for i in range(7):
    t.left(2.5)
    t.forward(7.5)

t.left(85)
t.forward(14)
t.end_fill()

#harf kısımları
t.setheading(0)
t.penup()
t.goto(-170,-190)
t.pendown()
t.write("T",font=("Verdana",50,"bold"))
t.penup()

t.setheading(0)
t.penup()
t.goto(-95,-190)
t.pendown()
t.write("E",font=("Verdana",50,"bold"))
t.penup()

t.setheading(0)
t.penup()
t.goto(-20,-190)
t.pendown()
t.write("S",font=("Verdana",50,"bold"))
t.penup()

t.setheading(0)
t.penup()
t.goto(55,-190)
t.pendown()
t.write("L",font=("Verdana",50,"bold"))
t.penup()

t.setheading(0)
t.penup()
t.goto(130,-190)
t.pendown()
t.write("A",font=("Verdana",50,"bold"))
t.penup()

turtle.done()