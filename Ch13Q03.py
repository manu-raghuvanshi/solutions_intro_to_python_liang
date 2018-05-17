#Suppose that a text file contains an unspecified number
#of scores. Write a program that reads the scores from the file and displays their
#total and average. Scores are separated by blanks. Your program should prompt
#the user to enter a filename.
x = input("Input a file name")
z = open(x , "r")
y = z.read().split()
print(str(len(y)) + " numbers")
scores = [eval (x) for x in y]
total = sum(scores)
avg = total/len(scores)
print("average is " +str(avg))
print("sum is " +str(total))
z.close()