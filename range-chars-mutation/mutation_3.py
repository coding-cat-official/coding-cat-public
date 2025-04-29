def range_chars_mutation(a: str, b:str) -> str:
    '''
        Changes "<" into ">"on line 8 after the second or statement making that condition always False which removes the logic that checks if a matches b
    '''
    result = ""
    for i in range(len(a)):
        if (b[i] == a[i]) or (i > 0 and b[i - 1] == a[i]) or (i > len(a) - 1 and b[i + 1] == a[i]):
            result += a[i] 
    return result