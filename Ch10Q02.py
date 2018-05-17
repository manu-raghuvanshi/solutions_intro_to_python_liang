#(Reverse the numbers entered) Write a program that reads a list of integers and
#displays them in the reverse order in which they were read.
n = eval(input("Enter the number of inputs"))
list1 = []
for i in range (0,n):
    print("enter a number")
    list1.append(eval(input()))
print("Normal List is - ",list1)
print("Reversed List is - ",list1[::-1])