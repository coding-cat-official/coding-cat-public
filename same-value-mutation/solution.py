def is_same(array):
    '''
        Correct implementation
    '''
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True
    
    return False