import math
year = eval(input("Enter year: (e.g., 2008):"))
m = eval(input("Enter month: 1-12:"))
q = eval(input("Enter the day of the month: 1-31:"))
j = year/100 #Century
k = year%100 #Year of the Century

h = ( q + ((26 * (m + 1))/10) + k + (k / 4) + (j / 4) + (5*j) ) % 7
h = math.ceil(h)

if h == 0:
   print("Day of the week is Saturday")
elif h == 1:
   print("Day of the week is Sunday")
elif h == 2:
   print("Day of the week is Monday")
elif h == 3:
   print("Day of the week is Tuesday")
elif h == 4:
   print("Day of the week is Wednesday")
elif h == 5:
   print("Day of the week is Thursday")
elif h == 6:
   print("Day of the week is Friday")