def elementArranger(a):
    """
    Checks list indices instead of the elements
    """
    strings = []
    for i in range(len(a)):
        if type(i) == str:
            strings.append(i)
    return strings
