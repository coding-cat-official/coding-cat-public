def first_a_then_b_mutation(list_ab: list) -> list:
    '''
    elif replaced by else
    '''
    A = []
    B = []
    for char in range(len(list_ab)):
        if list_ab[char] == "a":
            A.append(list_ab[char])
        else:
            B.append(list_ab[char])
    return A + B
