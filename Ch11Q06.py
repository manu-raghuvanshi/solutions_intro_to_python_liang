#(Algebra: multiply two matrices) Write a function to multiply two matrices. The
#header of the function is:
#def multiplyMatrix(a, b)
#To multiply matrix a by matrix b, the number of columns in a must be the same as
#the number of rows in b, and the two matrices must have elements of the same or
#compatible types. Let c be the result of the multiplication.

def multiplyMatric(a,b):
    sum = 0
    c = []
    for i in range(0,3):
        c.append([])
        for j in range(0,3):
            c[i].append(a[i][0]*b[0][j] + a[i][1]*b[1][j] + a[i][2]*b[2][j])
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
            
    print("Multiplication[ of the matrices",multiplyMatric(item1,item2))
    
main()