#(Longest common prefix) Write a method that returns the longest common prefix
#of two strings. For example, the longest common prefix of distance and
#disinfection is dis. The header of the method is:
#def prefix(s1, s2)
#If the two strings have no common prefix, the method returns an empty string.
#Write a main method that prompts the user to enter two strings and displays their common prefix.

def prefix(s1, s2):
    len1= len(s1)
    len2= len(s2)
    prefix=""
    count=0
    for i in range (0,min(len1,len2)):
        if s1[i]==s2[i]:
            count+=1
            prefix = prefix + s2[i]
        else:
            break
    if count >= 1:
        print("The largest common prefix is - ",prefix)
    else:
        print("Prefix doesn't exist")
    
def main():
    st1 = input("Enter the first word")
    st2 = input("Enter the second word")
    prefix(st1, st2)

main()