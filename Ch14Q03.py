#(Count the occurrences of each keyword) Write a program that reads in a Python
#source code file and counts the occurrence of each keyword in the file. Your program
#should prompt the user to enter the Python source code filename

import os.path

keywords = {"and":0, "del":0, "from":0, "not":0, "while":0,"as":0,"elif":0, "global":0, "or":0, "with":0, "assert":0, "else":0, \
        "if":0, "pass":0, "yield":0, "break":0, "except":0, "import":0, "print":0, "class":0, "exec":0, "in":0, "raise":0, \
        "continue":0, "finally":0, "is":0, "return":0, "def":0, "for":0, "lambda":0, "try":0}

strFile = input("Enter a filename that contains python source code:")

if os.path.isfile(strFile):#check if file exists
    f1 = open(strFile, "r")
else:
    exit()
    
s = f1.read().split()
strList = [x for x in s]

for word in strList:
    for char in word:
        if(char ==(":") or char==("+") or char==(")") or char==("(") or char==("[") or char==("]") or char==("=") or char==(",") or char==(".") \
           or char==("?") or char==("!")): 
            char = ""

strKeys = keywords.keys()

for strItem in strList:
    print(strItem)
    if(strItem in strKeys): 
        keywords[strItem] += 1

for strItem in strList:
    if(strItem in strKeys): 
        print("Keyword ("+str(strItem)+ ") is repeated " + str(keywords[strItem]) + " times in the source code")
    
