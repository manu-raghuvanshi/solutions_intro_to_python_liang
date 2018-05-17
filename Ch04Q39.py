import turtle
import math
x1,y1,r1 = eval(input("Enter the center x1,y1 and radii of CIRCLE 1:"))
x2,y2,r2 = eval(input("Enter the center x1,y1 and radii of CIRCLE 2:"))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.circle(r1)
turtle.down()

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.circle(r2)
turtle.down()

d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

if r1+r2 <= d:
    turtle.write("Circle 2 is outside Circle 1")
elif (d+r2 < r1) or (d+r1 < r2):
    turtle.write("Circle 2 is inside Circle 1")
else:
    turtle.write("Circle 2 Overlaps Circle 1")
    

turtle.done()