def range_chars(a: str, b:str) -> str:
    '''
        Checks if b[i] is not equal to a[i] which reverse the logic
    '''
    result = ""
    for i in range(len(a)):
        if (b[i] != a[i]) or (i > 0 and b[i - 1] == a[i]) or (i < len(a) - 1 and b[i + 1] == a[i]):
            result += a[i] 
    return result