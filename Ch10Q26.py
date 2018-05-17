#(Merge two sorted lists) Write the following function that merges two sorted lists
#into a new sorted list:
#def merge(list1, list2):
#Implement the function in a way that takes len(list1) + len(list2) comparisons.
#Write a test program that prompts the user to enter two sorted lists and
#displays the merged list. Here is a sample run:

def merge(list1,list2):
    list3=[]
    i=0
    j=0
    while i<=len(list1)-1 and j<=len(list2)-1: #will run till the index of smaller list
        if list1[i] <= list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1
                
    #will add the remaining elements of the longer lists
    if i>=len(list1):
        for x in range (j,len(list2)):
            list3.append(list2[x])
    
    if j>=len(list2):
        for x in range (i,len(list1)):
            list3.append(list1[x])
            
    print("Unsorted Combined List - ", list3)

def main():
    item1 = input("Enter integers separated by spaces:")
    item1 = item1.split(" ")
    for i in range (0,len(item1)):
        item1[i] = eval(item1[i])
    item1.sort()
    
    item2 = input("Enter integers separated by spaces:")
    item2 = item2.split(" ")
    for i in range (0,len(item2)):
        item2[i] = eval(item2[i])
    item2.sort()
    
    print("Sorted List1 - ",item1)
    print("Sorted List2 - ",item2)
    merge(item1, item2)

main()