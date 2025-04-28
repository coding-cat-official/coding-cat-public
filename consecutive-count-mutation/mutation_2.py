def consecutive_count(nums):
    '''
    Comparing to pos -1 instead of +1
    '''
    count = 0
    for n in range(len(nums)-1):
        if nums[n] == nums[n-1]:
            count += 1
    return count