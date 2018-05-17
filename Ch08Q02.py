#(Check substrings) You can check whether a string is a substring of another string
#by using the find method in the str class. Write your own function to implement
#find. Write a program that prompts the user to enter two strings and then checks
#whether the first string is a substring of the second string.

str1= input("Enter the string")
str2= input("Enter the substring you want to check")
len1= len(str1)
len2= len(str2)

for i in range (0,len1):
    count=0
    for j in range (0,len2):
        if i+j<len1:
            if str1[i+j]==str2[j]:
                count+=1
                index = i
            else:
                break
    if count == len2:
        break
if count == len2:
    print("Substring appears in String at index",i)
else:
    print("Substring does not exist")        