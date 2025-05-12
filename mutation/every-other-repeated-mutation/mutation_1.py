def every_other_repeated_mutation(a, b):
    '''
        Mutation 1: loop goes over range that skips every other index (misses some)
    '''
    
    count = 0

    for i in range(0, len(a) - 2, 2):
        if a[i] + a[i+2] == b[-2:]:
            count += 1
    return count
