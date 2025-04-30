def vowel_capitalization_mutation(s):
    '''
        Mutation 1: Replaces consonants instead of vowels
    '''
    vowels = 'aeiou'
    result = ''
    for char in s:
        if char.lower() not in vowels:  # Incorrect condition: targets consonants
            result += char.upper()      # Replaces consonants with uppercase
        else:
            result += char
    return result
