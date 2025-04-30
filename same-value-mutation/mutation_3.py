def same_value_mutation(array):
    '''
        Incorrect operator
    '''
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]: # Should be ==, not >=
            return True
    
    return False