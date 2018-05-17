#Find the two highest scores
num = eval(input("Enter the number of students"))
first = 0
second = 0
i = 1
while i <= num:
    score = eval(input("Enter the score"))
    if score>first:
        second = first
        first = score
    elif score>second:
        second = score
    i += 1
print("The highest number is",first,"and the second highest number is",second)