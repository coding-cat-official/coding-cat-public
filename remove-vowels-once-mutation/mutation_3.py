def remove_vowels_once_mutation(word: str) -> str:
    '''
    Wrong function for the return statement
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
    return set(result)
