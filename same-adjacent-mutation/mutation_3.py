def same_adjacent(str, char):
    '''
        Mistake: Incorrectly modify loop boundaries
    '''
    count = 0
    adjacent = False
    for i in range(1, len(str) - 1):    # Mutated loop limits 
        if str[i] == char:
            count += 1
            if str[i-1] == char or str[i+1] == char:    # Incorrectly checks on both sides
                adjacent = True
    return count if adjacent else 0
