def sum_7_mutation(list_a, list_b):
    '''
        Wrong relational operator (==)
    '''
    count = 0
    # assigns a tuple that takes in all the combinations
    pairs = [(int_a, int_b) for int_a in list_a for int_b in list_b]

    # directly additions and tests if the pair is a sum of 7
    for i in pairs:
        if i[0] + i[1] != 7:
            count += 1
    
    return count
