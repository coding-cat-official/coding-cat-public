def sum_digits_mutation(n: int) -> int:
    '''
    only works for the first two digits instead of the whole number
    '''
    if n < 10:
        return n
    return (n % 10) + (n // 10)