def sum_of_odd_numbers_mutation(lst):
    '''
	Forgets to check the first and last numbers
    '''
    sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            # Mutated: Removed checks for lst[0] and lst[-1]
            sum += lst[i]
    return sum
