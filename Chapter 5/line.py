# ---------------------------------------------------------------------

import turtle

def line(startX, startY, endX, endY, color):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX, endY)