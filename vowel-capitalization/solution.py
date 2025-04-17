def vowel_caps(s):
    '''
        Correct implementation
    '''
    vowels = 'aeiou'
    result = ''
    for char in s:
        if char.lower() in vowels:
            result += char.upper()
        else:
            result += char
    return result
