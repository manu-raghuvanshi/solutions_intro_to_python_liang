x1,y1,x2,y2,x3,y3 = eval(input("Enter three points for a triangle:"))
#find the length of the sides
s1 = ((x2-x1)**2 + (y2-y1)**2) **0.5
s2 = ((x3-x2)**2 + (y3-y2)**2) **0.5
s3 = ((x1-x3)**2 + (y1-y3)**2) **0.5

s=(s1+s2+s3)/2
#calculate area
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5

print("The area of the triangle is", format(area,'.1f'))