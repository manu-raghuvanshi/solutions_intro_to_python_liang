num = eval(input("Enter a Number"))
new= 0
while num>0:
    ext = num % 10;
    new = (new*10)+ext
    num = num // 10
print("The Reversed Number is", new)