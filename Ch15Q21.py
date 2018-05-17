#(Binary to decimal) Write a recursive function that parses a binary number as a
#string into a decimal integer. The function header is as follows:
#def binaryToDecimal(binaryString):

def binaryToDecimal(binaryString):
    if (len(binaryString)==1):
        return int(binaryString)* (2**(len(binaryString)-1))
    else:
        return int(binaryString[0])* (2**(len(binaryString)-1)) + binaryToDecimal(binaryString[1:])
def main():
    bin = input("Enter a Binary Number")
    print("The Decimal Equivalent of binary number is", binaryToDecimal(bin))
    
main()