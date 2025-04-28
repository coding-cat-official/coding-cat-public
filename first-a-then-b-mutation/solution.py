def first_a_then_b(list_ab: list) -> list:
    A = []
    B = []
    for char in range(len(list_ab)):
        if list_ab[char] == "a":
            A.append(list_ab[char])
        elif list_ab[char] == "b":
            B.append(list_ab[char])
    return A + B
