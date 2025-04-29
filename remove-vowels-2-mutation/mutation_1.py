def remove_vowels_2_mutation(word: str, y_is_a_vowel: bool) -> str:
    '''
    Forgeting to add the uppercase vowels to the vowels string
    '''
    vowels = "aeiou"
    vowels += "y" if y_is_a_vowel else ""
    result = ""
    for letter in word:
        if letter not in vowels:
            result += letter
    return result