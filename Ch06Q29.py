#Financial: credit card number validation

# Return true if the card number is valid
def isValid(number):
    if number % 10 == 0:
        return True
    else:
        return False
    
# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    count = 1
    sum = 0
    while number != 0:
        if count%2==0:
            ext = number%10
            sum = sum + getDigit(ext)
            number = number // 10
        else:
            number = number // 10
        count += 1
    print (sum)
    return sum

# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    number = number * 2
    sum = 0
    if number >= 10:
        while number != 0:
            ext = number%10
            sum = sum + ext
            number = number // 10
        return sum
    else:
        return number
        
# Return sum of odd place digits in number
def sumOfOddPlace(number):
    count = 1
    sum = 0
    while number != 0:
        if count%2!=0:
            ext = number%10
            sum = sum + ext
            number = number // 10
        else:
            number = number // 10
        count += 1
    print(sum)
    return sum
    
def main():
    number = eval(input("Enter the 13 to 16 digit Card Number"))
    step1 = sumOfDoubleEvenPlace(number)
    step2 = sumOfOddPlace(number)
    valid = isValid(step1 + step2)
    if valid == True:
        print("The Card is Valid")
    else:
        print("The Card is Invalid")

main()