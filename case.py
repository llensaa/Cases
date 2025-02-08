import turtle as trt
import math as mth

trt.penup()

def triangle(x, y, l, color):
    trt.fillcolor(color)
    trt.setpos(x, y)
    trt.pendown()
    trt.begin_fill()
    trt.forward(l)
    trt.right(135)
    trt.forward(l * 0.5 * mth.sqrt(2))
    trt.right(90)
    trt.forward(l * 0.5 * mth.sqrt(2))
    trt.end_fill()
    trt.penup()
    trt.home()

def square (x, y, l, w, color):
    trt.fillcolor(color)
    trt.setpos(x,y)
    trt.pendown()
    trt.begin_fill()
    for i in range(2):
        trt.forward(l)
        trt.right(90)
        trt.forward(w)
        trt.right(90)
    trt.end_fill()
    trt.penup()
    trt.home()
    pass

def parallelogramm (x, y, l, w, color):
    trt.fillcolor(color)
    trt.setpos(x,y)
    trt.pendown()
    trt.begin_fill()
    for i in range (2):
        trt.forward(l)
        trt.right(135)
        trt.forward(w)
        trt.right(45)
    trt.end_fill()
    trt.penup()
    trt.home()
    pass

triangle(-50, 50, 100, 'red')

trt.right(90)
triangle(50, 50, 50, 'green')

trt.right(45)
square(25, 25,
       50 * 0.5 * mth.sqrt(2),
       50 * 0.5 * mth.sqrt(2),
       'purple'
       )

trt.left(45)
triangle(0, -50, 71, 'yellow')

trt.right(180)
triangle(25, -25, 50, 'orange')

trt.left(90)
triangle(-50, -50, 100, 'pink')

parallelogramm(-25, -25,50,
               50 * 0.5 * mth.sqrt(2),
               'moccasin')

trt.right(180)
triangle(-100, -10, 50, 'pink')

trt.right(90)
parallelogramm(-125, 21 + 25 * 0.5 * mth.sqrt(2),25,
               25 * 0.5 * mth.sqrt(2),
               'moccasin')

trt.right(135)
square(-125, 16,
       25 * 0.5 * mth.sqrt(2), 25 * 0.5 * mth.sqrt(2), 'purple')

trt.right(180)
triangle(-137.5, 4, 25, 'orange')

triangle(-187.5, 4, 50, 'red')

triangle(-137.5, 34 + 25 * 0.5 * mth.sqrt(2), 25, 'green')

trt.left(90)
triangle(-200, -8.5, 25, 'yellow')

trt.mainloop()
