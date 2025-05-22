def vowel_capitalization_mutation(s):
    '''
        Mutation 3: Includes 'y' as a vowel
    '''
    vowels = 'aeiouy'  # 'y' is added to the set of vowels
    result = ''
    for char in s:
        if char.lower() in vowels:
            result += char.upper()
        else:
            result += char
    return result
