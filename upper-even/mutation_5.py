def upper_even_i(string):
    '''
    Missing return statement
    '''
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i].lower()
    # Missing <return result>
