from Ch07Q10_class import Time

def main():
    t = Time()
    print("Current Time is",t.getHour(),":",t.getMinutes(),":",t.getSecond())
    elapse = eval(input("Enter the elapsed time:"))
    t.setTime(elapse)
    
main()