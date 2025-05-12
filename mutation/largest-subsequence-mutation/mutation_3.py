def largest_subsequence_mutation(nums, is_even):
    '''
    max now compares the last 2 elements and return the highest
    '''
    if is_even:
        nums = [num if num % 2 == 0 else 0 for num in nums]
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    lst = [0] * n
    lst[0], lst[1] = nums[0], max(nums[0], nums[1])
    for i in range(0, n):
        lst[i] = max(nums[i], nums[i - 1])  # compares last 2 here and takes the max.

    return lst[-1]
