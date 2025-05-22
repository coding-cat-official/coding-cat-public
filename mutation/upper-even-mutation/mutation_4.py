def upper_even_mutation(string):
    '''
    Mutation 4:

    Add to result
    the wrong character
    at the wrong index (i-1)
    
    '''
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i-1].upper()
        else:
            result += string[i-1].lower()
    return result
