def list_splitter_mutation(a):
    """
    Iterating while removing elements causes it to skip over some elements
    """
    for i, n in enumerate(a):
        if type(n) != str:
            a.pop(i)
    return a
