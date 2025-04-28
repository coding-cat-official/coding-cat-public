def first_a_then_b(list_ab: list) -> list:
    '''
    Wrong range
    '''
    A = []
    B = []
    for char in range(len(list_ab) - 1):
        if list_ab[char] == "a":
            A.append(list_ab[char])
        elif list_ab[char] == "b":
            B.append(list_ab[char])
    return A + B
