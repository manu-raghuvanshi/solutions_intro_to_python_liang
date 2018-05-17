#(Sum the major diagonal in a matrix) Write a function that sums all the numbers
#of the major diagonal in an n*n matrix of integers using the following header:
#def sumMajorDiagonal(m):
#The major diagonal is the diagonal that runs from the top left corner to the bottom
#right corner in the square matrix. Write a test program that reads a 4*4 matrix and
#displays the sum of all its elements on the major diagonal. Here is a sample run:

def sumMajorDiagonal(m):
    sum = 0
    for i in range(0,4):
        for j in range(0,4):
            if i == j:
                sum += m[i][j]
    return sum

def main():
    item = []
    for i in range(0,4):
        item.append([])
        print("Enter a 4-by-4 matrix row for row",i+1,":")
        for j in range(0,4):
            item[i].append(eval(input()))
    print("Sum of the elements in the major diagonal is",sumMajorDiagonal(item))
    
main()