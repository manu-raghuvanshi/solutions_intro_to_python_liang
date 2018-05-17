#(Bubble sort) Write a sort function that uses the bubble-sort algorithm. The
#bubble-sort algorithm makes several passes through the list. On each pass,
#successive neighboring pairs are compared. If a pair is in decreasing order,
#its values are swapped; otherwise, the values remain unchanged. The technique
#is called a bubble sort or sinking sort because the smaller values gradually
# bubble their way to the top and the larger values sink to the bottom.
#Write a test program that reads in ten numbers, invokes the function, and displays
#the sorted numbers.

def bubbleSort(x):
    for i in range (len(x)-1,0,-1):
        for j in range (0,i):
            if (x[j]>x[j+1]):
                x[j],x[j+1] = x[j+1],x[j]
    print("Sorted List - ",x)

def main():
    lst = [] # Create a list
    print("Enter 10 numbers: ")
    for i in range(0,10):
        lst.append(eval(input()))
    bubbleSort(lst)

main()