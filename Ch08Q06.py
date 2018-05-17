#(Count the letters in a string) Write a function that counts the number of letters in
#a string using the following header:
#def countLetters(s):
#Write a test program that prompts the user to enter a string and displays the number
#of letters in the string.

def countLetters(s):
    l = len(s)
    ch = 0
    for i in range(0,l):
        if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
            ch += 1
    print("The number of letters in the string is", ch)
    
def main():
    str = input("Enter a String")
    countLetters(str)

main()