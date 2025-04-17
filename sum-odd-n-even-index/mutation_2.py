def sum_oddneven_list(input_list):
    '''
    Putting the behavior for when the list length is even in the if statement for when the list length is odd and vice-versa
    '''
    output = 0
    if(len(input_list) % 2 != 0):
        for i in range(len(input_list)):
            if i % 2 != 0:
                output += input_list[i]
    else:
        for i in range(len(input_list)):
            if i % 2 == 0:
                output += input_list[i]
    return output
