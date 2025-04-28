def largest_sum(nums, is_even):
    '''
    Implement greedy solution
    '''
    new_list = nums[::2]

    return sum(new_list)


