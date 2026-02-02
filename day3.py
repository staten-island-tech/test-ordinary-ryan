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
""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):         
        square(length,90)
        length = length * 2
doubleSquares(5) """
""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5) """

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.right(5)

def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5  
    addSquares(60)
        
turtle.done()