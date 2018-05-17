#Palindrome integer
num = 0
def reverse(number):
    rev = 0
    while number != 0:
        ext = number % 10 # extracts the last digit
        rev = (rev*10) + ext # reverses the number
        number = number //10 # removes the number
    return rev    
def isPalindrome(number):
    global num
    if number == num:
        return True
    else:
        return False
    
def main():
    global num
    num = eval(input("Input the number to find if it is a palindrome or not"))
    rev = reverse(num)
    pal = isPalindrome(rev)
    if pal == True:
        print("The Number is a Palindrome")
    else:
        print("The Number is not a Palindrome")

main()