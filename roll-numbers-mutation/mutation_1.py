def roll_numbers_mutation(students):
    '''
       Skipping empty string check
    '''    
    if not students:
        return "Invalid list"
    sorted_students = sorted(students)
    roll_numbered_list = [[i+1, sorted_students[i]] for i in range(len(sorted_students))]
    return roll_numbered_list
