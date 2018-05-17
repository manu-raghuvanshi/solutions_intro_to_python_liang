#Use Class LinearEquations from Chapter 7 Question 7
from Ch07Q07_class import LinearEquation

def main():
    lin = LinearEquation()
    x1,y1,x2,y2 = eval(input("Enter the endpoints of the first line segment (x1,y1,x2,y2):"))
    x3,y3,x4,y4 = eval(input("Enter the endpoints of the first line segment (x3,y3,x4,y4):"))
    lin.getA(x2-x1)
    lin.getB(y2-y1)
    lin.getC(x4-x3)
    lin.getD(y4-y3)
    lin.getE(x3-x1)
    lin.getF(y3-y1)
    if lin.isSolvable()!=0:
        print("Point OF Intersection:")
        print("X=",lin.getX())
        print("Y=",lin.getY())
    else:
        print("The lines do not intersect")

main()