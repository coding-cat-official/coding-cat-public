def median_num(nums):
    '''
    Forgetting the final division
    '''
    if nums: 
        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        return (nums[len(nums)//2] + nums[(len(nums)//2)-1])
