def is_same(array):
    '''
        Incorrectly modify loop boundary
    '''
    for i in range(len(array) - 2): # Should be - 1
        if array[i] == array[i + 1]:
            return True
    return False