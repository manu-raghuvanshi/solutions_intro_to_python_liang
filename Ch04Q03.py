a,b,c,d,e,f = eval(input("Enter a, b, c, d, e, f:"))
print(a,"x +",b,"y=",e)
print(c,"x +",d,"y=",f)
numx = e*d - b*f #numerator of x
numy = a*f - e*c #numerator of y
den = a*d - b*c #common denominator
if den != 0:
    print("x is",(numx/den),"and y is",(numy/den))
else:
    print("The equation has no solution")