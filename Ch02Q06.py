num = eval(input("Enter a number between 0 and 1000:"))
sum = 0
while num != 0:
    ext = num % 10 # extracts the last digit
    sum = sum + ext # sum of the digits
    num = num //10 # removes the number
print("The sum of the digits is", sum)