def flatten_list_mutation(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list_mutation(i))
        else:
            result.append(i)
    return result