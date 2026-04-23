def range_chars(a: str, b: str) -> str:
    result = ""
    n = min(len(a), len(b))  # Ensure we only iterate up to the shortest string length
    for i in range(n):
        if (i > 0 and a[i] == b[i-1]) or a[i] == b[i] or (i < n - 1 and a[i] == b[i+1]):
            result += a[i]
    return result
