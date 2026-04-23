def range_chars(a: str, b: str) -> str:
    """
    Buggy Mutation: using >= instead of >
    This will try to compare a[0] with b[-1] which is wrong and creates bugs
    """
    result = ""
    n = min(len(a), len(b))  
    for i in range(n):
        if (i >= 0 and a[i] == b[i-1]) or a[i] == b[i] or (i < n - 1 and a[i] == b[i+1]):
            result += a[i]
    return result
