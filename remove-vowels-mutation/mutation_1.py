def remove_vowels(strng: str) -> str:
    """
    Bug: Implementation that uses the wrong operators
    """

    result = ""

    for i in strng:
        if i == "a" and i == "e" and i == "i" and i == "o" and i == "u": # used "==" instead of "!="
            result = result + i
    return result