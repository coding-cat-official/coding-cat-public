def vowel_caps(s):
    '''
        Mutation 4: Off-by-one error, skips the last character
    '''
    vowels = 'aeiou'
    result = ''
    for i in range(len(s) - 1):  # Off by one, skips last character
        char = s[i]
        if char.lower() in vowels:
            result += char.upper()
        else:
            result += char
    if len(s) > 0:
        result += s[-1]  # Adds the last character unchanged
    return result
