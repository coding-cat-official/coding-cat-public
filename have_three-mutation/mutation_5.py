def have_3_threes(nums):
    '''
	Returns True just based on count
    '''
    if nums.count(3) == 3:
        return True
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return False
    return False
