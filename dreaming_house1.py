import turtle as t
import math
import random
import shape
import color

# Hệ số tỷ lệ
k = 5
t.speed(10)

# toạ độ ban đầu
x0 = 0
y0 = -250

# Vẽ đường mặt đất
x = 250
t.penup()
t.pensize(5)
t.goto(-k*x/2 + x0,0 + y0)
t.pendown()
t.forward(k*x)
t.penup()
t.home()

# vẽ mặt trước ngôi nhà
t.goto(0+x0, 0+y0)
x = 100
y = 70
shape.rectangle(k*x, k*y,color.get_color())

# vẽ mái nhà
x1 = 123
y1 = 80
t.goto(-k*(x1-x)/2+x0, k*y+y0)
shape.triangle(k*x1, k*y1,color.get_color())

# vẽ cửa chính
x2 = 23
y2 = 50
t.goto(k*(x-x2)/2+x0, 0+y0)
shape.rectangle(k*x2,k*y2,color.get_color())

# vẽ tay nắm cửa
r = 1
t.goto(k*0.57*x+x0,k*(y2-r)/2+y0)
shape.circle(k*r,color.get_color())

# vẽ cửa số trái
r1 = 12
t.goto(k*0.22*x+x0,k*28/70*y+y0)
shape.circle(k*r1,color.get_color())

#vẽ cửa sổ phải
x3 = 23
y3 = 23
t.goto(k*0.7*x+x0,k*32/70*y+y0)
shape.triangle(k*x3,k*y3,color.get_color())
#vẽ ống khói
x4 = 17
y41 = 29
y42 = 14
t.goto(k*0.87*x+x0,k*90/70*y+y0)
t.left(90)
t.pendown()
t.fillcolor(color.get_color())
t.begin_fill()
t.forward(k*y41)
t.left(90)
t.forward(k*x4)
t.left(90)
t.forward(k*y42)
t.end_fill()
t.penup()
t.home()

# vẽ thân cây
x5 = 17
y5 = 45
t.goto(-k*68 + x0, 0 + y0)
shape.rectangle(k*x5,k*y5,color.get_color())

#vẽ tán cây
t.goto(-k*(68-x5/2)+x0,k*y5+y0)
t.pendown()
t.fillcolor(color.get_color())
t.begin_fill()
t.forward(k*40)
t.left(180-26.29)
t.forward(k*29)
t.right(180-26.29)
t.forward(k*17)
t.left(180-33.56)
t.forward(k*24)
t.right(180-33.56)
t.forward(k*9)
t.left(180-55.15)
t.forward(k*35)
t.penup()
t.goto(-k*(68-x5/2)+x0,k*y5+y0)
t.left(55.15)
t.pendown()
t.forward(k*40)
t.right(180-26.29)
t.forward(k*29)
t.left(180-26.29)
t.forward(k*17)
t.right(180-33.56)
t.forward(k*24)
t.left(180-33.56)
t.forward(k*9)
t.right(180-55.15)
t.forward(k*35)
t.end_fill()
t.penup()
t.home()

# vẽ mặt trăng
t.goto(-k*70+x0,k*125+y0)
t.pendown()
t.fillcolor(color.get_color())
t.begin_fill()
t.left(90)
t.circle(k*17,270)
t.end_fill()
t.penup()
t.goto(-k*70+x0,k*125+y0)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.left(135)
t.circle(k*17*math.sqrt(2)/2,180)
t.end_fill()
t.penup()
t.home()

# vẽ ngôi sao
min_x = -k*50 + x0
min_y = k*130 + y0
max_y = k*160 + y0
for i in range(18):
    t.goto(min_x + k*10*i,random.randint(min_y, max_y))
    t.pendown()
    shape.star(k*random.randint(2, 3),color.get_color())
    t.penup()
    t.home()

t.hideturtle()
t.done()