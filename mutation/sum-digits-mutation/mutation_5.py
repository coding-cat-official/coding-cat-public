def sum_digits_mutation(n: int) -> int:
    '''
    uses =+ instead of += so the running total never accumulates
    '''
    total = 0
    while n > 0:
        total =+ n % 10
        n //= 10
    return total