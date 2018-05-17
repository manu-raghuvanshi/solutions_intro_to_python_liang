import math

atlx, atly= 33.7489954,-84.3879824
orlx, orly= 28.5383355,-81.3792365
savx, savy= 32.0835407,-81.0998342
chax, chay= 35.2270869,-80.8431267

radius = 6371.01
#Convert degrees into Radians
atlx= math.radians(atlx)
atly= math.radians(atly)
orlx= math.radians(orlx)
orly= math.radians(orly)
savx= math.radians(savx)
savy= math.radians(savy)
chax= math.radians(chax)
chay= math.radians(chay)
#Use the Great Circle Distance Formula
s1 = radius * math.acos (math.sin(atlx) * math.sin(chax) + math.cos(atlx) * math.cos(chax) * math.cos(atly - chay))
s2 = radius * math.acos (math.sin(atlx) * math.sin(orlx) + math.cos(atlx) * math.cos(orlx) * math.cos(atly - orly))
s3 = radius * math.acos (math.sin(chax) * math.sin(orlx) + math.cos(chax) * math.cos(orlx) * math.cos(chay - orly))
s4 = radius * math.acos (math.sin(savx) * math.sin(chax) + math.cos(savx) * math.cos(chax) * math.cos(savy - chay))
s5 = radius * math.acos (math.sin(savx) * math.sin(orlx) + math.cos(savx) * math.cos(orlx) * math.cos(savy - orly))

sa=(s1+s2+s3)/2
sb=(s3+s4+s5)/2

area1 = (sa*(sa-s1)*(sa-s2)*(sa-s3))**0.5
area2 = (sb*(sb-s3)*(sb-s4)*(sb-s5))**0.5
total_area = area1 + area2
print("The estimated area enclosed by these four cities is ", total_area)