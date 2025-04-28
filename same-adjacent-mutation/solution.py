def same_adjacent(str, char):
    '''
        Correct implementation
    '''
    count = 0
    adjacent = False
    for i in range(len(str)):
        if str[i] == char:
            count += 1
            if i > 0 and str[i-1] == char:
                adjacent = True
    return count if adjacent else 0
