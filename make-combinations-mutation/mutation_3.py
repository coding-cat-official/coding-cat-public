def make_combinations(letters, numbers):
    '''
    Uses 'letters' instead of 'numbers' in the inner loop.
    '''
    return [[letter, number] for letter in letters for number in letters]