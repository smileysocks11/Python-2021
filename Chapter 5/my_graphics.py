# ---------------------------------------------------------------------
import turtle

def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    
def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
def circle_nofill(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.color(color)
    turtle.pendown()
    turtle.circle(radius)
    
def line(startX, startY, endX, endY, color):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX, endY)
    
