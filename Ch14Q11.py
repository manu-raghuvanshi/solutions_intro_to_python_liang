#(Count consonants and vowels) Write a program that prompts the user to enter a
#text filename and displays the number of vowels and consonants in the file. Use
#a set to store the vowels A, E, I, O, and U.
input = input("Enter a filename[Manu.txt]: ")
file = open(input, "r")
content = file.read()
content = content.lower()
vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}
consonants = 0
for char in content:
    if char in vowels:
        vowels[char]+=1

    else:
        consonants+=1
print("consonants " +str(consonants))
print(vowels)         
        
file.close()
