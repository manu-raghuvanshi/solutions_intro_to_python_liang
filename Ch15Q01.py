#(Sum the digits in an integer using recursion) Write a recursive function that computes
#the sum of the digits in an integer.

def sumDigits(n):
    sum = 0
    if n!= 0:
        ext = n%10
        sum = sumDigits(n//10) + ext
        return sum
    else:
        return 0

def main():
    num = eval(input("enter a number"))
    print("Sum of the digits in the integer are ", sumDigits(num))
    
main()