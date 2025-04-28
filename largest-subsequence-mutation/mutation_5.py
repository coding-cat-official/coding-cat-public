def largest_sum(nums, is_even):
    '''
    removed flow control for is_even. Doesn't check parity
    '''
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    lst = [1] * n
    lst[0] = nums[0]
    lst[1] = max(nums[0], nums[1])
    for i in range(2, n):
        lst[i] = max(lst[i - 1], lst[i - 2] + nums[i])
    return lst[-1]
