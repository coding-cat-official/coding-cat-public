def sum_digits_mutation(n: int) -> int:
    '''
    adds the wrong part of the number (dividing by 10 instead of taking the remainder)
    '''
    total = 0
    while n > 0:
        total += n // 10
        n //= 10
    return total