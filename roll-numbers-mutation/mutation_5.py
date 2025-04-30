def roll_numbers_mutation(students):
    '''
       Duplicating Roll Numbers (Forgot to put i+1 and instead put 1)
    '''    
    if not students or any(student=="" for student in students):
        return "Invalid list"
    sorted_students = sorted(students)
    roll_numbered_list = [[1, sorted_students[i]] for i in range(len(sorted_students))]
    return roll_numbered_list
