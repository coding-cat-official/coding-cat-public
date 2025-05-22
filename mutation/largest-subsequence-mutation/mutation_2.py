def largest_subsequence_mutation(nums, is_even):
    '''
    greedy but less greedy implementation
    '''
    if len(nums) % 2 == 0:
        new_list = nums[1::2]
    else:
        new_list = nums[::2]

    return sum(new_list)
