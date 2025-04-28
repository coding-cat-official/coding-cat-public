def first_a_then_b(list_ab: list) -> list:
    '''
    Appending the index instead of the character
    '''
    A = []
    B = []
    for char in range(len(list_ab)):
        if list_ab[char] == "a":
            A.append(char)
        elif list_ab[char] == "b":
            B.append(char)
    return A + B
