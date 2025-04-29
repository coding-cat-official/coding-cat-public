def add_evens_mutation(numbers):
    '''
    wrong indentation, returning the sum of the first even element of the list instead of the sum of all even numbers in the list
    '''
    list1 = []
    for x in range(len(numbers)):
        if numbers[x] % 2 == 0:
            list1 = list1 + [numbers[x]]
            return numbers + [sum(list1)]
