def have_3_threes(nums):
    '''
	Checks for consecutive 3's incorrectly(or instead of and)
    '''
    if nums.count(3) != 3:
        return False
    for i in range(len(nums) - 1):
        if nums[i] == 3 or nums[i + 1] == 3:
            return False
    return True
