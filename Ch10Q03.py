#(Count occurrence of numbers) Write a program that reads some integers
#between 1 and 100 and counts the occurrences of each. Here is a sample run of
#the program:

item = input("Enter integers between 1 and 100 separated by space:")
item = item.split(" ")
print(item)
for i in range(0,len(item)):
    if int(item[i]) >= 1:
        count = 1
        if i != len(item)-1: #so that i does not go to the last number
            for j in range(i+1, len(item)):
                if item[i] == item [j]:
                    count += 1
                    item[j] = -1 # removes the redundant item from index-j
        if count > 1:
            print(item[i],"occurs",count,"times")
        else:
            print(item[i],"occurs",count,"time")