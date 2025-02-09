# Case-study 1
# Developers: Dak A., Kruykov G., Lebedev N., Cheremisina E.

import turtle as trt
import math as mth

trt.penup()

def triangle(x, y, l, color):
    '''
    Function, drawing triangle
    :param x: left end of hypothenuse coordinate x
    :param y: left end of hypothenuse coordinate y
    :param l: length of hypothenuse
    :param color: triangle fillcolor
    :return: None
    '''
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
    pass

def rectangle (x, y, l, w, color):
    '''
    Function, drawing rectangle
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param l: length of rectangle's horizontal side
    :param w: length of rectangle's vertical side
    :param color: rectangle fillcolor
    :return: None
    '''
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

def parallelogram (x, y, l, w, color):
    '''
    Function, drawing rectangle
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param l: length of parallelogram's horizontal side
    :param w: length of parallelogram's vertical side
    :param color: parallelogram fillcolor
    :return: None
    '''
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

def mosaic():
    '''
    Function, drawing mosaic
    :params: None
    :return: None
    '''
    triangle(-50, 50, 100, 'red')

    trt.right(90)
    triangle(50, 50, 50, 'green')

    trt.right(45)
    rectangle(25, 25,
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

    parallelogram(-25, -25,50,
                   50 * 0.5 * mth.sqrt(2),
                   'moccasin')
    pass

def horse():
    '''
    Function, drawing horse
    :params: None
    :return: None
    '''
    trt.right(180)
    triangle(-100, -10, 50, 'pink')

    trt.right(90)
    parallelogram(-125, 21 + 25 * 0.5 * mth.sqrt(2),25,
                   25 * 0.5 * mth.sqrt(2),
                   'moccasin'
                   )

    trt.right(135)
    rectangle(-125, 16,
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
    pass

def swan():
    '''
    Function, drawing swan
    :params: None
    :return: None
    '''
    trt.left(135)
    triangle(-90, -80, 37.5, 'yellow')

    trt.right(135)
    rectangle(-86.25 - 25 * 0.5 * mth.sqrt(2),
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
    parallelogram(-97.5 - 25 * 0.5 * mth.sqrt(2),
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
    pass

def lion():
    '''
    Function, drawing lion
    :params: None
    :return: None
    '''
    trt.right(135)
    triangle(-50,150,50, 'red')

    trt.right(135)
    rectangle(-45, 130,
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
    parallelogram(-64 - 100 * 0.5 * mth.sqrt(2),
                   141 - 37.5 * 0.5 * mth.sqrt(2) ,
                   25, 25 * 0.5 * mth.sqrt(2),
                   'moccasin'
                   )
    pass

def bear():
    '''
    Function, drawing bear
    :params: None
    :return: None
    '''
    trt.right(90)
    triangle(30,150,50, 'red')

    trt.right(135)
    triangle(30 + 50 * 0.5 * mth.sqrt(2),
             150,50, 'pink'
             )

    trt.left(45)
    triangle(30 + 12.5 * 0.5 * mth.sqrt(2),
             150 - 37.5 * 0.5 * mth.sqrt(2),
             37.5, 'yellow'
             )

    rectangle(30 + 50 * 0.5 * mth.sqrt(2), 150,
           25 * 0.5 * mth.sqrt(2),
           25 * 0.5 * mth.sqrt(2),
           'purple'
           )

    trt.right(45)
    triangle(30 + 75 * 0.5 * mth.sqrt(2),
             150,25, 'orange'
             )

    trt.right(45)
    parallelogram(30 + 50 * 0.5 * mth.sqrt(2),
                   150 - 37.5 * 0.5 * mth.sqrt(2) ,
                   25, 25 * 0.5 * mth.sqrt(2),
                   'moccasin'
                   )

    trt.right(45)
    triangle(23, 142 - 50 * 0.5 * mth.sqrt(2),
             25, 'green'
             )
    pass

def rhino():
    '''
    Function, drawing rhino
    :params: None
    :return: None
    '''
    trt.right(90)
    triangle(100+25*mth.sqrt(2), 130-12.5*mth.sqrt(2),
             12.5*mth.sqrt(2), 'red'
             )

    trt.right(135)
    triangle(100+45*mth.sqrt(2), 130+2.5*mth.sqrt(2),
             40, 'blue'
             )

    trt.left(45)
    triangle(100+30*mth.sqrt(2), 130-12.5*mth.sqrt(2),
             50, 'green'
             )

    rectangle(100+40*mth.sqrt(2), 130-12.5*mth.sqrt(2),
              10*mth.sqrt(2), 10*mth.sqrt(2), 'yellow'
              )

    trt.left(90)
    triangle(100+55*mth.sqrt(2), 130-12.5*mth.sqrt(2),
             25*mth.sqrt(2), 'orange'
             )

    parallelogram(100+67.5*mth.sqrt(2), 130,
                  12.5*mth.sqrt(2), 25, 'purple'
                  )

    trt.right(45)
    triangle(100+67.5*mth.sqrt(2), 130+12.5*mth.sqrt(2),
             25, 'brown'
             )
    pass

def rabbit():
    '''
    Function, drawing rabbit
    :params: None
    :return: None
    '''
    # Rabbit should be smaller
    trt.left(90)
    triangle(115, -60, 50, 'red')

    trt.left(45)
    triangle(115, -60,
             50*mth.sqrt(2),'pink'
             )

    triangle(105, 0, 70, 'blue')

    rectangle(130, 20, 20, 20, 'brown')

    trt.left(135)
    parallelogram(100, 20, 30*mth.sqrt(2),
                  30, 'moccasin'
                  )

    trt.left(45)
    triangle(150, 20,
             30*mth.sqrt(2), 'green'
             )

    trt.left(225)
    triangle(210, 50,
             30*mth.sqrt(2), 'yellow'
             )
    pass

#Two figures are in progress...

mosaic()
horse()
swan()
lion()
bear()
rhino()
rabbit()
trt.mainloop()

