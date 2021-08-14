import turtle as t
import math

def star(d):
    t.pendown()
    t.pensize(2)
    for i in range(5):
        t.forward(d)
        t.left(72)
        t.forward(d)
        t.right(144)
    t.penup()
    t.home()

def rectangle(x,y):
    t.pendown()
    t.pensize(2)
    for i in range(4):
        if i % 2 == 0:
            t.forward(x)
        else:
            t.forward(y)
        t.left(90)
    t.penup()
    t.home()

def triangle(x,y):
    t.pendown()
    t.pensize(2)
    t.forward(x)
    deg = math.acos(x/(2*y)) * 180 / math.pi
    t.left(180-deg)
    t.forward(y)
    t.left(2*deg)
    t.forward(y)
    t.penup()
    t.home()

def circle(r):
    t.pendown()
    t.pensize(2)
    t.circle(r)
    t.penup()
    t.home()