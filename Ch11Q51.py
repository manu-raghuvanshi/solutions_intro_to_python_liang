#(Sort students) Write a program that prompts the user to enter the students
#names and their scores on one line, and prints student names in increasing order
#of their scores. (Hint: Create a list. Each element in the list is a sublist with two
#elements: score and name. Apply the sort method to sort the list. This will sort
#the list on scores.)

i = eval(input("Enter the total number of students"))
data = []
for x in range (0,i):
    data.append([])
    print("Enter student name and score:")
    name = input()
    marks = eval(input())
    data[x].append(name)
    data[x].append(marks)

data.sort(key = lambda x:(x[1],x[0]))   
print(data)