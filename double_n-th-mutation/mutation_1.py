def double_nth(str,n):
    """
    Bug: Repeats all characters in the string instead of only the n-th character.
    """
    if n <= 0 or not str:
        return ""
    if n > len(str):
        return str

    result = []
    for i, char in enumerate(str):
        result.append(char * 2)  # Repeats all characters
    return "".join(result)
