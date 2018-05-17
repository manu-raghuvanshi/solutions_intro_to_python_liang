#Display a pyramid
num = eval(input("Enter the number of lines"))
r = 1
x = num
space = 1
m = 0
while r<= num:
    while space<x:
        print(" ",end="")
        space +=1
    m = r
    if m == 1:
        print(m,end="")
    while m>1:
        print(m,end="")
        m -= 1
        if m==1:
            n = m
            while n<=r:
                print(n,end="")
                n += 1
    x = num - r
    r += 1
    space=1
    print("")