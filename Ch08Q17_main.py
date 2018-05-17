from Ch08Q17_class import Point

def main():
    pt = Point()
    x1,y1,x2,y2 = eval(input("Enter two points x1, y1, x2, y2:"))
    pt.getX(x1,y1)
    pt.getY(x2,y2)
    print("The distance between the two points is",format(pt.distance(), "0.2f"))
    if pt.isNearBy(pt.distance()) == True:
        print("The two points are near each other")
    else:
        print("The two points are not near each other")
main()