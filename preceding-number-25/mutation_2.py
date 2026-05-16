def preceding_number25(lst):
    '''
        Reversed the order of the appended values.
    '''
    result = []
    for num in lst:
        if num == 2:
            result.append(2)
            result.append(5)
        elif num == 5:
            result.append(5)
            result.append(2)
        else:
            result.append(num)
    return result
