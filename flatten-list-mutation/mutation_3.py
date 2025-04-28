def flatten_list(lst):
    '''
    Changed result.append(i) to result.append(lst) rendering the function to always append the list itself instead of the element.
    '''
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(lst)
    return result