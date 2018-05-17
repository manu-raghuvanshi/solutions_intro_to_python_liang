import random

lottery = random.randint(100,999) # randomly chooses a 3 digit number
user = eval(input("Enter a 3 Digit Number"))
lot,us = lottery,user #makes a bakcup of both the number
#extracts the digits of the lottery number
l3=lot%10 
lot=lot//10
l2=lot%10
l1=lot//10
#extracts the number of the User entered number
u3=us%10
us=us//10
u2=us%10
u1=us//10

flag=0 #to keep the count of how many number matches

if u1==l1:
    l1 = -1
    flag += 1
elif u1==l2:
    l2 = -1
    flag +=1
elif u1==l3:
    l3 = -1
    flag +=1
     
if u2==l1:
    l1 = -1
    flag += 1
elif u2==l2:
    l2 = -1
    flag +=1
elif u2==l3:
    l3 = -1
    flag +=1
    
if u3==l1:
    l1 = -1
    flag += 1
elif u3==l2:
    l2 = -1
    flag +=1
elif u3==l3:
    l3 = -1
    flag +=1
    
if user == lottery:
    print("Congratulations!!!You have won $10,000")
elif flag == 3:
    print("You have won $3000")
elif flag == 2 or flag == 1:
    print("You have won $1000")
elif flag == 0:
    print("Sorry, try your luck next time")    