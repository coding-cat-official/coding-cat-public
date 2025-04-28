def assign_roll_numbers(students):
    '''
       Correct implementation
    '''    
    if not students or any(student=="" for student in students):
        return "Invalid list"
    sorted_students = sorted(students)
    roll_numbered_list = [[i+1, sorted_students[i]] for i in range(len(sorted_students))]
    return roll_numbered_list
