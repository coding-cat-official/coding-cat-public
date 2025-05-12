def range_chars_mutation(a: str, b:str) -> str:
    result = ""
    for i in range(len(a)):
        if (b[i] == a[i]) or (i > 0 and b[i - 1] == a[i]) or (i < len(a) - 1 and b[i + 1] == a[i]):
            result += a[i] 
    return result