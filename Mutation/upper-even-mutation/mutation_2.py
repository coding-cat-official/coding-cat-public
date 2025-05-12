def upper_even_mutation(string):
    '''
    Mutation 2:

    Switch upper with lower
    and vice versa
    
    This means the wrong characters
    will be lower and upper case

    '''
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i].lower()
        else:
            result += string[i].upper()
    return result
