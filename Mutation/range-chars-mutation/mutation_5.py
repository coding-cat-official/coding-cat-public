def range_chars_mutation(a: str, b:str) -> str:
    result = ""
    '''
        Does result + a[i] instead of += making the result never update throughout the loop and just return an empty string
    '''
    for i in range(len(a)):
        if (b[i] == a[i]) or (i > 0 and b[i - 1] == a[i]) or (i < len(a) - 1 and b[i + 1] == a[i]):
            result + a[i] 
    return result
