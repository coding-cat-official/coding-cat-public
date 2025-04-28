def remove_vowels(strng: str) -> str:
    """
    Bug: Implementation that does not create an empty result string
    """
# Does not create an empty result string

    for i in strng:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            result = i
    return ""