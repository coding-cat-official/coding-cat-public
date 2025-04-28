def vowel_caps(s):
    '''
        Mutation 2: Replaces vowels with lowercase instead of uppercase
    '''
    vowels = 'aeiou'
    result = ''
    for char in s:
        if char.lower() in vowels:
            result += char.lower()  # Should be char.upper()
        else:
            result += char
    return result
