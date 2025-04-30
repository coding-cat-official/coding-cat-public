def upper_even_mutation(string):
    '''
    Mutation 1:

    Change
    i % 2 == 0
    to 
    i % 2 == 1
    
    This means the characters 
    at the wrong index
    will be lower and upper case

    '''
    result = ""
    for i in range(len(string)):
        if i % 2 == 1:
            result += string[i].upper()
        else:
            result += string[i].lower()
    return result
