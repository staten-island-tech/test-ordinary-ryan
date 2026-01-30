import turtle
from turtle import *
t = Turtle()

""" for i in range(60):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90) 
    t.right(5) 
 """
""" for i in range(3):
    t.forward(100)
    t.left(120) """
""" 
sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90)
 """
sidelength = 100
rotate = 90
def square(x,y):
    for i in range(iRange):
        t.forward(x)
        t.left(y)
square(100,90)

def doubleSquare(iRange):
    length = 25
    for i in range(iRange):
        square(length,90)
        length = length * 2
    doubleSquare(5)

turtle.done()