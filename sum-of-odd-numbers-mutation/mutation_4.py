def sum_of_odd(lst):
    '''
	Returns lst instead of sum
    '''
    sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            if lst[i] != lst[0] and lst[i] != lst[-1]:
                sum += lst[i]
    return lst	     # Wrong return
