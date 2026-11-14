def sum_digits_mutation(n: int) -> int:
    '''
    stops one digit too early, so the last (ones) digit is never added
    '''
    total = 0
    while n > 1:
        total += n % 10
        n //= 10
    return total