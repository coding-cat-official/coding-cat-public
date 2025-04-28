def countRepeat(a, b):
    '''
        No return statement
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
            previous_is_b = False

    #Missing return statement here
            
