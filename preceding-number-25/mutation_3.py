def preceding_number25(lst):
    '''
        Forgot to consider numbers that are not 2 or 5
    '''
    result = []
    for num in lst:
        if num == 2:
            result.append(5)
            result.append(2)
        elif num == 5:
            result.append(2)
            result.append(5)

    return result
