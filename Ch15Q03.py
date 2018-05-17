#(Compute greatest common divisor using recursion) The gcd(m, n) can also be
#defined recursively as follows:

def gcd(m,n):
    div = 0
    if m%n==0:
        return n
    else:
        div = gcd(n,m%n)
        return div

def main():
    m,n = eval(input("Enter the two numbers"))
    print("Greatest Divisor is :",gcd(max(m,n),min(m,n)))

main()