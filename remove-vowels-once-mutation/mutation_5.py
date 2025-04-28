def remove_vowels_once(word: str) -> str:
    '''
    letters separated in the form of a set
    '''
    vowels = "aeiouyAEIOUY"
    seen_vowels = set()
    result = []
    for char in word:
        if char in vowels:
            if char not in seen_vowels:
                seen_vowels.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return result
