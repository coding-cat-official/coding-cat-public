def is_same(array):
    '''
        Switched return statements
    '''
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return False # This should be return True
    
    return True # This should be return False