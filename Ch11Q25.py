#(Markov matrix) An matrix is called a positive Markov matrix if each element
#is positive and the sum of the elements in each column is 1. Write the following
#function to check whether a matrix is a Markov matrix:
#def isMarkovMatrix(m):

def isMarkovMatrix(m):
    flag = 0
    for i in range(0,3):
        sum = 0
        for j in range(0,3):
            sum += m[j][i]
        if sum != 1:
            flag = 1
            break
    if flag == 0:
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")

def main():
    data = []
    print("Enter a 3-by-3 matrix row by row:")
    for x in range(0,3):
        data.append([])
        for y in range(0,3):
            ans = eval(input())
            data[x].append(ans)
    isMarkovMatrix(data)
    
main()