def median_num_mutation(nums):
    '''
    Forgetting brackets around the final return (second term is being divided by 2 instead of the whole sum)
    '''
    if nums:
        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        return nums[len(nums)//2] + nums[(len(nums)//2)-1]/2
