def double_n_th_mutation(str,n):
    """
    Bug: Forgets to join the list of characters into a string at the end.
    """
    if n <= 0 or not str:
        return ""
    if n > len(str):
        return str

    result = []
    for i, char in enumerate(str):
        if (i + 1) % n == 0:
            result.append(char * 2)
        else:
            result.append(char)
    return result 
