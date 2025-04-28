def count_peaks(nums):
    """
        "count" variable should add a 1 not equal 1 if the if-statement is met.
    """
    count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            count == 1 # Problem here
    return count

