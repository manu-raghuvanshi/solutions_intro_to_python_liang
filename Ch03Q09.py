import math
name = input("Enter Employee's Name:")
hours = eval(input("Enter number of hours worked in a week:"))
pay = eval(input("Enter hourly pay rate:"))
federal = eval(input("Enter federal tax withholding rate in percentage:"))
state = eval(input("Enter state tax withholding rate in percentage:"))

gross = hours*pay #calculated Gross Pay
fed = (federal/100)*gross #calculated Federal Withholding tax
sta = (state/100)*gross #calculated State Withholding tax
net = gross - (fed + sta) #calculated Net Withholding tax

print("")
print("Employee name:",name)
print("Hours Worked:$",hours)
print("Pay Rate:$",pay)
print("Gross Pay:$",(hours*pay))
print("Deductions:")
print("   Federal Withholding (",federal,"%):",format(fed,".2f"))
print("   State Withholding (",state,"%):",format(sta,".2f"))
print("   Total Deduction:$",format(fed+sta,".2f")) #total of federal tax and state tax
print("Net Pay:$",format(net,".2f"))