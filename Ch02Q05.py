subt, grat_rate = eval(input("Enter the subtotal and the gratuity rate:"))
grat = (grat_rate/100) * subt #calculates Gratuity rate
total = grat + subt #calculate total
print("The  gratuity rate is", format(grat, '.2f'),"and the total is", format(total, '.2f'))