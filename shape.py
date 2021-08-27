import turtle as t
import math

def star(d,color):
    t.pendown()
    t.pensize(2)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(d)
        t.left(72)
        t.forward(d)
        t.right(144)
    t.end_fill()
    t.penup()
    t.home()

def rectangle(x,y,color):
    t.pendown()
    t.pensize(2)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            t.forward(x)
        else:
            t.forward(y)
        t.left(90)
    t.end_fill()
    t.penup()
    t.home()

def triangle(x,y,color):
    t.pendown()
    t.pensize(2)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(x)
    deg = math.acos(x/(2*y)) * 180 / math.pi
    t.left(180-deg)
    t.forward(y)
    t.left(2*deg)
    t.forward(y)
    t.end_fill()
    t.penup()
    t.home()

def circle(r,color):
    t.pendown()
    t.pensize(2)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()
    t.home()