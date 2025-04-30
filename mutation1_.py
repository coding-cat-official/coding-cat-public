def range_chars(a: str, b: str) -> str:
    """
     This code does not handle strings of different lengths correctly
     Some inputs will still work if b is longer which is wrong
    """
    result = ""
    for i in range(len(a)):
        if (i > 0 and a[i] == b[i-1]) or a[i] == b[i] or (i < len(a) - 1 and a[i] == b[i+1]):
            result += a[i]
    return result
