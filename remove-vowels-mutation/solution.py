def remove_vowels(strng: str) -> str:
    """
    Correct implementation of remove_vowels function.
    """
    result = ""

    for i in strng:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            result = result + i
    return result