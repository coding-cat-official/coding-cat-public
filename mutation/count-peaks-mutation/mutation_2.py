def count_peaks_mutation(nums):
    """
        Used OR instead of AND in the second if statement.
    """    
    count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] or nums[i] > nums[i + 1]: #Wrong logical operator on this line.
            count += 1
    return count

