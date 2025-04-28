def median_num(nums):
    '''
    using floor division on the sum of the two midlle numbers (float should be allowed for the final answer)
    '''
    if nums:
        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        return (nums[len(nums)//2] + nums[(len(nums)//2)-1])//2
