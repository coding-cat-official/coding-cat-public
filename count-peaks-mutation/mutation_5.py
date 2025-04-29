def count_peaks_mutation(nums):
    """
        Wrong return indentation, should be in the same level of indentation as the for statement.
    """
    count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            count += 1
        return count #Indentation bug here

