def largest_subsequence_mutation(nums, is_even):
    if is_even:
        nums = [num if num % 2 == 0 else 0 for num in nums]
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    lst = [0] * n
    lst[0], lst[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        lst[i] = max(lst[i - 1], lst[i - 2] + nums[i])
    return lst[-1]
