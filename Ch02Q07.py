minutes = eval(input("Enter the number of minutes:"))
total_days = int(minutes/(60*24)) #converts minutes to days
years = total_days // 365 #number of years in those days
rem_days = total_days - (years*365) #days remaining
print(minutes,"minutes is approximately",years,"years and",rem_days,"days")