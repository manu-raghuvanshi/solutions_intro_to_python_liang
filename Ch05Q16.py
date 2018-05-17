#Compute the greatest common divisor
n1,n2 = eval(input("input the 2 numbers to find the GCD"))
if (n1>=n2):
    min = n2
else:
    min = n1
for min in range(min,0,-1):
    if n1%min==0 and n2%min==0:
        gcd = min
        break
print("The GCD of",n1,"and",n2,"is",min)