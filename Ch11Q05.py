#(Algebra: add two matrices) Write a function to add two matrices. The header of
#the function is:
#def addMatrix(a, b):
#In order to be added, the two matrices must have the same dimensions and the
#same or compatible types of elements. Let c be the resulting matrix. 

def addMatricx(a,b):
    sum = 0
    c = []
    for i in range(0,3):
        c.append([])
        for j in range(0,3):
            c[i].append(a[i][j]+b[i][j])
    return c

def main():
    item1 = []
    item2 = []
    print("Enter Matrix 1:")
    for i in range(0,3):
        item1.append([])
        for j in range(0,3):
            item1[i].append(eval(input()))
    
    print("Enter Matrix 2:")       
    for i in range(0,3):
        item2.append([])
        for j in range(0,3):
            item2[i].append(eval(input()))
            
    print("Sum of the matrices",addMatricx(item1,item2))
    
main()