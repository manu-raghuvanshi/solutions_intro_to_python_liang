#Write a program that computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
tuition = 10000
count = 1
cost = 0
while count<=14:
    tuition += tuition * 0.05
    if count==10:
        print("The cost of tuition after 10 years is $", format (tuition, '0.2f'))
    if count>10:
       cost = cost + tuition
    count = count + 1 
print("The total cost of four years' worth of tuition starting tenth year is $", format(cost,'0.2f'))