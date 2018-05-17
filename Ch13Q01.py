#(Remove text) Write a program that removes all the occurrences of a specified
#string from a text file. Your program should prompt the user to enter a filename
#and a string to be removed. 
strf = input("Enter a filename:")
x = open(strf, "r")
y = input("Enter a string to be removed").strip()
a = x.read()

z = [x for x in a.split()]
for string in z:
    if(string==(y)): 
        z.remove(y)
            
out = "" #adding the words in the file that user did not remove
for stri in z:
    out = out + stri + " "
    
print(out)
x.close()

ofl = open(strf, "w")
ofl.write(out)
ofl.close()