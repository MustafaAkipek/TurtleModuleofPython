from turtle import *
import random

my_colors = ["white","yellow","pink","cyan"]
n = 45
speed(0)
bgpic("retmenler-gunu-2.gif")


def one():
    return random.randint(15, 70)

def two():
    return random.randint(3,7)

def animated_works(a,b):
    penup()
    setheading(0)
    left(53)
    goto(a,b)
    pencolor("red")
    begin_fill()
    fillcolor("red")
    forward(143.5)
    circle(50,200)
    left(215)
    circle(50,200)
    forward(143.5)
    end_fill()

def soz(a,b):
    penup()
    goto(a,b)
    pendown()
    pencolor("purple")
    write("En fedakar ve kıymetli öğretmenime",font=("Verdana",30,"bold"))
    

def animated_stars(a,b):
    pensize(1)
    hideturtle()
    col1 = random.choice(my_colors)
    l = one()
    color(col1)
    penup()
    goto(a,b)
    pendown()
    begin_fill()
    for i in range(5):
        forward(l)
        right(144)
        forward(l)
    end_fill()
    
onscreenclick(animated_stars,1)
onscreenclick(soz,2)
onscreenclick(animated_works,3)

done()
