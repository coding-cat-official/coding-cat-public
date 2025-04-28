def add_evens(numbers):
    '''
    correct implementation
    '''
    total = 0
    for x in numbers:
        if x % 2 == 0:
            total = total + x
    numbers.append(total)
    return numbers
