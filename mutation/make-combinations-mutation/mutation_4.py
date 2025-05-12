def make_combinations_mutation(letters, numbers):
    '''
    Uses 'numbers' instead of 'letters' in the inner loop.
    '''
    return [[letter, number] for letter in numbers for number in numbers]