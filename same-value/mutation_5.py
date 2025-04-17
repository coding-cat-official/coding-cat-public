def is_same(array):
    '''
        Incorrect use of else statement
    '''
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True
        else:   # Remove else statement, and put this return statement outside the for loop
            return False