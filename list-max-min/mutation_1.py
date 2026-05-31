def list_max_min(nums):
    '''
    By adding an equality checker to the second if statement we miss test cases of numbers that sum up to exactly 30 because we will remove the last value from the list
    '''
    l = []
    max_val = max(nums)
    min_val = min(nums)
    if max(nums) + min(nums)<=0:
        return 0
    while sum(l) < 30:
        l.append(max_val+min_val)
    if sum(l) >= 30:
        l.remove(l[0])
    return l
