def every_other_repeated(a, b):
    '''
        Mutation 2: instead of comparing 2 characters with 2 characters, it compares a single one with a pair
    '''

    count = 0 
    
    for i in range(len(a) - 2):
        if a[i] + a[i+2] == b[-2:][0]:
            count +=1
    return count
