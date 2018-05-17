#Display matrix of 0s and 1s
import random
def printMatrix(n):
    total = n*n
    count = 1
    while count<=total:
        print(random.randint(0,1),end=" ")
        if count%n==0:
            print()
        count += 1

def main():
    n = eval(input("Enter N:"))
    printMatrix(n)

main()