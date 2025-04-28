def double_odd(i_list):
    ''''
    using an "and" to connect the logic of the odd index and the odd value at that index instead of putting the does not equalsign in both of them 

    ''' 

    new_list = []
    for i in range(len(i_list)):
        if i_list[i] and i % 2 != 0:
            new_list.append(i_list[i])
        
    return new_list
