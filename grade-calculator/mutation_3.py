def final_grade(list):
"""
This mutation replaces / to //, using integer divison truncates the result instead of rounding it
which can lead to average being lower than intended.
"""
    if len(list) == 6:
        list.sort()
        grade = list[2:]
        average = round(sum(grade) // len(grade))
        if average < 60:
            return(0)
        else:
            return(average)
    else:
        return(0)
