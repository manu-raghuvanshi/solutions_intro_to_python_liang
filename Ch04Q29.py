import math
x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))
x2, y2, r2 = eval(input("Enter circle2's center x-, y-coordinates, and radius: "))

dist = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )

if (dist <= abs(r1-r2)):
    print("Circle 2 is inside Circle 1")
elif dist <= r1+r2:
    print("Circle 2 overlaps Circle 1")
elif dist > r1+r2:
    print("Circle 2 is outside Circle 1")