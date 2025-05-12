def remove_vowels_2_mutation(word: str, y_is_a_vowel: bool) -> str:
    vowels = "aeiouAEIOU"
    vowels += "yY" if y_is_a_vowel else ""
    result = ""
    for letter in word or letter == " ":
        if letter not in vowels:
            result += letter
    return result