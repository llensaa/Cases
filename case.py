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
               'moccasin'
               )

trt.right(180)
triangle(-100, -10, 50, 'pink')

trt.right(90)
parallelogramm(-125, 21 + 25 * 0.5 * mth.sqrt(2),25,
               25 * 0.5 * mth.sqrt(2),
               'moccasin'
               )

trt.right(135)
square(-125, 16,
       25 * 0.5 * mth.sqrt(2),
       25 * 0.5 * mth.sqrt(2),
       'purple'
       )

trt.right(180)
triangle(-137.5, 4, 25, 'orange')

triangle(-187.5, 4, 50, 'red')

triangle(-137.5, 34 + 25 * 0.5 * mth.sqrt(2),
         25, 'green'
         )

trt.left(90)
triangle(-205, -15, 37.5, 'yellow')

trt.left(135)
triangle(-90, -80, 37.5, 'yellow')

trt.right(135)
square(-86.25 - 25 * 0.5 * mth.sqrt(2),
       -82.75 + 25 * 0.5 * mth.sqrt(2),
       25 * 0.5 * mth.sqrt(2),
       25 * 0.5 * mth.sqrt(2),
       'purple'
       )

trt.right(180)
triangle(-85 - 25 * 0.5 * mth.sqrt(2),
         -73 - 25 * 0.5 * mth.sqrt(2),
         50, 'red'
         )

trt.right(135)
triangle(-110 - 25 * 0.5 * mth.sqrt(2),
         -48 - 25 * 0.5 * mth.sqrt(2),
         50, 'pink'
        )

trt.right(180)
parallelogramm(-97.5 - 25 * 0.5 * mth.sqrt(2),
               -85.5 - 25 * 0.5 * mth.sqrt(2) ,
               25, 25 * 0.5 * mth.sqrt(2),
               'moccasin'
               )

trt.right(90)
triangle(-140 - 25 * 0.5 * mth.sqrt(2),
         -78 - 25 * 0.5 * mth.sqrt(2),
         25, 'orange'
         )

trt.right(135)
triangle(-110 - 75 * 0.5 * mth.sqrt(2),
         -48 - 25 * 0.5 * mth.sqrt(2),
         25, 'green'
         )

trt.right(135)
triangle(-50,150,50, 'red')

trt.right(135)
square(-45, 130,
       25 * 0.5 * mth.sqrt(2),
       25 * 0.5 * mth.sqrt(2),
       'purple'
       )

trt.left(45)
triangle(-58 - 75 * 0.5 * mth.sqrt(2),
         150 - 50 * 0.5 * mth.sqrt(2),
         37.5, 'yellow'
         )

trt.right(135)
triangle(-60 - 50 * 0.5 * mth.sqrt(2),
         150 - 25 * 0.5 * mth.sqrt(2),
         50, 'pink'
         )

trt.left(135)
triangle(-45 - 50 * 0.5 * mth.sqrt(2),
         150 - 75 * 0.5 * mth.sqrt(2),
         25, 'green'
         )

trt.right(180)
triangle(-45 - 87.5 * 0.5 * mth.sqrt(2),
         150 - 75 * 0.5 * mth.sqrt(2),
         25, 'orange'
         )

trt.right(150)
parallelogramm(-64 - 100 * 0.5 * mth.sqrt(2),
               141 - 37.5 * 0.5 * mth.sqrt(2) ,
               25, 25 * 0.5 * mth.sqrt(2),
               'moccasin'
               )

trt.mainloop()
