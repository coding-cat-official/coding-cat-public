def count_peaks_mutation(nums):
    """
        Forgot to return the statement.
    """
    count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            count += 1
# Missing a return statement in this line
