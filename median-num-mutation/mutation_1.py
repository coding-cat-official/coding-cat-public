def median_num(nums):
    '''
    checking the wrong modulo (filtering out evens instead of odds)
    '''
    if nums:
        if len(nums) % 2 == 0:
            return nums[len(nums)//2]
        return (nums[len(nums)//2] + nums[(len(nums)//2)-1])/2
