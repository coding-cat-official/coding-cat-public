def range_chars(a: str, b: str) -> str:
    """
    Buggy Mutation: using a[i] == b[i]
    This creates incorrects matches when a characters should not be included
    """
    result = ""
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] == b[i] or (i > 0 and a[i] == b[i-1]) or (i < n - 1 and a[i] == b[i+1]):
            result += a[i]
    return result
