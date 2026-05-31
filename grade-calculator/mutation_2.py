def final_grade(list):
"""
This mutatin changes the selection of grades from list[2:] to list[:4]. retaining the fitst 4 
elements rather than discarding the lowest two.
"""
    if len(list) == 6:
        list.sort()
        grade = list[:4]
        average = round(sum(grade) / len(grade))
        if average < 60:
            return(0)
        else:
            return(average)
    else:
        return(0)
