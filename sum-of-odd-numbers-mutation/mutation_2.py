def sum_of_odd(lst):
    '''
	Starts at range 1 instead of 0
    '''
    sum = 0
    for i in range(1, len(lst)):  # Mutated range: starts at 1 instead of 0
        if lst[i] % 2 == 1:
            if lst[i] != lst[0] and lst[i] != lst[-1]:
                sum += lst[i]
    return sum
