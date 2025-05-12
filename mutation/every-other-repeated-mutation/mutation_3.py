def every_other_repeated_mutation(a, b):
    '''
        loop looks at every consecutive number instead of every OTHER number
    '''

    count = 0

    for i in range(len(a) - 2):
        if a[i+1] + a[i+2] == b[-2:]:
            count += 1
    return count
