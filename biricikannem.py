import turtle
import time

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

def ağız():
    t.pencolor("black")
    t.right(315)
    t.circle(30,180)
    t.left(90)
    t.forward(53)

def dil():
    t.pencolor("red")
    t.forward(25)
    t.right(135)
    t.forward(10)
    t.right(40)
    t.forward(10)
    t.right(40)
    t.forward(10)

def ggözler():
    t.pensize(5)
    t.pencolor("black")
    for i in range(7):
        t.forward(4)
        t.left(9)

def gülücük():
    for i in range(6):
        t.forward(11)
        t.left(9)

def huge():
    t.pencolor("red")
    t.begin_fill()
    t.fillcolor("red")
    t.forward(143.5)
    t.circle(50,200)
    t.left(215)
    t.circle(50,200)
    t.forward(143.5)
    t.end_fill()

def yarabandı():
    t.color("#FFD39B")
    t.forward(50)
    for i in range(10):
        t.forward(4)
        t.right(20)
    t.left(20)
    t.forward(50)
    for i in range(10):
        t.forward(4)
        t.right(20)

def kırık():
    t.penup()
    t.right(200)
    t.goto(-250, -50)
    t.pendown()
    t.pencolor("#8B2323")
    t.begin_fill()
    t.fillcolor("#8B2323")
    s.bgcolor("black")
    t.left(255)
    t.forward(25)
    t.left(105)
    t.forward(12)
    t.right(120)
    t.forward(45)
    t.right(160)
    t.forward(25)
    t.left(95)
    t.forward(12)
    t.right(100)
    t.forward(37)
    t.right(75)
    t.forward(15)
    t.end_fill()

#kalp
t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.setup(1000,600)
s.title("ANNELER GÜNÜ")
t.hideturtle()

t.goto(0,-75)
t.pensize(3)
t.speed(10)
t.color("red")
t.begin_fill()
t.left(140)
t.forward(175)
t.circle(-90,200)
t.setheading(59)
t.circle(-90,200)
t.forward(175)
t.end_fill()

#sağdakiyüz
t.penup()
t.goto(225,225)
t.pendown()
t.pencolor("yellow")
t.begin_fill()
t.fillcolor("yellow")
t.circle(65,360)
t.end_fill()

#kalpgözler
t.penup()
t.goto(235,190)
t.pendown()
mini()
t.penup()
t.goto(285,190)
t.pendown()
mini()

#ağız
t.penup()
t.goto(235,170)
t.pendown()
t.begin_fill()
t.fillcolor("black")
ağız()
t.end_fill()

#dil
t.penup()
t.goto(275,150)
t.pendown()
t.begin_fill()
t.fillcolor("red")
dil()
t.end_fill()

#soldakiyüz
t.penup()
t.goto(-275,240)
t.pendown()
t.right(135)
t.pencolor("yellow")
t.begin_fill()
t.fillcolor("yellow")
t.circle(65,360)
t.end_fill()

#kalpler
t.penup()
t.goto(-225,210)
t.left(35)
t.pendown()
mini()
t.penup()
t.goto(-320,200)
t.pendown()
mini()
t.penup()
t.goto(-215,125)
t.pendown()
mini()

#gülengözler
t.penup()
t.goto(-280,200)
t.right(75)
t.pendown()
ggözler()
t.penup()
t.goto(-230,197)
t.right(75)
t.pendown()
ggözler()
t.forward(2)

#gülücük
t.penup()
t.goto(-300,155)
t.right(230)
t.pendown()
gülücük()

#yarabantlı kalp
t.penup()
t.goto(-200,-245)
t.pendown()
t.left(18)
huge()
t.penup()
t.goto(-225,-100)
t.pendown()
t.right(90)

#kırık
t.right(10)
t.speed(5)
kırık()
time.sleep(1)

t.penup()
t.speed(5)
t.goto(-280,-85)
t.pendown()
t.left(20)
t.begin_fill()
t.fillcolor("#FFD39B")
yarabandı()
t.end_fill()

t.penup()
t.right(135)
t.goto(-243,-108)
t.pendown()
t.right(90)
yarabandı()

t.penup()
t.goto(-190,-90)
t.pendown()
t.pencolor("white")
t.write("ANNELER",font=("Verdana",13,"bold"))
t.penup()
t.goto(-210,-120)
t.pendown()
t.write("İYİLEŞTİRİR",font=("Verdana",12,"bold"))

t.penup()
t.goto(200,-245)
t.speed(10)
t.right(70)
t.pendown()

#Ozlu soz
t.penup()
t.goto(80,-100)
t.pendown()
t.color('white')
t.write("GÖZ YAŞLARIMI DİNDİREN",font=("Verdana",15,"bold"))
time.sleep(2)

t.penup()
t.goto(80,-130)
t.pendown()
t.color('white')
t.write("BENİ HAYATA GETİREN",font=("Verdana",15,"bold"))
time.sleep(2)

t.penup()
t.goto(80,-160)
t.pendown()
t.color('white')
t.write("VE HAYATA BAĞLAYAN",font=("Verdana",15,"bold"))
time.sleep(2)

t.penup()
t.goto(80,-190)
t.pendown()
t.color('white')
t.write("CANIM ANNEM",font=("Verdana",15,"bold"))
time.sleep(2)

t.penup()
t.goto(80,-220)
t.pendown()
t.color('white')
t.write("ANNELER GÜNÜN",font=("Verdana",15,"bold"))
time.sleep(2)

t.penup()
t.goto(80,-250)
t.pendown()
t.color('white')
t.write("KUTLU OLSUN",font=("Verdana",15,"bold"))
time.sleep(2)

#kalbin içindeki yazı
t.penup()
t.goto(-100,95)
t.pendown()
t.color('white')
t.write("İYİKİ VARSIN",font=("Verdana",20,"bold"))
t.penup()
t.goto(-85,50)
t.pendown()
t.write("ANNECİĞİM",font=("Verdana",20,"bold"))

turtle.done()