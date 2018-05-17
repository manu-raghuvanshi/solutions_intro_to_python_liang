import turtle

x=0
y=0
i=1
turtle.setheading(45)

while i<=8:
    x = 200
    if(i%2!=0):
        j=1
        while(j<=8):
            if j%2!=0:
                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()
                turtle.circle(30,steps = 4)
                x += 40
            else:
                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(30,steps = 4)
                turtle.end_fill()
                x += 40
            j += 1
    else:
        j=1
        while(j<=8):
            if j%2!=0:
                 turtle.penup()
                 turtle.goto(x,y)
                 turtle.pendown()
                 turtle.begin_fill()
                 turtle.circle(30,steps = 4)
                 turtle.end_fill()
                 x += 40   
            else:
                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()
                turtle.circle(30,steps = 4)
                x += 40
            j += 1
    i += 1
    y -= 40
turtle.done()