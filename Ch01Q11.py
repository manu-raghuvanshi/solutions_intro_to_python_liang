current_population = 312032486
birth = ((365*24*60*60)//7)*5 #Total births in the next five years
death = ((365*24*60*60)//13)*5 #Total deaths in the next five years
immigrant = ((365*24*60*60)//45)*5 #Total immigrants in the next five years
projected_population = current_population + birth - death + immigrant
print ("Projected Population after 5 years", projected_population)