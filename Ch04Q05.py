today = eval(input("Enter today's day from 0 to 6:"))
elapse = eval(input("Enter the number of days elapsed since today:"))
future = (today + elapse)%7
if today == 0:
   print("Today is Sunday and the future day is", end=" ")
elif today == 1:
   print("Today is Monday and the future day is", end=" ")
elif today == 2:
   print("Today is Tuesday and the future day is", end=" ")
elif today == 3:
   print("Today is Wednesday and the future day is", end=" ")
elif today == 4:
   print("Today is Thursday and the future day is", end=" ")
elif today == 5:
   print("Today is Friday and the future day is", end=" ")
elif today == 6:
   print("Today is Saturday and the future day is", end=" ")
if future == 0:
   print("Sunday")
elif future == 1:
   print("Monday")
elif future == 2:
   print("Tuesday")
elif future == 3:
   print("Wednesday")
elif future == 4:
   print("Thursday")
elif future == 5:
   print("Friday")
elif future == 6:
   print("Saturday")