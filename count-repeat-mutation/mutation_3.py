def countRepeat(a, b):
    '''
        Incorrect order of variable assignment
    '''
    count = 0
    previous_is_b = False
    repeat_lock = False
    
    for i in a:  
        if i == b:
            previous_is_b = True #Mutated position of variable being assigned a value
            if previous_is_b == True and repeat_lock == False:  
                count += 1
                repeat_lock = True  
        else:
            repeat_lock = False
            previous_is_b = False

    return count 
