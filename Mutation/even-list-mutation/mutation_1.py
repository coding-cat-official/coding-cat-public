def even_list_mutation(numbers):
    '''
    simple mistake, divided by 2 instead of modulus 2
'''
    even_numbers = []
    for num in numbers:
        if num / 2 == 0:    # mutated: wrong arithmetic operator
            even_numbers.append(num)
    return even_numbers

