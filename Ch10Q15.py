#(Sorted?) Write the following function that returns true if the list is already
#sorted in increasing order:
#def isSorted(lst):
#Write a test program that prompts the user to enter a list and displays whether the
#list is sorted or not.

item = input("Enter list :")
item = item.split(" ")
print(item)
flag = 0
for i in range (0,len(item)):
    item[i] = eval(item[i])
for i in range (0,len(item)-1):
    if item[i]>item[i+1]:
        flag = 1
        break
if flag == 1:
    print("The list is not sorted")
else:
    print("The list is already sorted")