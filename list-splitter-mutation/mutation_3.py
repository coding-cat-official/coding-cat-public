def elementArranger(a):
    """
    Incorrectly checks type ("str" should simply be str)
    """
    return [n for n in a if type(n) == "str"]
