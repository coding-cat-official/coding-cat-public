def adjacent_vowels_mutation(word: str) -> int:
    """
    Wrong length check
    """
    vowels = "aeiouAEIOU"
    if len(word) < 3:
        return 1
    if word[0] in vowels and word[1] in vowels:
        return 1 + adjacent_vowels(word[1:])

    return adjacent_vowels(word[1:])

