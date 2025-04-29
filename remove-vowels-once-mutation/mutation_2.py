def remove_vowels_once_mutation(word: str) -> str:
    '''
    Missing lowercase vowels
    '''
    vowels = "AEIOUY"
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
    return ''.join(result)
