def elementArranger(a):
    """
    Leaves the possibility of floats getting into the new list
    """
    strings = []
    for n in a:
        if type(n) == int:
            continue
        else:
            strings.append(n)
    return strings
