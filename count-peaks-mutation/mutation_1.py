def count_peaks_mutation(nums):
    """
        Small mistake, change the second comparison operator in the if statement.
    """
    count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] < nums[i + 1]: #Second comparison operator on this line.
            count += 1
    return count
