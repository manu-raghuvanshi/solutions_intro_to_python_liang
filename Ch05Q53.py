import math
import turtle

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
turtle.goto(-200,-30)
turtle.write("-2 \u03c0")
turtle.goto(200,-30)
turtle.write("2 \u03c0")

for x in range(-200,200):
    turtle.color("blue")
    turtle.goto(x, (50 * math.sin((x/100) * 2 * math.pi)))
    turtle.pendown()
turtle.penup()

for x in range(-200,200):
    turtle.color("red")
    turtle.goto(x, (50 * math.cos((x/100) * 2 * math.pi)))
    turtle.pendown()
    
turtle.done()