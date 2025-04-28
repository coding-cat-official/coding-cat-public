def sum_oddneven_list(input_list):
    '''
    Limiting the range function as if "look ahead" for loop is used when it isn't
    '''
    output = 0
    if(len(input_list) % 2 == 0):
        for i in range(len(input_list)-1):
            if i % 2 != 0:
                output += input_list[i]
    else:
        for i in range(len(input_list)-1):
            if i % 2 == 0:
                output += input_list[i]
    return output
