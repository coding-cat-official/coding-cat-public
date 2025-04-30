def preceding_number25(lst):
    '''
        Swapped to the wrong conditions for the if statements.
    '''
    result = []
    for num in lst:
        if num != 2:
            result.append(5)
            result.append(2)
        elif num != 5:
            result.append(2)
            result.append(5)
        else:
            result.append(num)
    return result

