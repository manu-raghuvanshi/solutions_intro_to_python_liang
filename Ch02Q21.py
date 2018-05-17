saving = eval(input("Enter the monthly saving amount:"))
rate = 0.05/12 #rate
sum = 0 #initializes sum to 0
i=1
while i<=6:
    sum = (saving+sum) *(1+rate) #stores the sum
    i+=1
print ("After the sixth month, the account value is", sum)