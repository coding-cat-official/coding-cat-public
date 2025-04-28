def ordered_sequence(nums):
    '''
    index out of range
    '''
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i+1] == 1 and nums[i+2] == 4:
            return True
    return False

