def double_odd_mutation(i_list):
    '''
    Missing the index skip to properly check the values at odd index 
    ''' 
    new_list = []
    for i in range(1, len(i_list)):
        if i_list[i] % 2 != 0:
            new_list.append(i_list[i])
    return new_list
