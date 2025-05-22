def range_chars_mutation(a: str, b: str) -> str:
    '''
        Compares a[i - 1] with a[i] rather than comparing b[i - 1] with a[i]
    '''
    result = ""

    for i in range(len(a)):
        
        if (b[i] == a[i]) or (i > 0 and a[i - 1] == a[i]) or (i < len(a) - 1 and b[i + 1] == a[i]):
            result += a[i]  

    return result