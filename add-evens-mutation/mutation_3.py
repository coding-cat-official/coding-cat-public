def add_evens_mutation(numbers):
    '''
    checking for odd numbers instead of even numbers
    '''
    total = 0
    for x in numbers:
        if x % 2 == 1:
            total = total + x
    numbers.append(total)
    return numbers
