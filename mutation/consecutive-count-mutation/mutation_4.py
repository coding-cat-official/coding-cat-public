def consecutive_count_mutation(nums):
    '''
    Start at position - 1
    '''
    count = 0
    for n in range(-1,len(nums)-1):
        if nums[n] == nums[n+1]:
            count += 1
    return count