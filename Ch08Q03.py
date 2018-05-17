#(Check password) Some Web sites impose certain rules for passwords. Write a
#function that checks whether a string is a valid password. Suppose the password
#rules are as follows:
#■ A password must have at least eight characters.
#■ A password must consist of only letters and digits.
#■ A password must contain at least two digits.
#Write a program that prompts the user to enter a password and displays valid
#password if the rules are followed or invalid password otherwise.

pw = input("Enter the password")
l = len(pw) #length of the password
digit = 0
ch = 0
if l>=8:
    for i in range (0,l):
        if (ord(pw[i])>=48 and ord(pw[i])<=57) or (ord(pw[i])>=65 and ord(pw[i])<=90) or (ord(pw[i])>=97 and ord(pw[i])<=122):
            if ord(pw[i])>=48 and ord(pw[i])<=57:
                digit += 1
            else:
                ch += 1
    if digit >= 2:
        if ch + digit == l:
            print("Valid Password")
        else:
            print("Invalid password")
    else:
        print("Invalid password")
else:
    print("Invalid password")