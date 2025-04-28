def remove_vowels_once(word: str) -> str:
    '''
    Missing the capital vowels
    '''
    vowels = "aeiouy"
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
