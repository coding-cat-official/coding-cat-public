def same_adjacent_mutation(str, char):
    '''
        Mistake: Variable set to incorrect boolean
    '''
    count = 0
    adjacent = True     # Returns the count, even if no adjacent chars
    for i in range(len(str)):
        if str[i] == char:
            count += 1
            if i > 0 and str[i-1] == char:
                adjacent = True
    return count if adjacent else 0
