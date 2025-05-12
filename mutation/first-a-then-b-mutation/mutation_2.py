def first_a_then_b_mutation(list_ab: list) -> list:
    '''
    Comparing the index to the characters
    '''
    A = []
    B = []
    for char in range(len(list_ab)):
        if char == "a":
            A.append(list_ab[char])
        elif char == "b":
            B.append(list_ab[char])
    return A + B
