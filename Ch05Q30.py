#Display the first days of each month
year = eval(input("Enter the year"))
day  = eval(input("Enter the number for the corresponding First day of the Year eg:-0 for sunday,1 for monday and so on"))
i = 1
while i<=12:
    if i==1:
        rem = day%7
        if rem == 0:
            print("January 1",year,"is Sunday")
        if rem == 1:
            print("January 1",year,"is Monday")
        if rem == 2:
            print("January 1",year,"is Tuesday")
        if rem == 3:
            print("January 1",year,"is Wednesday")
        if rem == 4:
            print("January 1",year,"is Thursday")
        if rem == 5:
            print("January 1",year,"is Friday")
        if rem == 6:
            print("January 1",year,"is Saturday")
        day = day + 31
    i+=1
    if i==2:
        rem = day%7
        if rem == 0:
            print("February 1",year,"is Sunday")
        if rem == 1:
            print("February 1",year,"is Monday")
        if rem == 2:
            print("February 1",year,"is Tuesday")
        if rem == 3:
            print("February 1",year,"is Wednesday")
        if rem == 4:
            print("February 1",year,"is Thursday")
        if rem == 5:
            print("February 1",year,"is Friday")
        if rem == 6:
            print("February 1",year,"is Saturday")
        if year%4==0:
            if year%100 and year%400==0:
                day = day + 29
            else:
                day = day + 29
        else:
            day = day + 28
    i+=1
    if i==3:
        rem = day%7
        if rem == 0:
            print("March 1",year,"is Sunday")
        if rem == 1:
            print("March 1",year,"is Monday")
        if rem == 2:
            print("March 1",year,"is Tuesday")
        if rem == 3:
            print("March 1",year,"is Wednesday")
        if rem == 4:
            print("March 1",year,"is Thursday")
        if rem == 5:
            print("March 1",year,"is Friday")
        if rem == 6:
            print("March 1",year,"is Saturday")
        day = day + 31
    i+=1
    if i==4:
        rem = day%7
        if rem == 0:
            print("April 1",year,"is Sunday")
        if rem == 1:
            print("April 1",year,"is Monday")
        if rem == 2:
            print("April 1",year,"is Tuesday")
        if rem == 3:
            print("April 1",year,"is Wednesday")
        if rem == 4:
            print("April 1",year,"is Thursday")
        if rem == 5:
            print("April 1",year,"is Friday")
        if rem == 6:
            print("April 1",year,"is Saturday")
        day = day + 30
    i+=1
    if i==5:
        rem = day%7
        if rem == 0:
            print("May 1",year,"is Sunday")
        if rem == 1:
            print("May 1",year,"is Monday")
        if rem == 2:
            print("May 1",year,"is Tuesday")
        if rem == 3:
            print("May 1",year,"is Wednesday")
        if rem == 4:
            print("May 1",year,"is Thursday")
        if rem == 5:
            print("May 1",year,"is Friday")
        if rem == 6:
            print("May 1",year,"is Saturday")
        day = day + 31
    i+=1
    if i==6:
        rem = day%7
        if rem == 0:
            print("June 1",year,"is Sunday")
        if rem == 1:
            print("June 1",year,"is Monday")
        if rem == 2:
            print("June 1",year,"is Tuesday")
        if rem == 3:
            print("June 1",year,"is Wednesday")
        if rem == 4:
            print("June 1",year,"is Thursday")
        if rem == 5:
            print("June 1",year,"is Friday")
        if rem == 6:
            print("June 1",year,"is Saturday")
        day = day + 30
    i+=1
    if i==7:
        rem = day%7
        if rem == 0:
            print("July 1",year,"is Sunday")
        if rem == 1:
            print("July 1",year,"is Monday")
        if rem == 2:
            print("July 1",year,"is Tuesday")
        if rem == 3:
            print("July 1",year,"is Wednesday")
        if rem == 4:
            print("July 1",year,"is Thursday")
        if rem == 5:
            print("July 1",year,"is Friday")
        if rem == 6:
            print("July 1",year,"is Saturday")
        day = day + 31
    i+=1
    if i==8:
        rem = day%7
        if rem == 0:
            print("August 1",year,"is Sunday")
        if rem == 1:
            print("August 1",year,"is Monday")
        if rem == 2:
            print("August 1",year,"is Tuesday")
        if rem == 3:
            print("August 1",year,"is Wednesday")
        if rem == 4:
            print("August 1",year,"is Thursday")
        if rem == 5:
            print("August 1",year,"is Friday")
        if rem == 6:
            print("August 1",year,"is Saturday")
        day = day + 31
    i+=1
    if i==9:
        rem = day%7
        if rem == 0:
            print("September 1",year,"is Sunday")
        if rem == 1:
            print("September 1",year,"is Monday")
        if rem == 2:
            print("September 1",year,"is Tuesday")
        if rem == 3:
            print("September 1",year,"is Wednesday")
        if rem == 4:
            print("September 1",year,"is Thursday")
        if rem == 5:
            print("September 1",year,"is Friday")
        if rem == 6:
            print("September 1",year,"is Saturday")
        day = day + 30
    i+=1
    if i==10:
        rem = day%7
        if rem == 0:
            print("October 1",year,"is Sunday")
        if rem == 1:
            print("October 1",year,"is Monday")
        if rem == 2:
            print("October 1",year,"is Tuesday")
        if rem == 3:
            print("October 1",year,"is Wednesday")
        if rem == 4:
            print("October 1",year,"is Thursday")
        if rem == 5:
            print("October 1",year,"is Friday")
        if rem == 6:
            print("October 1",year,"is Saturday")
        day = day + 31
    i+=1
    if i==11:
        rem = day%7
        if rem == 0:
            print("November 1",year,"is Sunday")
        if rem == 1:
            print("November 1",year,"is Monday")
        if rem == 2:
            print("November 1",year,"is Tuesday")
        if rem == 3:
            print("November 1",year,"is Wednesday")
        if rem == 4:
            print("November 1",year,"is Thursday")
        if rem == 5:
            print("November 1",year,"is Friday")
        if rem == 6:
            print("November 1",year,"is Saturday")
        day = day + 30
    i+=1
    if i==12:
        rem = day%7
        if rem == 0:
            print("December 1",year,"is Sunday")
        if rem == 1:
            print("December 1",year,"is Monday")
        if rem == 2:
            print("December 1",year,"is Tuesday")
        if rem == 3:
            print("December 1",year,"is Wednesday")
        if rem == 4:
            print("December 1",year,"is Thursday")
        if rem == 5:
            print("December 1",year,"is Friday")
        if rem == 6:
            print("December 1",year,"is Saturday")
        day = day + 31
    i+=1