def final_grade(list):
"""
It process lists with lengths other than 6, goes against the requirement.

"""
    if len(list) != 6:
        list.sort()
        grade = list[2:]
        average = round(sum(grade) / len(grade))
        if average < 60:
            return(0)
        else:
            return(average)
    else:
        return(0)
