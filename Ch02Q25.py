import turtle

x,y,width,height = eval(input("Enter the Center of a Rectangle(x,y),it's width and it's height"))

turtle.penup()
turtle.goto(x,y)
turtle.write(".")
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

turtle.done()