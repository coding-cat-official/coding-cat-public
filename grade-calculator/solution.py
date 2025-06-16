def final_grade(list):
	if len(list) == 6:
		list.sort() """It will arrange the list in an increasing order"""
		grade = list[2:] """Removes the two lowest values"""
		average = round(sum(grade) / len(grade)) # Finds the average
		if average < 60:
			return(0) 
		else:
			return(average)
	else:
		return(0)

