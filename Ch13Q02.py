#(Count characters, words, and lines in a file) Write a program that will count the
#number of characters, words, and lines in a file. Words are separated by a whitespace
#character.

input = input("Enter a filename[Manu.txt]: ")
file = open(input, "r")
content = file.read()
print(str(len(content)) + " characters") 
print(str(len(content.split())) + " words") 
print(str(len(content.split('\n'))) + " lines") 
file.close()