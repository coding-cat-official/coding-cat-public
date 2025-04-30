def sum_of_odd_numbers_mutation(lst):
    '''
	Checks for even instead of odd numbers
    '''
    sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:  # Checks for even numbers
            if lst[i] != lst[0] and lst[i] != lst[-1]:
                sum += lst[i]
    return sum
