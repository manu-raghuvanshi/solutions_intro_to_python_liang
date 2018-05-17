import turtle
import random

def drawCircle(x=50,y=0,radius =50 ):
    turtle.penup()
    turtle.goto(50,0)
    turtle.pendown()
    turtle.circle(50)
    
    for i in range (0,10):
        x = random.randint(25,75)
        y = random.randint(25,75)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.dot(4)
        turtle.penup() 
    
    
    
def drawRectangle(x= -75, y= 0, width = 100, height = 100):
       turtle.penup()
       turtle.goto(x,y)
       turtle.forward(width/2)
       turtle.down()
       turtle.left(90)
       turtle.forward(height/2)
       turtle.left(90)
       turtle.forward(width)
       turtle.left(90)
       turtle.forward(height)
       turtle.left(90)
       turtle.forward(width)
       turtle.left(90)
       turtle.forward(height/2)
       
       for i in range (0,10):
           x= random.randint(-125 , -25)
           y = random.randint(-50 , 50)
           turtle.penup()
           turtle.goto(x, y)
           turtle.pendown()
           turtle.dot(4)
           turtle.penup()


def main():
    drawCircle()
    drawRectangle()

main()
turtle.done()