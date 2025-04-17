def vowel_caps(s):
    '''
        Mutation 5: Returns a list instead of a string
    '''
    vowels = 'aeiou'
    result = []
    for char in s:
        if char.lower() in vowels:
            result.append(char.upper())  # Appending uppercase vowel
        else:
            result.append(char)          # Appending consonant as is
    return result  # Returns a list instead of a string
