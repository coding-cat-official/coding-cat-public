def have_three_mutation(nums):
    if nums.count(3) != 3:
        return False
        
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return False
    return True
