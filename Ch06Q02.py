#Sum the digits in an integer
def sumDigits(n):
    sum = 0
    while n != 0:
        ext = n % 10 # extracts the last digit
        sum = sum + ext # sum of the digits
        n = n //10 # removes the number
    return sum
def main():
    num = eval(input("Input the number to find the sum of the digits"))
    print("The sum of the digits are",sumDigits(num))

main()