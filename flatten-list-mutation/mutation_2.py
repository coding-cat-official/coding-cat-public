def flatten_list_mutation(lst):
    '''
    Changed the type comparison from type(i) == lst to type(i) == list rendering the if condition always false.
    '''
    result = []
    for i in lst:
        if type(i) == lst:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result