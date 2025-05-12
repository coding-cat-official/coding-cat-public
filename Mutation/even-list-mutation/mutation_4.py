def even_list_mutation(numbers):
    '''
    Logical error: compares indeces, not the actual number
'''
    even_numbers = []
    for num in range(len(numbers)): # Mutation: used range and len functions
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
