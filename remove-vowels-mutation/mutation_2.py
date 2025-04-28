def remove_vowels(strng: str) -> str:
    """
    Bug: Implementation with one incorrect comparison
    """

    result = ""

    for i in strng:
        if i != "a" and i != "e" and i != "i" and i == "o" and i != "u": # used "==" instead of "!=" for o
            result = result + i
    return result