def make_combinations_mutation(letters, numbers):
    '''
    Iterates over 'numbers' first instead of 'letters'.
    '''
    return [[letter, number] for number in numbers for letter in letters]
