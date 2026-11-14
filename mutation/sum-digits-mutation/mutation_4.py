def sum_digits_mutation(n: int) -> int:
    '''
    string approach but ignores the last character of the digit string
    '''
    return sum(int(ch) for ch in str(n)[:-1])