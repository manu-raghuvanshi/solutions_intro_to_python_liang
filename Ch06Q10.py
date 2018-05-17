count = 0
def isPrime(number):
    global count
    flag=0
    i=2
    while i <= (number//2):
        if number % i ==0:
            flag += 1
        i += 1
    if flag == 0:
        count += 1

def main():
    global count
    i = 2
    while i<10000:
        isPrime(i)
        i += 1
    print("Total number of prime number within 10,000 are", count)

main()