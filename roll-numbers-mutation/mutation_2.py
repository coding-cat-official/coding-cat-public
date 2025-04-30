def roll_numbers_mutation(students):
    '''
       Incorrect roll number assignment
    '''    
    if not students or any(student=="" for student in students):
        return "Invalid list"
    sorted_students = sorted(students)
    roll_numbered_list = [[i, sorted_students[i]] for i in range(len(sorted_students))]
    return roll_numbered_list
