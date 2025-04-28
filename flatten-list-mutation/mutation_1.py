def flatten_list(lst):
    '''
    Changed the extend method to append method, causing the function to return a list of lists instead of a flat list.
    '''
    result = []
    for i in lst:
        if type(i) == list:
            result.append(flatten_list(i)) # Changed extend to append
        else:
            result.append(i)
    return result