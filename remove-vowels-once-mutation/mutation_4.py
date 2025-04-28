def remove_vowels_once(word: str) -> str:
    '''
    forgot a logical operator
    '''
    vowels = "aeiouyAEIOUY"
    seen_vowels = set()
    result = []
    for char in word:
        if char in vowels:
            if char in seen_vowels:
                seen_vowels.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)
