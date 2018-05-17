#Palindrome integer
num = 1

def isPrime(number):
    flag=0
    i=2
    while i <= (number//2):
        if number % i ==0:
            flag += 1
        i += 1
    if flag == 0:
        return True
    else:
        return False
    
def reverse(number):
    rev = 0
    while number != 0:
        ext = number % 10 # extracts the last digit
        rev = (rev*10) + ext # reverses the number
        number = number //10 # removes the number
    return rev

def isPalindrome(number,i):
    if number == i:
        return True
    else:
        return False
    
def printLine(i):
    global num
    if num%10 == 0:
        print(i,end="   ")
        print()
    else:
        print(i,end="   ")
    num +=1

def main():
    global num
    i = 2
    while num<=100:
        prime = isPrime(i)
        if prime == True:
            rev = reverse(i)
            pal = isPalindrome(rev,i)
            if pal == True:
                printLine(i)                
        i += 1
            
main()