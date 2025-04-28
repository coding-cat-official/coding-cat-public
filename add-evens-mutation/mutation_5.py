def add_evens(numbers):
    '''
    the sum of all even numbers is being added to the list as the first element instead of the last
    '''
    list1 = []
    for x in range(len(numbers)):
        if numbers[x] % 2 == 0:
            list1 = list1 + [numbers[x]]
    return [sum(list1)] + numbers
