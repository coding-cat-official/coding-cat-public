def count_repeat_mutation(a, b):
    '''
        Incorrect resetting of `previous_is_b` 
    '''
    count = 0  
    previous_is_b = False
    repeat_lock = False
    
    for i in a:  
        if i == b:  
            if previous_is_b == True and repeat_lock == False:  
                count += 1
                repeat_lock = True  
            previous_is_b = True  
        else:  
            repeat_lock = False  
            previous_is_b = True # Mutated value: never resets to False

    return count 
