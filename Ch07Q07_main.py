from Ch07Q07_class import LinearEquation

def main():
    lin = LinearEquation()
    a,b,c,d,e,f = eval(input("Enter a,b,c,d,e,f"))
    lin.getA(a)
    lin.getB(b)
    lin.getC(c)
    lin.getD(d)
    lin.getE(e)
    lin.getF(f)
    if lin.isSolvable()!=0:
        print("X=",lin.getX())
        print("Y=",lin.getY())
    else:
        print("The Equation is Unsolvable")

main()