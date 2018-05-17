# (Locate the largest element) Write the following function that returns the location
#of the largest element in a two-dimensional list:
#def locateLargest(a):
#The return value is a one-dimensional list that contains two elements. These
#two elements indicate the row and column indexes of the largest element in the
#two-dimensional list.

def locateLargest(a):
    print(a)
    largest = 0
    r = 0
    c = 0
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            if a[i][j] >= largest:
                r = i+1
                c = j+1
    return r,c
    
def main():
    i = eval(input("Enter the number of rows"))
    j = eval(input("Enter the number of columns"))
    data = []
    for x in range(0,i):
        data.append([])
        print("Enter Row",(x+1),":")
        for y in range(0,j):
            print("Column",(y+1))
            ans = eval(input())
            data[x].append(ans) 
    r,c = locateLargest(data)
    print("The location of the largest element is at",r,",",c)
main()