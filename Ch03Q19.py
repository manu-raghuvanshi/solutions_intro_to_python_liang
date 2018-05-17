import math
import turtle

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

if a+b>c and b+c>a and c+a>b:
    
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.write("P1=" + str(round(A)))
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.penup()
    turtle.write("P2=" + str(round(B)))
    turtle.pendown()
    turtle.goto(x3,y3)
    turtle.penup()
    turtle.write("P3=" + str(round(C)))
    turtle.pendown()
    turtle.goto(x1,y1)
    turtle.done()
    
else:
    
    print("The Triangle is not possible")