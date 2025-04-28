def is_same(array):
    '''
        Forgot return statement at end
    '''
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True
    # Missing return statement here