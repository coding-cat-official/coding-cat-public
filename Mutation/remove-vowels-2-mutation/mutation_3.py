def remove_vowels_2_mutation(word: str, y_is_a_vowel: bool) -> str:
    '''
    Assigning "yY" to vowels if y_is_a_vowel is True instead of adding it to the vowels string
    '''
    vowels = "aeiouAEIOU"
    vowels = "yY" if y_is_a_vowel else ""
    result = ""
    for letter in word:
        if letter not in vowels:
            result += letter
    return result