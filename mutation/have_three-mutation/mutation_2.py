def have_three_mutation(nums):
    '''
        Returns True after only 1st element
    '''
    if nums.count(3) != 3:
        return False
        
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] != 3:
            return True
    return True
