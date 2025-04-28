def add_evens(numbers):
    '''
    returning the sum instead of the the whole list with the sum appended to the end
    '''
    total = 0
    for x in numbers:
        if x % 2 == 0:
            total = total + x
    return total
