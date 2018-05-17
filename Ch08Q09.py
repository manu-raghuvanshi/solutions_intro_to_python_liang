#(Binary to hex) Write a function that parses a binary number into a hex number.
#The function header is:
#def binaryToHex(binaryValue):
#Write a test program that prompts the user to enter a binary number and displays
#the corresponding hexadecimal value.

import math

def binaryToHex(binaryValue):
    i=0
    hex = ""
    decimalValue = 0
    while binaryValue!=0:
        ext = binaryValue%10
        if ext == 1:
            decimalValue = decimalValue + math.pow(2,i)
        binaryValue = binaryValue // 10
        i+=1
    decimalValue = int(decimalValue)
    print("The Decimal Value of the binary number is",decimalValue)
    if decimalValue !=0:
        while decimalValue!=0:
            rem = decimalValue % 16
            if rem <= 9:
                hex = str(rem) + hex
            elif rem == 10:
                hex = "A" + hex
            elif rem == 11:
                hex = "B" + hex
            elif rem == 12:
                hex = "C" + hex
            elif rem == 13:
                hex = "D" + hex
            elif rem == 14:
                hex = "E" + hex
            elif rem == 15:
                hex = "F" + hex
            elif rem == 16:
                hex = "G" + hex
            decimalValue = decimalValue // 16
        print("The Hexadecimal Value of the binary number is",hex)
    else:
        print("The Hexadecimal Value of the binary number is 0")
def main():
    bin = eval(input("Enter the binary number"))
    binaryToHex(bin)
    
main()