import math
import turtle

turtle.setup(800,600)

turtle.penup()
turtle.goto(0,100)
turtle.write("Y")
turtle.pendown()
turtle.goto(0,-100)

turtle.penup()
turtle.goto(200,0)
turtle.write("X")
turtle.pendown()
turtle.goto(-200,0)
turtle.penup()

for x in range(-25,25):
    turtle.color("red")
    y = math.pow(x,2)
    turtle.goto(x, y)
    turtle.pendown()
    
turtle.done()