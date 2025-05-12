def count_repeat_mutation(a, b):
    '''
        Correct implementation/solution
    '''
    count = 0 # Variable used to store if the previous element was b 
    previous_is_b = False # Variable used to prevent overcounting a series of repetitions
    repeat_lock = False
    
    for i in a:  
        if i == b:  
            if previous_is_b == True and repeat_lock == False:  
                count += 1 # Once a repetition is counted, we have to prevent this from running in order to avoid overcounting
                repeat_lock = True  
            previous_is_b = True  
        else:  
            repeat_lock = False
            previous_is_b = False

    return count 
