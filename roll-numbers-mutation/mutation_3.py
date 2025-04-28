def assign_roll_numbers(students):
    '''
       Forgetting to Sort the List
    '''    
    if not students or any(student=="" for student in students):
        return "Invalid list"
    
    roll_numbered_list = [[i+1, students[i]] for i in range(len(students))]
    return roll_numbered_list
