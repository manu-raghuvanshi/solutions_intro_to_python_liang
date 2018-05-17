#(Statistics: compute deviation) Exercise 5.46 computes the standard deviation of
#numbers. This exercise uses a different but equivalent formula to compute the
#standard deviation of n numbers.
#To compute the standard deviation with this formula, you have to store the
#individual numbers using a list, so that they can be used after the mean is obtained.
#Your program should contain the following functions:
# Compute the standard deviation of values
#def deviation(x):
# Compute the mean of a list of values
#def mean(x):
#Write a test program that prompts the user to enter a list of numbers and displays
#the mean and standard deviation

def mean(x):
    sum = 0
    for i in range(0,len(x)):
        sum += x[i]
    return (sum/len(x))

def deviation(x):
    m = mean(x)
    sum = 0
    print("The Mean is ", format(m,"0.2f"))
    for i in range(0,len(x)):
        sum += (x[i]-m)**2
    deviation = (sum/((len(x)-1)))**0.5
    print("The standard deviation is",format(deviation,"0.2f"))

def main():
    item = input("Enter integers :")
    item = item.split(" ")
    print(item)
    for i in range (0,len(item)):
        item[i] = eval(item[i])
    deviation(item)
    
main()