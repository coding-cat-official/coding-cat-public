def consecutive_count_mutation(nums):
    '''
    One too many indents on return statement
    '''
    count = 0
    for n in range(len(nums)-1):
        if nums[n] == nums[n+1]:
            count += 1
        return count